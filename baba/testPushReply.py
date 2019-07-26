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




@app.route("/whbell/line2", methods=["POST"])
##รับค่าจากไลน์##
##############
def prtg2():
   
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    print(decoded)
    r = decoded["events"][0]['message']['text'] ##check text##
    #id=[d['replyToken'] for d in user][0]
    #print(json_line)
    s = str(r)
    
    ## ถ้า user พิมมาว่า hi ##
    if s == "hi":
        print("ผู้ใช้：",user)
        sendText(user,"hello")
        return "", 200
        # speech = "มีไรให้ช่วยยย"

    else:

    ##โหลด json จาก prtg
        data1 = 'https://10.17.1.28/api/getsensordetails.json?id=5396&username=prtgadmin&password=OishiGr3!'
        response = requests.get(data1, verify=False)
        print(response.text)
            # g = response.text
            # print(g)
            # s = (g['prtgversion']['statustext'])
            # print(s)
        y = json.dumps(response.json())
        x = json.loads(y)
        g = (x['sensordata']['statustext'])
        print(g)

        ##กำหนดข้อมูล
        print("ผู้ใช้：",user)
        sendText(user,g)
        # sendText1(user,g)

        return g,200


###ตอบข้อความไปไลน์ prtg2()###
#############################
def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer ym5ACrqHsZvCdxdhwtHvbQtr8SMLjU/Tzwbxv3Fa2c28RXWaOXU7/4adYdDsrXe9qEVDqV7tG8VDnpxLo8kLAQ0u3YVGKphURTLkpVIGrzuMqUIRbwyCu3YNMQTB4M+VlBppsxbQDQa+hPmLaRI0CAdB04t89/1O/w1cDnyilFU=' 
  headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Authorization':Authorization
  }
  data = json.dumps({
  "replyToken":user,
  "messages":[
        {
    "type": "template",
    "altText": "this is a carousel template",
    "template": {
        "type": "carousel",
        "actions": [],
        "columns": [
        {
            "thumbnailImageUrl": "SPECIFY_YOUR_IMAGE_URL",
            "title": "Title",
            "text": "Text",
            "actions": [
            {
                "type": "message",
                "label": "Action 1",
                "text": "Action 1"
            },
            {
                "type": "message",
                "label": "Action 2",
                "text": "Action 2"
            }
            ]
        }
        ]
    }
    }
      ]
      }
      )

# ##เรียกไฟล์ json##
#   with open('json1.js') as myfile:
#       ta=myfile.read()
#       taa = json.loads(ta)
#       print(taa)

  #print("ข้อมูล：",data)
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล
  #print(r.text)




@app.route("/whbell/prtg1", methods=["POST"])
###กดกระดิ่ง PRTG###
##################
def prtg1():
    r = request.get_data(as_text=True)
    # print(r)

    ##แปลง int เป็น string
    ree ='https://10.17.1.28/api/getsensordetails.json?id='+str(r)+'&username=prtgadmin&password=OishiGr3!'
    # print(ree)
    ree = str.encode('https://10.17.1.28/api/getsensordetails.json?id=5396&username=prtgadmin&password=OishiGr3!')
    # print(ree)
    
    ##เรียกข้อมูล json
    ree = request.get_json(silent=True, force=True)
    res = processRequest(ree)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'

    return r

def processRequest(ree):
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
        sendText1(b)
        # sendText1(b)
        prtg2()
        return b,200



  
###ส่งข้อมูลกระดิ่งไป Line###
########################

def sendText1(text1):
    # print(text)
    # print("fn2"+text)
    # print("fn2.1"+user)
    LINE_API = 'https://api.line.me/v2/bot/message/push'
    Authorization = 'Bearer bp40QhnT1ZncneOuPam5XYaIF7y5FR4Cd0HYq53rJedoE5Lxsb5cN2q4GjpLinQdqEVDqV7tG8VDnpxLo8kLAQ0u3YVGKphURTLkpVIGrzt+6fYrNt10XuxA/CuK50Za06VZ7w6eC+UckhnlqqrZiQdB04t89/1O/w1cDnyilFU=' # ใส่ ENTER_ACCESS_TOKEN เข้าไป
    headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization':Authorization
    }
    data = json.dumps({
    "to": "R37d59791a338b1c8573f1206dd7ceee8",  ##ส่ง text
    "messages":[
    ##ส่ง carousel template
    {
  "type": "template",
  "altText": "this is a carousel template",
  "template": {
      "type": "carousel",
      "columns": [
          {
            "thumbnailImageUrl": "https://i2.wp.com/dailysysadmin.com/wp-content/uploads/2018/07/Setup-a-PRTG-Monitoring-Server-from-start-to-finish-30.png?fit=730%2C350&ssl=1",
            "imageBackgroundColor": "#808080",
            "title": "Report Status PRTG: ",
            "text": text1,
            "defaultAction": {
                "type": "uri",
                "label": "View detail",
                "uri": "http://example.com/page/123"
            },
            "actions": [
                {
                    "type": "postback",
                    "label": "Open Case",
                    "data": "action=buy&itemid=111"
                },
                {
                    "type": "postback",
                    "label": "Follow",
                    "data": "action=add&itemid=111"
                },
               
            ]
          },
          
      ],
      "imageAspectRatio": "rectangle",
      "imageSize": "cover"
    }
    }
    ]
    })
    #print("ข้อมูล：",data)
    # print(text)
    r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล
    #   print(text)
    # end()
        


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5555',debug=True)



# https://bots.dialogflow.com/line/f9e7919e-b50c-47c2-a910-f282bd99adea/webhook
# https://whapi.officemate.co.th/whbell/prtg1

