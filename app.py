from flask import Flask
# added the json library to work with json formats
from flask import json
# added the logging module to handle logs for the app
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"

# added a route for the /status endpoint
@app.route("/status")
# this function should be used to run heathchecks in the app and return OK if the app is healthy
# as this is an exercise, the healthy status e basically hardcoded into the app.
def status():
    response = app.response_class(
        response = json.dumps({"result":"OK - healthy"}),
        status = 200,
        mimetype = 'application/json'
    )
    app.logger.info('Status request successfull')
    return response

#added a route for the /metrics endpoint
@app.route("/metrics")
# this function should be used to gather maetrics about the usage of the app and return their values in json format
# as this is an exercise, the metrics of User Activity are hardcodede into the app.
def metrics():
    response = app.response_class(
        response = json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status = 200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request successfull')
    return response

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0', port=8080)
