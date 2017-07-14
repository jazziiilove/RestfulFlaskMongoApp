"""
 " " " " " " " " " " " " " " " " " " " " " " "
 " Assignment: RestfulFlaskMongoApp          "
 " Programmer: Baran Topal                   "
 " File name: RestfulFlaskMongo.py           "
 "                                           "
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " "
 "	                                                                                         "
 "  LICENSE: This source file is subject to have the protection of GNU General               "
 "	Public License. You can distribute the code freely but storing this license information. "
 "	Contact Baran Topal if you have any questions. barantopal@barantopal.com                 "
 "	                                                                                         "
 " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " " "
"""

# Start mongo db server as follows:
# C:\Windows\system32>"C:\Program Files\MongoDB\Server\3.4\bin\mongod.exe" --dbpath C:\Users\Baran.Topal\Documents\mongodb_data
# data to be inserted
"""
        db.Employees.insert_one({
  "Personnels": {
    "Employee": [
      {
        "Id": "3674",
        "type": "permanent",
        "Age": "34",
        "Name": "Seagull"
      },
      {
        "Id": "3675",
        "type": "contract",
        "Age": "25",
        "Name": "Robin"
      },
      {
        "Id": "3676",
        "type": "permanent",
        "Age": "28",
        "Name": "Crow"
      }
    ]
  }
})
"""

from pymongo import MongoClient
from flask import Flask, render_template, jsonify, json, request
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)

client = MongoClient('localhost:27017')
a = client.database_names()

b = ''.join(a)
print("DB info: " + b)
db = client.EmployeeDB


@app.route("/addEmployee", methods=['POST'])
def addEmployee():
    try:

        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        type = request.form['type']

        post_data = {
            'id': id,
            'name': name,
            'age': age,
            'type': type
        }
        result = db.Employees.insert_one(post_data)

        return jsonify(status='OK', message='inserted successfully')
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))
        # return json.dumps({'status': 'OK', 'id': id, 'name': name, 'age': age, 'type':type})


@app.route("/getEmployeeList", methods=['GET'])
def getEmployeeList():
    try:
        col = db.Employees
        array = list(col.find())
        print(array)

        return json.dumps(JSONEncoder().encode(array))

    except Exception as e:
        print("err" + e)
        return str(e)


@app.route('/')
def showEmployeeList():
    return render_template('list.html')


if __name__ == '__main__':
    app.run()
