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

from pymongo import MongoClient
from flask import Flask, render_template, jsonify, json, request

app = Flask(__name__)

client = MongoClient('localhost:27017')
a = client.database_names()

b = ''.join(a)
print("baran" + b)
db = client.EmployeeDB

# cheating here
# TODO
@app.route("/addEmployee", methods=['GET'])
def addEmployee():
    try:
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
        return jsonify(status='OK', message='inserted successfully')
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


@app.route("/getEmployeeList", methods=['POST'])
def getEmployeeList():
    try:
        employees = db.Employees.find()
        employee_list = []

        for employee in employees:
            print(employee)
            employeeItem = {
                'id': employee['id'],
                'name': employee['name'],
                'age': employee['age'],
                'type': employee['type']
            }
            employee_list.append(employeeItem)
    except Exception as e:
        return str(e)
    return json.dumps(employee_list)


@app.route('/')
def showEmployeeList():
    return render_template('list.html')


if __name__ == '__main__':
    app.run()
