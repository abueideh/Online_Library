from flask import Flask , request , jsonify
from flask_marshmallow import Marshmallow
import requests
import json

front = Flask(__name__)


@front.route('/search/<topic>' ,methods=['POST','GET'])
def search(topic):
    Cat_IP = '192.168.1.101:5000'
    request = 'http://' + Cat_IP + '/search/' + topic
    response = requests.get(request).content
    return jsonify(json.loads(response)) 


@front.route('/lookup/<id>' ,methods=['POST','GET'])
def lookup(id):
    Cat_IP = '192.168.1.101:5000'
    request = 'http://' + Cat_IP + '/lookup/' + id
    response = requests.get(request)
    return response.json()

@front.route('/buy/<id>' ,methods=['POST','GET'])
def get_quantity(id):
    Order_IP = '192.168.1.109:5000'
    request = 'http://' + Order_IP + '/buy/' + id
    return requests.get(request).content
    



if __name__ == "__main__":
    front.run(host='192.168.1.107')
    front.run(debug=True)
