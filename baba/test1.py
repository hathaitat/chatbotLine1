import json
text={
  "object": "page",
  "entry": [
   {
    "id": "293281931540823",
    "time": 1553589482913,
    "messaging": [
     {
      "sender": {
       "id": "100027991697049",
       "community": {
        "id": "166389563870112"
       }
      },
      "recipient": {
       "id": "293281931540823"
      },
      "timestamp": 1553589482588,
      "message": {
       "mid": "sgWn7FYpGE_YRDMd58eeJTlIwIkkKF-uzPbE9lmKp7XVQrCF0uOPtUPyll_OE5aNq-7cJC4cVyawcvVvIktA-A",
       "seq": 119272,
       "text": "haha"
      }
     }
    ]
   }
  ]
 }

data = text["entry"][0]["messaging"][0]["sender"]["id"]
print(data)

data1 = text["entry"][0]["messaging"][0]["message"]["text"]
print(data1)