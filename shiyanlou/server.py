#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

import http.server
import json
from ocr import OCRNeuralNetwork
import numpy as np
import random

# server settings
HOST_NAME = 'localhost'
PORT_NUMBER = '8000'

# this value is the best one according to run the neural network script
HIDDEN_NODE_COUNT = 15

#loading data set
data_matrix = np.loadtxt(open('data.csv', 'rb'), delimiter = ',')
data_labels = np.loadtxt(open('dataLabels.csv', 'rb'))

#tranfer to list
data_matrix = data_matrix.tolist()
data_labels = data_labels.tolist()

#set got 5000 data. train_indice is use to save the number of training data.

train_indice = range(5000)

#random it.
random.shuffle(train_indice)

nn = OCRNeuralNetwork(HIDDEN_NODE_COUNT, data_matrix, data_labels, train_indice);

class JSONHandler(http.server.BaseHTTPRequestHandler):
    '''handler the post request recieved'''
    def do_POST(self):
        response_code = 200
        response = ""
        var_len = int(self.headers.get('Content-Length'))
        content = self.rfile.read(var_len)
        payload = json.loads(content)

        # if the requestZ is training request. train it and save the neural network after that
        if payload.get('train'):
            nn.train(payload['trainArray'])
            nn.save()
            # if the request is for predict .return the predict value.
        elif payload.get('predict'):
            try:
                print
                nn.predict(data_matrix[0])
                response = {"type": "test", "result": str(nn.predict(payload['image']))}
            except:
                response_code = 500
        else:
            response_code = 400

        self.send_response(response_code)
        self.send_header("Content-type", "application/json")
        #access-control-allow  解决浏览器自动阻止跨域问题。
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_header()
        if response:
            self.wfile.write(json.dumps(response))
        return

if __name__ == "__main__":
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), JSONHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    else:
        print("unexpected server exception occured.")
    finally:
        httpd.server_close()
