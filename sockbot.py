import discord
from discord.ext import commands,tasks
from discord.utils import get
import random
import sqlite3
import json
from datetime import datetime as dt
import threading as tr
import os
import asyncio
import requests
import psycopg2
mlist=[]




#const


DATABASE_URL = os.environ['DATABASE_URL']

cn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = cn.cursor()
#y = tr.Thread(target=get_members,daemon=True)

#l = tr.Thread(target=run, daemon=True)
cur.execute("select token, default_cfg from 'bot data'")
token = cur.fetchone()[0]
intents = discord.Intents().all()

bot = commands.Bot(command_prefix="-",intents=intents)
bot.remove_command("help")

def get_members():
    mlistx=[]
    global mlist
    for member in bot.get_guild(824959091532890133).members:
        cur.execute(f"select score from 'lb' where id={member.id}")
        if cur.fetchone() == None:
            cur.execute(f"insert into lb values ({member.id}, 0)")
            cur.execute(f"select score from 'lb' where id={member.id}")
            score=cur.fetchone()[0]
        else:
            cur.execute(f"select score from 'lb' where id={member.id}")
            score=cur.fetchone()[0]
        mname=f"{member.name}#{member.discriminator}"
        aurl=(str(member.avatar_url))
        rls=[]
        for role in member.roles:
            if role.name == "@everyone":
                continue
            rname=str(role.name)
            rcol=str(role.color)
            rls.append({'name':rname,'color':rcol})
        x={'name':mname,'a_urls':aurl,'score':score,'roles':rls}
        mlistx.append(x)
    mlist=json.dumps(mlistx)
    cn.commit()
    #print(mlist)





@bot.event
async def on_ready():
    print(f"{bot.user.name} {bot.user.id}")
    #y.start()
    data_send.start()

@tasks.loop(seconds=10)
async def data_send():
    get_members()
    r=requests.post("http://chaircord-rl.herokuapp.com:80/webhook/leaderboardoikjrngWPOIURGBLREGOVCQNHREWQLIGFPWQOHRUCGTEQR", headers={'Content-Type':'application/json'}, data=mlist)
    #print(r)

@commands.cooldown(rate=1, per=3600, type=commands.BucketType.user)
@bot.command()
async def vote(ctx,user: discord.Member,x: str):
    try:
        if user == ctx.author:
            ctx.command.reset_cooldown(ctx)
            await ctx.send("this is you, you cant")
        elif user.bot:
            ctx.command.reset_cooldown(ctx)
            await ctx.send("this is bot...")

        else:
            cur.execute(f"select score from lb where id={user.id}")
            d=cur.fetchone()[0]
            if x == "+":
                f=d+1
            elif x == "-":
                f=d-1
            else:
                ctx.command.reset_cooldown(ctx)
                await ctx.send("Wrong arguments.\nUsage: `-vote @member +/-`\nFor example:`-vote <@784785353533554688> -`")
            cur.execute(f"update lb set score={f} where id={user.id}")
            print('pass')
            await ctx.send("voted")
        cn.commit()
    except(discord.ext.commands.ArgumentParsingError,discord.ext.commands.MissingRequiredArgument) as e:
        ctx.command.reset_cooldown(ctx)
        await ctx.send(e)



@vote.error
async def v_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandOnCooldown):
        msg = 'This command is ratelimited, please try again in {:.0f}m'.format((error.retry_after/60))
        await ctx.send(f"`{msg}`")
    elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
        ctx.command.reset_cooldown(ctx)
        await ctx.send(f"Not enough arguments.\nUsage: `-vote @member +/-`\nFor example:`-vote <@784785353533554688> -`")
    elif isinstance(error, discord.ext.commands.ArgumentParsingError):
        ctx.command.reset_cooldown(ctx)
        await ctx.send(error)
    else:
        ctx.command.reset_cooldown(ctx)
        raise error

@bot.command()
async def test(ctx):
    await ctx.send(bot.guilds)





bot.run(token)
d=input()
if d == "":
    os.kill(0)
