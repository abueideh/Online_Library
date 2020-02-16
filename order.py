from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
import requests

order = Flask(__name__)


@order.route('/buy/<id>' ,methods=['POST','GET'])
def get_quantity(id):
    Cat_IP = '192.168.1.101:5000'
    request = 'http://' + Cat_IP + '/quantity/' + id
    quantity = int(requests.get(request).content)
    if quantity > 0:
        request = 'http://' + Cat_IP + '/update/' + id
        requests.get(request)
        return 'The book has been purchased successfully'
    else:
        return 'This book is out of stock'



if __name__ == "__main__":
    order.run(host='192.168.1.109')
    order.run(debug=True)
