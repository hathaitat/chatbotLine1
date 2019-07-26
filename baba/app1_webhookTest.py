import json

import os




from flask import Flask

from flask import request

from flask import make_response

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

# Flask app should start in global layout

app = Flask(__name__)



@app.route('/whbell/webhook1', methods=['POST'])

def webhook():



    req = request.get_json(silent=True, force=True)

    res = processRequest(req)

    res = json.dumps(res, indent=4)

    r = make_response(res)

    r.headers['Content-Type'] = 'application/json'

    return r



def processRequest(req):

    # Parsing the POST request body into a dictionary for easy access.

    req_dict = json.loads(request.data)

    print(req_dict)
    print(req_dict["responseId"])
    print(req_dict['originalDetectIntentRequest']["payload"]["data"]["replyToken"])
    print(req_dict['originalDetectIntentRequest']["payload"]["data"]["source"])

    



    # Accessing the fields on the POST request boduy of API.ai invocation of the webhook

    intent = req_dict["queryResult"]["intent"]["displayName"]


    if intent == 'hello':

        speech = "มีไรให้ช่วยยย"
        # speech = efLine.py
        
    else:

        speech = "ผมไม่เข้าใจ คุณต้องการอะไร จริงหรอ"
       
    res = makeWebhookResult(speech)
    
    return res

def makeWebhookResult(speech):

    return {

  "fulfillmentText": speech

    }



if __name__ == '__main__':

    # port = int(os.getenv('PORT', 5000))



    # print("Starting app on port %d" % port)



    app.run(debug=False, host='0.0.0.0', threaded=True)