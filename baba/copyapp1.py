from flask import Flask, request, abort
import requests
import json

from linebot import (
LineBotApi, WebhookHandler
)
from linebot.exceptions import (
InvalidSignatureError
)
from linebot.models import (
MessageEvent, TextMessage, TextSendMessage,
)


from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

from urllib.request import urlopen
from flask import make_response
import urllib
# import urllib2
import response
import urllib.request

import urllib3

app = Flask(__name__)

line_bot_api = LineBotApi('bp40QhnT1ZncneOuPam5XYaIF7y5FR4Cd0HYq53rJedoE5Lxsb5cN2q4GjpLinQdqEVDqV7tG8VDnpxLo8kLAQ0u3YVGKphURTLkpVIGrzt+6fYrNt10XuxA/CuK50Za06VZ7w6eC+UckhnlqqrZiQdB04t89/1O/w1cDnyilFU=') #I put my TOKEN
handler = WebhookHandler('fb59bf1fa17d60c08da1ac2619a0e0f7')

@app.route("/whline/line", methods=['GET'])
def my_get():
    return "Webhook for Line" , 200

#line
@app.route("/whbell/webhook2", methods=['POST'])
def callback():
# get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

# get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
#print(body)
# handle webhook body
    try:
        handler.handle(body, signature)
#print("Testtttt")
    except InvalidSignatureError:
        abort(400)

    return 'OK', 200


# #PRTG2 แบบง่ายๆปริ้นแค่ uo and down
# @app.route("/whbell/prtg", methods=['POST'])
# def prtg():
#     body = request.get_data(as_text=True)
#     print(body)
#     if body == "":
#         print("up")
#     else :
#         print("down")
#         body = ""
        
#     return 'OK', 200

# #รันได้แต่จะมีพวก % ติดอยู่
# @app.route("/whbell/prtg1", methods=["POST"])
# def prtg1():
#     r = request.get_data('https://10.17.1.28/api/getsensordetails.json?id=5396&username=prtgadmin&password=OishiGr3!')
#     print(r)
#     return r


@app.route("/whbell/prtg1", methods=["POST"])
def prtg1():
    r = request.get_data(as_text=True)
    # print(r)


    ree ='https://10.17.1.28/api/getsensordetails.json?id='+str(r)+'&username=prtgadmin&password=OishiGr3!'
    # print(ree)
    ree = str.encode('https://10.17.1.28/api/getsensordetails.json?id=5396&username=prtgadmin&password=OishiGr3!')
    # print(ree)
    


    re3 = 'https://10.17.1.28/api/getsensordetails.json?id=5396&username=prtgadmin&password=OishiGr3!'
    re4 = request.get_data(str.encode(re3))
    print(re4)
    

    ree = request.get_json(silent=True, force=True)
    res = processRequest(ree)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'

    return r
def processRequest(ree):

    # Parsing the POST request body into a dictionary for easy access.

    req_dict = json.loads(request.data)
    # print(req_dict)
    
    data1 ='https://10.17.1.28/api/getsensordetails.json?id='+str(req_dict)+'&username=prtgadmin&password=OishiGr3!'
    # print(data1)

    data2 = requests.get(data1, verify=False)
    print(data2)
    print(data2.json())
    y = json.dumps(data2.json())
    x = json.loads(y)
    a = (x['sensordata']['statustext'])
    print(a)
    b = str(a)
    print(b)
    sendText(b) 
    return b,200
    # return b

    
    

# @app.route("/whbell/prtg1", methods=["POST"])

# def prtg2(bo):
#     print("fn1"+bo)
#     json_line = request.get_json()
#     json_line = json.dumps(json_line)
#     decoded = json.loads(json_line)
#     user = decoded["events"][0]['replyToken']
    
    # id=[d['replyToken'] for d in user][0]
    # print(json_line)
    # print("ผู้ใช้：",user)
    # # print(b)
    # sendText(user,bo) 
    # # print(bo)
    # return bo,200


def sendText(text):
    print(text)
    # print("fn2"+text)
    # print("fn2.1"+user)
    LINE_API = 'https://api.line.me/v2/bot/message/push'
    Authorization = 'Bearer bp40QhnT1ZncneOuPam5XYaIF7y5FR4Cd0HYq53rJedoE5Lxsb5cN2q4GjpLinQdqEVDqV7tG8VDnpxLo8kLAQ0u3YVGKphURTLkpVIGrzt+6fYrNt10XuxA/CuK50Za06VZ7w6eC+UckhnlqqrZiQdB04t89/1O/w1cDnyilFU=' # ใส่ ENTER_ACCESS_TOKEN เข้าไป
    headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization':Authorization
    }
    data = json.dumps({
    "to": "Ubf2476da6dfd78c2a4f65d589140478f",
    "messages":[{"type":"text","text":text}]})
    #print("ข้อมูล：",data)
    # print(text)
    r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล
    #   print(r.text)





"""
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
line_bot_api.reply_message(
event.reply_token,
TextSendMessage(text=event.message.text))
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
