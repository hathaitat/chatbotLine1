from flask import Flask, request, jsonify, render_template
import requests
import os
import json


web_hook_url="https://graph.facebook.com/v2.6/me/messages?access_token=DQVJzemlHdVlSRGFjcDhCWVFpcWo2VzE3R3R2M3M3VWQzX1drLWJpcTVqZA19IWVpCaFBYSEVKbW5yeHFMdVMzSnp1QjFobWktcDJYX1M1a3RIeHplWktweEhBczdCaGVkLTVFQ2RFdnp1MzhRMFNLUjRXY29tZA1N1TjNoS3lWT0VCZAU9xVmhVekxPZAmJQUDNMdkdwUFNoeHlKRW1xT2xFVVBrZATRxWTZAtOVNxd0ZAIZAGxFZAS12ekR3SkFLM3VlaDlhRk52cjVn"
hd = {
    "content-type":"application/json"
}
#import pusher

#from flask_sslify import SSLify

app = Flask(__name__)

# sslify = SSLify(app,subdomains=True)
# EAALNyShJXH8BAOo5o88mnzJu43t8TqeBl42qGNOna3Gx1RBhPUGvBcFB6tY6RXYNH7Df68Aj6IK3KMtRw9bBiHkeD5h6X7kAAlAxgFb5fiHbp3Udhx2sY7FET8xfIbz5tiLsFynlhDGz0W30Fz4FQFcuL1KZClwZAZA3U0l4gZDZD
@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        VERIFY_TOKEN = "ga75HpoblY9qBtOKo2m8QXauNvBoKQzt" # Key for Verify Token
        hubverify = request.args.get('hub.verify_token') # Get Verify Key tokem
        hubchallenge = request.args.get('hub.challenge') # For return to Facebook must to 'CHALLENGE_ACCEPTED'
        hubmode = request.args.get('hub.mode') # Mode must to 'subscribe'
        
        if hubverify == VERIFY_TOKEN and hubmode == "subscribe": # Check data verify and mode
            print('WEBHOOK_VERIFIED')
            return hubchallenge , 200 # Return 'CHALLENGE_ACCEPTED'
        
        else:
            return 'You Wrong Something' , 200

    elif request.method == 'POST':
        data = request.get_json()
        # print(data)
        
        # print(text)
        data2 = data["entry"][0]["messaging"][0]["sender"]["id"]
        data1 = data["entry"][0]["messaging"][0]["message"]["text"]
        print(data1)
        print(data2)
        msg={"recipient":{"id":data2},"message":{"text":data1}}
        requests.post(web_hook_url, headers=hd, data=json.dumps(msg))
        
        return "post"


        
if __name__ == '__main__':
  app.run(debug=True)

    