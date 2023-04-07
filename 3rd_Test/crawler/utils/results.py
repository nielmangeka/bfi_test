from flask import Flask


class RestAPI():
    def etle_endpoint(self,etle_api_util):
        app = Flask(__name__)

        @app.get('/etle_data')
        def list_programming_languages():
            return {"data": list(etle_api_util.values())}

        app.run(host='127.0.0.1', port=5000)
