
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
import xmltodict
import xml.etree.ElementTree as ET

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
    
    a = "Report Server PRTG: "
    b = "Status: "

    
    
    if s == "Open Case":
        print("ผู้ใช้：",user)
        # def open1(text10) :
        #     print(text10)
        #     for k, v in text10.items():
        #         url = 'https://servicedesk.officemate.co.th/sdpapi/request?OPERATION_NAME=ADD_REQUEST&TECHNICIAN_KEY=8A2D71B6-473C-4BBF-91C9-00493F31902B&INPUT_DATA=<Operation><Details><requester>PRTG</requester><subject>'+str(k)+' Status: Down</subject><description>'+str(v)+'</description><priority>Hight</priority><level>Tier 2</level><requesttemplate>Default Request</requesttemplate><impact>Affects Business</impact><urgency>Hight</urgency></Details></Operation>'
        #         headers = {
        #             'Content-Type': 'application/xml; charset=UTF-8',
        #             }  
        #         p = requests.post(url, headers=headers)
        #         print(p.text)

    ###app###
    elif s == "2492":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device[@id='3638']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device[@id='3640']"):
          dname2 = item.findtext('name')
          did2 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device[@id='3962']"):
          dname3 = item.findtext('name')
          did3 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device[@id='3963']"):
          dname4 = item.findtext('name')
          did4 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device[@id='3964']"):
          dname5 = item.findtext('name')
          did5 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device[@id='5075']"):
          dname6 = item.findtext('name')
          did6 = item.findtext('id')
          b1 = {dname1:did1, dname2:did2, dname3:did3, dname4:did4, dname5:did5, dname6:did6}
          sendText3(user, b1)
    ##device1 app###
    elif s == "3638":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='3639']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5372']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5373']"):  
                name3 = ("OS  Serial Number 508cbc42")
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5374']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            
    
            # print(name1)
            # print(tags)
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4}
                sendText(user, b1)
    ##device2 app###
    elif s == "3640":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='3641']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5375']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5376']"):  
                name3 = ("OS  Serial Number 508cbc42")
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5377']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            

                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4}
                sendText(user, b1)
    ##device3 app###
    elif s == "3962":
                g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
                xmldoc = parse.fromstring(g1.content)

                for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='3965']"):
                    name1 = item.findtext('name')
                    tags = item.findtext('status')
                for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5368']"):  
                    name2 = item.findtext('name')
                    tags2 = item.findtext('status')
                for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5369']"):  
                    name3 = item.findtext('name')
                    tags3 = item.findtext('status')
                for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5370']"):  
                    name4 = item.findtext('name')
                    tags4 = item.findtext('status')
                

                    b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4}
                    sendText(user, b1)
    ##device4 app###
    elif s == "3963":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='3966']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4117']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4141']"):  
                name3 = item.findtext('name')
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4327']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            
            # print(name1)
            # print(tags)
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4}
                sendText(user, b1)
    ##device5 app###
    elif s == "3964":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='3967']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4138']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4139']"):  
                name3 = item.findtext('name')
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4140']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4}
                sendText(user, b1)
    ##device6 app###
    elif s == "5075":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5076']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5077']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            
                b1 = {name1:tags, name2:tags2}
                sendText(user, b1)

    ###network###
    elif s == "2811":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='2491']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='2478']"):
          dname2 = item.findtext('name')
          did2 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='2477']"):
          dname3 = item.findtext('name')
          did3 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='2476']"):
          dname4 = item.findtext('name')
          did4 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='2475']"):
          dname5 = item.findtext('name')
          did5 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='5331']"):
          dname6 = item.findtext('name')
          did6 = item.findtext('id')
          b1 = {dname1:did1, dname2:did2, dname3:did3, dname4:did4, dname5:did5, dname6:did6}
          sendText3(user, b1)
    ###sensor g1 net###
    elif s == "2491":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2676']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5154']"):  
                name2 = ("(016)Switch-to-TrueRouter")
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5155']"):  
                name3 = ("(018)Switch-to-InterlinkRouter")
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5304']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4}
                sendText(user, b1)
    ###sensor g2 net###
    elif s == "2478":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/group/device/sensor[@id='4039']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/group/device/sensor[@id='4021']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/group/device/sensor[@id='4025']"):  
                name3 = item.findtext('name')
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/group/device/sensor[@id='4023']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4}
                sendText(user, b1)
    ###sensor g3 net###
    elif s == "2477":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/group/device/sensor[@id='4887']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/group/device/sensor[@id='4910']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/group/device/sensor[@id='4923']"):  
                name3 = item.findtext('name')
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/group/device/sensor[@id='5209']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/group/device/sensor[@id='5211']"):  
                name5 = item.findtext('name')
                tags5 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/group/device/sensor[@id='5213']"):  
                name6 = item.findtext('name')
                tags6 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/group/device/sensor[@id='5215']"):  
                name7 = item.findtext('name')
                tags7 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/group/device/sensor[@id='5217']"):  
                name8 = item.findtext('name')
                tags8 = item.findtext('status')
            
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4, name5:tags5, name6:tags6, name7:tags7, name8:tags8}
                sendText(user, b1)
    ###sensor g4 net ไม่ครบ###
    elif s == "2476":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/device/sensor[@id='2647']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/device/sensor[@id='2662']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/device/sensor[@id='2663']"):  
                name3 = item.findtext('name')
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/device/sensor[@id='2765']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/device/sensor[@id='2766']"):  
                name5 = item.findtext('name')
                tags5 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/device/sensor[@id='2776']"):  
                name6 = item.findtext('name')
                tags6 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/device/sensor[@id='2777']"):  
                name7 = item.findtext('name')
                tags7 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/group/device/sensor[@id='2801']"):  
                name8 = item.findtext('name')
                tags8 = item.findtext('status')
            
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4, name5:tags5, name6:tags6, name7:tags7, name8:tags8}
                sendText(user, b1)
    ###sensor g5 netไม่ครบ###
    elif s == "2475":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2728']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2729']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2788']"):  
                name3 = item.findtext('name')
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2789']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4414']"):  
                name5 = item.findtext('name')
                tags5 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4416']"):  
                name6 = item.findtext('name')
                tags6 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4419']"):  
                name7 = item.findtext('name')
                tags7 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4421']"):  
                name8 = item.findtext('name')
                tags8 = item.findtext('status')
            
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4, name5:tags5, name6:tags6, name7:tags7, name8:tags8}
                sendText(user, b1)
    ###sensor g6** net###
    elif s == "5331":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5333']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5335']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5337']"):  
                name3 = item.findtext('name')
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5339']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5341']"):  
                name5 = item.findtext('name')
                tags5 = item.findtext('status')
            
            
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4, name5:tags5}
                sendText(user, b1)

    ###server###
    elif s == "2823":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='2883']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='2884']"):
          dname2 = item.findtext('name')
          did2 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='2885']"):
          dname3 = item.findtext('name')
          did3 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='3346']"):
          dname4 = item.findtext('name')
          did4 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='4130']"):
          dname5 = item.findtext('name')
          did5 = item.findtext('id')
        

          b1 = {dname1:did1, dname2:did2, dname3:did3, dname4:did4, dname5:did5}
          sendText3(user, b1)
    ###sensor g1 server###
    elif s == "2883":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2856']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4481']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4868']"):  
                name3 = item.findtext('url')
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4869']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4870']"):
                name5 = item.findtext('name')
                tags5 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4871']"):  
                name6 = item.findtext('name')
                tags6 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5029']"):  
                name7 = item.findtext('url')
                tags7 = item.findtext('status')
            
            
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4, name5:tags5, name6:tags6, name7:tags7}
                sendText(user, b1)
    ###sensor g2 server###
    elif s == "2884":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4940']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4952']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4955']"):  
                name3 = ("Label: Serial Number ec4bcd73")
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4956']"):  
                name4 = ("Label: Serial Number 78efb1ed")
                tags4 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4957']"):
                name5 = item.findtext('name')
                tags5 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4962']"):  
                name6 = item.findtext('name')
                tags6 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4963']"):  
                name7 = item.findtext('url')
                tags7 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4968']"):  
                name8 = item.findtext('name')
                tags8 = item.findtext('status')
            
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4, name5:tags5, name6:tags6, name7:tags7, name8:tags8}
                sendText(user, b1)
    ###sensor g3 server###
    elif s == "2885":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2844']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2845']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2846']"):  
                name3 = item.findtext('name')
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2847']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2843']"):  
                name5 = item.findtext('name')
                tags5 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='3233']"):  
                name6 = item.findtext('name')
                tags6 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2899']"):  
                name7 = item.findtext('name')
                tags7 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='2900']"):  
                name8 = item.findtext('name')
                tags8 = item.findtext('status')
            
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4, name5:tags5, name6:tags6, name7:tags7, name8:tags8}
                sendText(user, b1)
    ###sensor g4 server###
    elif s == "3346":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='3348']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='3350']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='3351']"):  
                name3 = item.findtext('url')
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='3352']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4513']"):  
                name5 = item.findtext('name')
                tags5 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4846']"):  
                name6 = item.findtext('name')
                tags6 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4848']"):  
                name7 = item.findtext('name')
                tags7 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='4981']"):  
                name8 = item.findtext('name')
                tags8 = item.findtext('status')
            
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4, name5:tags5, name6:tags6, name7:tags7, name8:tags8}
                sendText(user, b1)
    
    ###User AD-Admin home###
    elif s == "4095":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group[@id='4095']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('id')
        
          b1 = {dname1:did1}
          sendText(user, b1)
   
    ###chayaphol phunpung home###
    elif s == "4104":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group[@id='4104']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('id')
        
          b1 = {dname1:did1}
          sendText(user, b1)
   
    ###Other sensors###
    elif s == "4863":
        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/device/sensor[@id='5092']"):
            name1 = item.findtext('name')
            tags = item.findtext('status')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/device/sensor[@id='5093']"):  
            name2 = item.findtext('name')
            tags2 = item.findtext('status')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/device/sensor[@id='5094']"):  
            name3 = item.findtext('name')
            tags3 = item.findtext('status')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/device/sensor[@id='5113']"):  
            name4 = item.findtext('name')
            tags4 = item.findtext('status')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/device/sensor[@id='5116']"):  
            name5 = item.findtext('name')
            tags5 = item.findtext('status')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/device/sensor[@id='5117']"):  
            name6 = item.findtext('name')
            tags6 = item.findtext('status')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/device/sensor[@id='5125']"):  
            name8 = item.findtext('name')
            tags8 = item.findtext('status')
            
        b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4, name5:tags5, name6:tags6, name8:tags8}
        sendText(user, b1)

    ###Application Read home###
    elif s == "4883":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group[@id='4883']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('id')
        
          b1 = {dname1:did1}
          sendText(user, b1)
        
    ###Sensor for IT-Operation###
    elif s == "5078":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group[@id='5078']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('id')
        
          b1 = {dname1:did1}
          sendText(user, b1)

    ###BITM home###
    elif s == "5080":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group[@id='5080']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('id')
        
          b1 = {dname1:did1}
          sendText(user, b1)

    ###DBM home###
    elif s == "5083":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group[@id='5083']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('id')
        
          b1 = {dname1:did1}
          sendText(user, b1)

    ###Development home###
    elif s == "5086":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group[@id='5086']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('id')
        
          b1 = {dname1:did1}
          sendText(user, b1)    

    ###IT Support all location home###
    elif s == "5107":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group[@id='5107']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('id')
        
          b1 = {dname1:did1}
          sendText(user, b1)

    ###Franchise Group home###
    elif s == "5296":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group[@id='5296']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('active')
        
          b1 = {dname1:did1}
          sendText(user, b1)

    ###Murata System###
    elif s == "5486":

        g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
        xmldoc = parse.fromstring(g1.content)
        # print(ree1.attrib)

        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='5487']"):
          dname1 = item.findtext('name')
          did1 = item.findtext('id')
        for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group[@id='5488']"):
          dname2 = item.findtext('name')
          did2 = item.findtext('id')
        
          b1 = {dname1:did1, dname2:did2}
          sendText3(user, b1)
    ##device1 Murata###
    elif s == "5487":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5490']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5491']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5492']"):  
                name3 = ("OS  Serial Number 66bf4ec2")
                tags3 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5493']"):  
                name4 = item.findtext('name')
                tags4 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5495']"):  
                name5 = item.findtext('name')
                tags5 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5506']"):  
                name6 = item.findtext('name')
                tags6 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5508']"):  
                name7 = item.findtext('name')
                tags7 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5510']"):  
                name8 = item.findtext('name')
                tags8 = item.findtext('status')
    
            # print(name1)
            # print(tags)
                b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4, name5:tags5, name6:tags6, name7:tags7, name8:tags8}
                sendText(user, b1)
    ##device1 Murata###
    elif s == "5488":
            g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
            xmldoc = parse.fromstring(g1.content)

            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5528']"):
                name1 = item.findtext('name')
                tags = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5530']"):  
                name2 = item.findtext('name')
                tags2 = item.findtext('status')
            for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5532']"):  
                name3 = item.findtext('name')
                tags3 = item.findtext('status')
            # for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5533']"):  
            #     name4 = item.findtext('name')
            #     tags4 = item.findtext('status')
            # for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5536']"):  
            #     name5 = item.findtext('name')
            #     tags5 = item.findtext('status')
            # for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5538']"):  
            #     name6 = item.findtext('name')
            #     tags6 = item.findtext('status')
            # for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5540']"):  
            #     name7 = item.findtext('name')
            #     tags7 = item.findtext('status')
            # for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/group/device/sensor[@id='5557']"):  
            #     name8 = item.findtext('name')
            #     tags8 = item.findtext('status')
    
            # print(name1)
            # print(tags)
                # b1 = {name1:tags, name2:tags2, name3:tags3, name4:tags4, name5:tags5, name6:tags6, name7:tags7, name8:tags8}
                b1 = {name1:tags, name2:tags2, name3:tags3}
                sendText(user, b1)

    ### message status###
    elif s == "status" or "Status" or "Hello":
      g1 = requests.get('https://10.17.1.28/api/table.xml?content=sensortree&username=prtgadmin&password=OishiGr3!',  verify=False)
      xmldoc = parse.fromstring(g1.content)
      for item in xmldoc.findall("./sensortree/nodes/group/probenode/group"):
          name1 = item.findtext(str('name'))
          id11 = item.findtext(str('id'))

          tt1 = {name1:id11}
          sendText2(user, tt1)
          # # print(tt1.content)
        #   print()
          
    
    
    
    
    
    return user,200
    
