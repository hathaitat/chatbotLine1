import json

# some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x: ,parse การวิเคราะห์คำ
# y = json.loads(x) #load วิเคราะห์
# z = json.dumps(x) #dump แปลง string ให้เป็น json

# the result is a Python dictionary: แสดงผล
# print(y["age"])x 
# print(z)


    ###indent,sort_keys###
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x, indent=1, separators = (". ", " = "),
# sort_keys=True))
#inden คือการจัดบรรทัด , sort_keys เรียงลำดับข้อความ


    ###research word###
# import re

# str = "The rain in Spain"

# # x = re.findall("rain", str)
# # print(x)

# # if (x):
# #   print("Yes, there is at least one match!")
# # else:
# #   print("No match")

# #or
# x = re.search("Portugal", str)
# print(x)



