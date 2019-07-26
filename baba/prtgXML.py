import json

import os
import requests



from flask import Flask

from flask import request

from flask import make_response

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

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
from flask import make_response

import xml.etree.ElementTree as parse

# Flask app should start in global layout

app = Flask(__name__)


##message from line
@app.route('/whbell/line2', methods=['POST'])
def prtg2():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    print(decoded)
    r = decoded["events"][0]['message']['text'] ##check text##
    # id=[d['replyToken'] for d in user][0]
    #print(json_line)
    s = str(r)
    
    
    ## ถ้า user พิมมาว่า hi ##
    if s == "hi":
        print("ผู้ใช้：",user)
        sendText2(user, "What do you want?")
        return "ok", 200
        

    elif s == "server":
        ##โหลด json จาก prtg
        a = "Report Server PRTG: "
        b = "Status: "

        ##server แต่ละตัว
        data1 = 'https://10.17.1.28/api/getsensordetails.json?id=5171&username=prtgadmin&password=OishiGr3!'
        response = requests.get(data1, verify=False)
        print(response.text)
        c = json.dumps(response.json())
        d = json.loads(c)
        e = (d['sensordata']['statustext'])
        f = (d['sensordata']['name'])
        g = a+" "+f
        h = b+" "+e
        # print(e)

        data2 = 'https://10.17.1.28/api/getsensordetails.json?id=2823&username=prtgadmin&password=OishiGr3!'
        response2 = requests.get(data2, verify=False)
        print(response.text)
        i = json.dumps(response2.json())
        j = json.loads(i)
        k = (j['sensordata']['statustext'])
        l = (j['sensordata']['name'])
        m = a+" "+l
        n = b+" "+k
        # print(k)

        data3 = 'https://10.17.1.28/api/getsensordetails.json?id=2883&username=prtgadmin&password=OishiGr3!'
        response3 = requests.get(data3, verify=False)
        print(response.text)
        i3 = json.dumps(response3.json())
        j3 = json.loads(i3)
        k3 = (j3['sensordata']['statustext'])
        l3 = (j3['sensordata']['name'])
        m3 = a+" "+l3
        n3 = b+" "+k3
        # print(k3)

        data4 = 'https://10.17.1.28/api/getsensordetails.json?id=2884&username=prtgadmin&password=OishiGr3!'
        response4 = requests.get(data4, verify=False)
        print(response.text)
        i4 = json.dumps(response4.json())
        j4 = json.loads(i4)
        k4 = (j4['sensordata']['statustext'])
        l4 = (j4['sensordata']['name'])
        m4 = a+" "+l4
        n4 = b+" "+k4
        # print(k4)

        data5 = 'https://10.17.1.28/api/getsensordetails.json?id=2885&username=prtgadmin&password=OishiGr3!'
        response5 = requests.get(data5, verify=False)
        print(response.text)
        i5 = json.dumps(response5.json())
        j5 = json.loads(i5)
        k5 = (j5['sensordata']['statustext'])
        l5 = (j5['sensordata']['name'])
        m5 = a+" "+l5
        n5 = b+" "+k5
        # print(k4)

        data6 = 'https://10.17.1.28/api/getsensordetails.json?id=3346&username=prtgadmin&password=OishiGr3!'
        respons6 = requests.get(data6, verify=False)
        print(response.text)
        i6 = json.dumps(respons6.json())
        j6 = json.loads(i6)
        k6 = (j6['sensordata']['statustext'])
        l6 = (j6['sensordata']['name'])
        m6 = a+" "+l6
        n6 = b+" "+k6
        # print(k4)


        ##ข้อมูล
        print("ผู้ใช้：",user)
        # a1 = [g, m, m3, m4, m5, m6]
        # a2 = [h, n, n3, n4, n5, n6]
        b1 = {g:h, m:n, m3:n3, m4:n4, m5:n5, m6:n6}
        # print(a3)
        sendText(user, b1)

    elif s == "Application":

        a = "Report Server PRTG: "
        b = "Status: "

        data1 = 'https://10.17.1.28/api/getsensordetails.json?id=3975&username=prtgadmin&password=OishiGr3!'
        response = requests.get(data1, verify=False)
        print(response.text)
        c = json.dumps(response.json())
        d = json.loads(c)
        e = (d['sensordata']['statustext'])
        f = (d['sensordata']['name'])
        g = a+" "+f
        h = b+" "+e
        # print(e)

        print("ผู้ใช้：",user)
        # a1 = [g]
        # a2 = [h]
        b1 = {g:h}
        # print(a3)
        sendText(user, b1)

        return user,200
    return 200


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
          {
            "thumbnailImageUrl": "https://pbs.twimg.com/media/D_pfHO-UcAUagH4?format=jpg&name=4096x4096",
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
                    "type": "uri",
                    "label": "Open Case",
                    "uri": "https://www.youtube.com/watch?v=fSOpiZo1BAA&list=RDLH4Y1ZUUx2g&index=32"
                },
                {
                    "type": "uri",
                    "label": "Follow",
                    "uri": "https://www.youtube.com/watch?v=fSOpiZo1BAA&list=RDLH4Y1ZUUx2g&index=32"
                },
               
            ]
          }
        )
        
    for data in msgs:
        data = json.dumps({
            "replyToken":user,
            "messages":[
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
    return 200

##message "hi"
def sendText2(user, text1):
    # print(text1)
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
      {
  "type": "template",
  "altText": "this is a confirm template",
  "template": {
    "type": "confirm",
    "actions": [
      {
        "type": "message",
        "label": "Application",
        "text":"Application"
      },
      {
        "type": "message",
        "label": "Database",
        "text":"database"
      }
    ],
    "text": "TYPE PRTG ?"
  }
}
       
      ]
      }
      )
    requests.post(LINE_API, headers=headers, data=data1)
    return 200