###ส่ง แต่ละ "device" ของ group ใหญ่###
#####################################
def sendText3(user, text):
    print(text)    
    
    
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer ym5ACrqHsZvCdxdhwtHvbQtr8SMLjU/Tzwbxv3Fa2c28RXWaOXU7/4adYdDsrXe9qEVDqV7tG8VDnpxLo8kLAQ0u3YVGKphURTLkpVIGrzuMqUIRbwyCu3YNMQTB4M+VlBppsxbQDQa+hPmLaRI0CAdB04t89/1O/w1cDnyilFU=' 
    headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization':Authorization
    }
    msgs = []
    for key3, value3 in text.items():
        msgs.append(
          {
            # "thumbnailImageUrl": "https://hlassets.paessler.com/common/files/preview/logo-prtg.png",
            # "imageBackgroundColor": "#808080",
            # "title": key3,
            "text": key3,
            "defaultAction": {
                "type": "uri",
                "label": "value1",
                "uri": "http://example.com/page/123"
            },
            "actions": [
        {
        "type": "message",
        "label": "CHECK SENSORS",
        "text": value3
      },{
        "type": "message",
        "label": "EXIT",
        "text": "status"
      }
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


###status "sensor"  ของ device###
#################################
def sendText(user, text):
    print(text)    
    
    
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer ym5ACrqHsZvCdxdhwtHvbQtr8SMLjU/Tzwbxv3Fa2c28RXWaOXU7/4adYdDsrXe9qEVDqV7tG8VDnpxLo8kLAQ0u3YVGKphURTLkpVIGrzuMqUIRbwyCu3YNMQTB4M+VlBppsxbQDQa+hPmLaRI0CAdB04t89/1O/w1cDnyilFU=' 
    headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization':Authorization
    }
    msgs = []
    for key2, value2 in text.items():
        msgs.append(
          {
            # "thumbnailImageUrl": "https://hlassets.paessler.com/common/files/preview/logo-prtg.png",
            # "imageBackgroundColor": "#808080",
            "title": key2,
            "text": value2,
            "defaultAction": {
                "type": "uri",
                "label": "value1",
                "uri": "http://example.com/page/123"
            },
            "actions": [
        {
        "type": "message",
        "label": "EXIT",
        "text": "status"
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


## message "status"####
#######################
def sendText2(user, text1):
    # print(text1)   

    aaa = ({"thumbnailImageUrl": "https://pbs.twimg.com/media/EASiXowU4AEX_W6?format=jpg&name=4096x4096","title": "Application","text": "id: 2492","actions": [{"type": "message","label": "DETAIL","text": "2492"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASjO5-U8AAavSf?format=jpg&name=4096x4096","title": "Network","text": "id: 2811","actions": [{"type": "message","label": "DETAIL","text": "2811"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASjeFcVUAEt_Wq?format=jpg&name=4096x4096","title": "Server","text": "id: 2823","actions": [{"type": "message","label": "DETAIL","text": "2823"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASkdgQU0AA4Syl?format=jpg&name=4096x4096","title": "User AD-Admin home","text": "id: 4095","actions": [{"type": "message","label": "DETAIL","text": "4095"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASkdgSUcAE11s9?format=jpg&name=4096x4096","title": "chayaphol phunpung home","text": "id: 4104","actions": [{"type": "message","label": "DETAIL","text": "4104"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASkdgPUEAIbb9n?format=jpg&name=4096x4096","title": "Other sensors","text": "id: 4863","actions": [{"type": "message","label": "DETAIL","text": "4863"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASkdkYU4AIKbbF?format=jpg&name=4096x4096","title": "Application Read home","text": "4883","actions": [{"type": "message","label": "DETAIL","text": "4883"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASkeboUYAABVxb?format=jpg&name=4096x4096","title": "Sensor for IT-Operation","text": "5078","actions": [{"type": "message","label": "DETAIL","text": "5078"}]},
       
        )
    bbb = (
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASkeeCU0AAEja5?format=jpg&name=4096x4096","title": "BITM home","text": "id: 5080","actions": [{"type": "message","label": "DETAIL","text": "5080"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASkefAVUAAE1jB?format=jpg&name=4096x4096","title": "DBM home","text": "id: 5083","actions": [{"type": "message","label": "DETAIL","text": "5083"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASkeihUIAAWThU?format=jpg&name=4096x4096","title": "Development home","text": "id: 5086","actions": [{"type": "message","label": "DETAIL","text": "5086"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASkfLNUcAMu-ll?format=jpg&name=4096x4096","title": "IT Support all location home","text": "id: 5107","actions": [{"type": "message","label": "DETAIL","text": "5107"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASkfTsVUAEd7AJ?format=jpg&name=4096x4096","title": "Franchise Group home","text": "id: 5296","actions": [{"type": "message","label": "DETAIL","text": "5296"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASkfNoU8AAQI_H?format=jpg&name=4096x4096","title": "Murata System","text": "id: 5486","actions": [{"type": "message","label": "DETAIL","text": "5486"}]},
        {"thumbnailImageUrl": "https://pbs.twimg.com/media/EASkfULVUAIEDdY?format=jpg&name=4096x4096","title": "Franchise","text": "id: 5486","actions": [{"type": "message","label": "DETAIL","text": "5486"}]},

        )
    
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
                "columns": aaa
            }
                },{
            "type": "template",
            "altText": "this is a carousel template",
            "template": {
                "type": "carousel",
                "columns": bbb
            }
                }
                        ]
                    }
                    )
   

        
    requests.post(LINE_API, headers=headers, data=data)
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
#   for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/device/sensor/[status='Down (Acknowledged)']"):
  for item in xmldoc.findall("./sensortree/nodes/group/probenode/group/device/sensor/[status='Up']"):

    name = item.findtext('name')
    id = item.findtext('id')

    print(name)
    print(id)
    # print(item.attrib)
    pp = {name:id}
    sendText1(pp)
    # open1(pp)
    

    #send to service desk###
    ########################
    url = 'https://servicedesk.officemate.co.th/sdpapi/request?OPERATION_NAME=ADD_REQUEST&TECHNICIAN_KEY=8A2D71B6-473C-4BBF-91C9-00493F31902B&INPUT_DATA=<Operation><Details><requester>PRTG</requester><subject>'+str(id)+' Status: Down</subject><description>'+str(name)+' has problems</description><priority>Hight</priority><level>Tier 2</level><requesttemplate>Default Request</requesttemplate><impact>Affects Business</impact><urgency>Hight</urgency></Details></Operation>'
    headers = {
            'Content-Type': 'application/xml; charset=UTF-8',
            }  
    p = requests.post(url, headers=headers)
    print(p.text)
    # print(.text)
    return 'OK'

  return 'OK'

###ส่งข้อมูลกระดิ่งไป Line###
########################
def sendText1(text1):
    # print(text)
    # print("fn2"+text)
    # print("fn2.1"+user)

    LINE_API = 'https://api.line.me/v2/bot/message/push'
    Authorization = 'Bearer ym5ACrqHsZvCdxdhwtHvbQtr8SMLjU/Tzwbxv3Fa2c28RXWaOXU7/4adYdDsrXe9qEVDqV7tG8VDnpxLo8kLAQ0u3YVGKphURTLkpVIGrzuMqUIRbwyCu3YNMQTB4M+VlBppsxbQDQa+hPmLaRI0CAdB04t89/1O/w1cDnyilFU=' # ใส่ ENTER_ACCESS_TOKEN เข้าไป
    headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization':Authorization
    }
    for key1, value1 in text1.items():
        
      data = json.dumps({
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
              "thumbnailImageUrl": "https://hlassets.paessler.com/common/files/preview/logo-prtg.png",
              "imageBackgroundColor": "#808080",
              "title":key1,
              "text": value1,
              "defaultAction": {
                  "type": "uri",
                  "label": "View detail",
                  "uri": "http://example.com/page/123"
              },
              "actions": [
                  {
                     "type": "message",
                     "label": "Open Case",
                     "text": "Open Case"
                  },
                  {
                      "type": "message",
                      "label": "Open Case",
                      "text": "Open Case"
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
      requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล
    #   print(text)
    # end()
    return 200
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True, threaded=True)
 