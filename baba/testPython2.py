import urllib3
import json
import time

http = urllib3.PoolManager()

# GET
# result = http.request('GET',"") #ระบุmethod, GETข้อมูลจะส่งไปกับ url และ รับค่า

#POST ส่งข้อมูลไปกับ http body แต่ขะใส่ key and value
result = http.request('GET',"") #ระบุmethod, GETข้อมูลจะส่งไปกับ url และ รับค่า