@app.route("/whbell/prtg1", methods=["POST"])
###กดกระดิ่ง PRTG###
##################
def processRequest1():
  ree1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
  xmldoc = parse.fromstring(ree1.content)
  # print(ree1.attrib)

  # print(xmldoc.text)
  # for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='3639']..."):
  for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/device/sensor/[status='Up']"):
    name = item.findtext('name')
    url = item.findtext('url')

    print(name)
    print(url)
    # print(item.attrib)
    pp = {name:url}
    sendText1(pp)
  return 'OK'

###ส่งข้อมูลกระดิ่งไป Line###
########################

def sendText1(text1):
    print(text1)
    # print("fn2"+text)
    # print("fn2.1"+user)
    LINE_API = 'https://api.line.me/v2/bot/message/push'
    Authorization = 'Bearer bp40QhnT1ZncneOuPam5XYaIF7y5FR4Cd0HYq53rJedoE5Lxsb5cN2q4GjpLinQdqEVDqV7tG8VDnpxLo8kLAQ0u3YVGKphURTLkpVIGrzt+6fYrNt10XuxA/CuK50Za06VZ7w6eC+UckhnlqqrZiQdB04t89/1O/w1cDnyilFU=' # ใส่ ENTER_ACCESS_TOKEN เข้าไป
    headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization':Authorization
    }
    for key1, value1 in text1.items():
      print(key1)
        
      data11 = json.dumps({
      "to": "R37d59791a338b1c8573f1206dd7ceee8",  ##ส่ง text room:R37d59791a338b1c8573f1206dd7ceee8 group:C8187f8c884345ad63a17b2b73af85f04
      "messages":[
      ##ส่ง carousel template
      {
    "type": "template",
    "altText": "this is a carousel template",
    "template": {
        "type": "carousel",
        "columns": [
            {
              "thumbnailImageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Prtg-network-monitor-logo.svg/240px-Prtg-network-monitor-logo.svg.png",
              "imageBackgroundColor": "#8B0000",
              "title":key1,
              "text": value1,
              "defaultAction": {
                  "type": "uri",
                  "label": "View detail",
                  "uri": "http://example.com/page/123"
              },
              "actions": [
                  {
                      "type": "uri",
                      "label": "Open Case",
                     "uri": "https://www.youtube.com/?gl=TH"
                  },
                  {
                      "type": "uri",
                      "label": "Follow",
                      "uri": "https://www.youtube.com/?gl=TH"
                  },
                
              ]
            },
            
        ],
        # "imageAspectRatio": "rectangle",
        # "imageSize": "cover"
      }
      }
      ]
      })
    #print("ข้อมูล：",data)
    # print(text)
      requests.post(LINE_API, headers=headers, data=data11) # ส่งข้อมูล
    #   print(text)
    # end()
    return 200
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True, threaded=True)



# ##C7042eb261106ecaa42eaacdb9ef364a4 กรุ๊ปใหญ่
# # R37d59791a338b1c8573f1206dd7ceee8 กรุ๊ปเล็ก
# from urllib.request import urlopen
# from xml.etree.ElementTree import parse

# var_url = urlopen('https://servicedesk.officemate.co.th/sdpapi/request/111?OPERATION_NAME=GET_REQUEST&TECHNICIAN_KEY=8A2D71B6-473C-4BBF-91C9-00493F31902B')
# xmldoc = parse(var_url)

# for item in xmldoc.iterfind('result'):
#     statuscode = item.findtext('message')
#     s = str(statuscode)
#     # date = item.findtext('pubDate')
#     # link = item.findtext('link')

#     print(statuscode)
#     # print(date)
#     # print(link)
#     print()
