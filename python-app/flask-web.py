import sys
import os
import logging
from flask import Flask
from flask import jsonify
from flask import request
from textblob import TextBlob

app = Flask(__name__)


@app.route(
    '/api/sentiment/query',
    methods=['POST', 'GET']
)
def query_sentiment():
    try:
        req_json = request.get_json()

        if req_json is None:

            return jsonify(
                error='this service require A JSON request'
            )
        else:
            if not ('text' in req_json):
                raise Exception('Missing mandatory paramater "text"')

        text = req_json['text']
        blob = TextBlob(text)
        sentiment = blob.sentiment

        return jsonify(
            polarity=sentiment.polarity,
            subjectivity=sentiment.subjectivity
        )

    except Exception as ex:
        app.log.error(type(ex))
        app.log.error(ex.args)
        app.log.error(ex)
        return jsonify(error=str(ex))

if __name__ == '__main__':

    LOG_FORMAT = "'%(asctime)s - %(name)s - %(levelname)s - %(message)s'"
    logging.basicConfig(
        level=logging.DEBUG,
        format=LOG_FORMAT
    )
    app.log = logging.getLogger(__name__)
    port = os.environ['FLASK_PORT']
    app.run(
        host='0.0.0.0',
        port=int(port),
        debug=False
    )
