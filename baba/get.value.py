import json


def read_data():
    file_data ="app/data/data.json"
    file = open(file_data, 'r')
    source = file.read()
    file.close()

    y = json.loads(source)
    # Convert from JSON to Python:
    user_id = y["events"][0]["message"]["type"]
    print (user_id)


read_data()


