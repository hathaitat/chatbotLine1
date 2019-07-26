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
        sendText1(user,"What do you want?")
        return "", 200
        # speech = "มีไรให้ช่วยยย"

    elif s == "server":

    ##โหลด json จาก prtg
        a = "Report Server PRTG: "
        b = "Status: "

        data1 = 'https://10.17.1.28/api/getsensordetails.json?id=5171&username=prtgadmin&password=OishiGr3!'
        response = requests.get(data1, verify=False)
        print(response.text)
        c = json.dumps(response.json())
        d = json.loads(c)
        e = (d['sensordata']['statustext'])
        f = (d['sensordata']['name'])
        g = a+" "+f
        h = b+" "+e
        print(e)

        data2 = 'https://10.17.1.28/api/getsensordetails.json?id=2823&username=prtgadmin&password=OishiGr3!'
        response2 = requests.get(data2, verify=False)
        print(response.text)
        i = json.dumps(response2.json())
        j = json.loads(i)
        k = (j['sensordata']['statustext'])
        l = (j['sensordata']['name'])
        m = a+" "+l
        n = b+" "+k
        print(k)

        data3 = 'https://10.17.1.28/api/getsensordetails.json?id=2883&username=prtgadmin&password=OishiGr3!'
        response3 = requests.get(data3, verify=False)
        print(response.text)
        i3 = json.dumps(response3.json())
        j3 = json.loads(i3)
        k3 = (j3['sensordata']['statustext'])
        l3 = (j3['sensordata']['name'])
        m3 = a+" "+l3
        n3 = b+" "+k3
        print(k3)


        ##กำหนดข้อมูล
        print("ผู้ใช้：",user)

        # sendText(user,k3)
        # ss(k3)
        # sendText1(user,g)

        a1 = [g, m, m3]
        a2 = [h, n, n3]
        a3 = {g:h, m:n, m3:n3}
        # print(a3)
        sendText(user, a3)

        return user,200



###ตอบข้อความไปไลน์ prtg2()###
#############################
def sendText(user, text):
    print(text)    
    
    
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer ym5ACrqHsZvCdxdhwtHvbQtr8SMLjU/Tzwbxv3Fa2c28RXWaOXU7/4adYdDsrXe9qEVDqV7tG8VDnpxLo8kLAQ0u3YVGKphURTLkpVIGrzuMqUIRbwyCu3YNMQTB4M+VlBppsxbQDQa+hPmLaRI0CAdB04t89/1O/w1cDnyilFU=' 
    headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization':Authorization
    }
    msgs = []
    for key, value in text.items():
        msgs.append(
        #     {
        #     "type":"text",
        #     "text":text1,
        # }
#         {
#             "type": "template",
#   "altText": "this is a carousel template",
#   "template": {
#       "type": "carousel",
#       "columns": [
          {
            "thumbnailImageUrl": "https://hlassets.paessler.com/common/files/preview/logo-prtg.png",
            "imageBackgroundColor": "#808080",
            "title": key,
            "text": value,
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
          
    #   ]
    # }
    # }
        
        )
    for data in msgs:
        data = json.dumps({
            "replyToken":user,
            "messages":[
    ##ส่ง carousel template
    {
  "type": "template",
  "altText": "this is a carousel template",
  "template": {
      "type": "carousel",
      "columns": msgs
  }
    }
            ]
            # "messages":msgs
        }
        )
    
    requests.post(LINE_API, headers=headers, data=data)
    return 

def sendText1(user, text1):
    print(text1)
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer ym5ACrqHsZvCdxdhwtHvbQtr8SMLjU/Tzwbxv3Fa2c28RXWaOXU7/4adYdDsrXe9qEVDqV7tG8VDnpxLo8kLAQ0u3YVGKphURTLkpVIGrzuMqUIRbwyCu3YNMQTB4M+VlBppsxbQDQa+hPmLaRI0CAdB04t89/1O/w1cDnyilFU=' 
    headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization':Authorization
    }
    data1 = json.dumps({
  "replyToken":user,
  "messages":[
      {"type":"text","text":text1},
       
      ]
      }
      )
    r = requests.post(LINE_API, headers=headers, data=data1)







    # for val in range(len(text)):
    #     # print("index is %d and va is %s" % (val))

    #     data = json.dumps({
    #     "replyToken":user,
    #     "messages":[
    #         {"type":"text","text":text[val]},
    #         {
    #         "id": "325708",
    #         "type": "sticker",
    #         "packageId": "1",
    #         "stickerId": "1"
    #             }
    #         ]
    #         }
    #         )
        
        
    #     # print(user)
    #     print(data)
    #     # val += 1
        
        
        
        
    #     # return user
    #     r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล
    #     # val += 1
    #     # return val
    #     print(r.text)
    # return user
        
    
        



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)



# https://bots.dialogflow.com/line/f9e7919e-b50c-47c2-a910-f282bd99adea/webhook
# https://whapi.officemate.co.th/whbell/prtg1

