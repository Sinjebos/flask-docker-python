from flask import Flask, jsonify
from flask_restful import API
test=FLASK(__name__)
api= Api(test)

@app.route("/Lads")
def bye():
    #prepare a respone for the request that came to /bye
    age = 25
    #c = 1/0
    retJson = {
        "GroupName": "Lads"
        "members:[
            {
                "first_name": "Liam",
                "last_name": "Jardine"
            },
            {
                "first_name": "Jacob",
                "last_name": "Retteli"
            },
            {
                "first_name": "Niklas",
                "last_name": "Nielsen"
            },
            {
                "first_name": "Jonathan",
                "last_name": "Gerard"
            },
            {
                "first_name": "Erik",
                "last_name": "Klang"
            },
            {
                "first_name": "Jacob",
                "last_name": "Retteli"
            },
        ]
    }
    return jsonify(retJson) 