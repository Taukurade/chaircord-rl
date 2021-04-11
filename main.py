from flask import Flask, request, Response
from flask import render_template
import json
import asyncio
import requests
app = Flask(__name__)
membs=""


members=[
    {
        'name':'member1',
        'score':2211,
        'a_urls':'https://as2.ftcdn.net/jpg/01/17/16/11/500_F_117161164_mBhUQUTj1vXMJYlBLVBnwgaoeNihNv00.jpg',
        'roles':
        [
        {
            'name':'muted',
            'color':'#a1a1a1'
        },
        {
            'name':'man',
            'color':'#2595a8'
        },
        {
            'name':'dude you...',
            'color':'#b03030'
        }
        ]

    },
    {
        'name':'member2',
        'score':0,
        'a_urls':'https://floritime.ru/userfiles/shop/medium/2/12863_kashpo-nieuwkoop-alegria-random-square-rusted-.jpg',
        'roles':
        [
        {
            'name':'muted',
            'color':'#a1a1a1'
        },
        {
            'name':'YOLOOOOOOO',
            'color':'#25f5a8'
        },
        {
            'name':'dude you...',
            'color':'#b03030'
        }
        ]

    },
    {
        'name':'member4',
        'score':140,
        'a_urls':'https://forums.odforce.net/uploads/monthly_2019_05/l_pt_02510.jpg.beee0f7bfd018892e162cc146d08486c.jpg',
        'roles':
        [
        {
            'name':'muted',
            'color':'#a1a1a1'
        }
        ]

    },
    {
        'name':'member1',
        'score':-2,
        'a_urls':'https://as2.ftcdn.net/jpg/01/17/16/11/500_F_117161164_mBhUQUTj1vXMJYlBLVBnwgaoeNihNv00.jpg',
        'roles':
        [
        {
            'name':'muted',
            'color':'#a1a1a1'
        },
        {
            'name':'man',
            'color':'#2595a8'
        },
        {
            'name':'dude you...',
            'color':'#b03030'
        }
        ]

    },
    {
        'name':'member2',
        'score':22,
        'a_urls':'https://floritime.ru/userfiles/shop/medium/2/12863_kashpo-nieuwkoop-alegria-random-square-rusted-.jpg',
        'roles':
        [
        {
            'name':'muted',
            'color':'#a1a1a1'
        },
        {
            'name':'YOLOOOOOOO',
            'color':'#25f5a8'
        },
        {
            'name':'dude you...',
            'color':'#b03030'
        }
        ]

    },
    {
        'name':'member4',
        'score':14,
        'a_urls':'https://forums.odforce.net/uploads/monthly_2019_05/l_pt_02510.jpg.beee0f7bfd018892e162cc146d08486c.jpg',
        'roles':
        [
        {
            'name':'muted',
            'color':'#a1a1a1'
        }
        ]

    }
    ]
def srt(ex):
    return ex.get('score')
@app.route('/webhook/leaderboardoikjrngWPOIURGBLREGOVCQNHREWQLIGFPWQOHRUCGTEQR', methods=['POST'])
def respond():
    global members
    members=request.json
    return Response(status=200)
@app.route('/')
def hello_world():

    global members
    members.sort(key=srt,reverse=True)
    return render_template('index.html',members=members)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=80)
