from flask import Flask


class RestAPI():
    def etle_endpoint(self,etle_api_util):
        app = Flask(__name__)

        # etle_data = {'plat_kendaraan': 'A1492RH', 'mesin_kendaraan': '4A91GD9541', 'rangka_kendaraan': 'MK2NCWHANJJ018193', 'location': 'Jalan Veteran Kota Serang',
        #              'penalty': 'Tidak menggunakan sabuk pengaman', 'nominal': 0.0, 'capture_date': '2021-09-29', 'created_date': '2023-04-06'}

        @app.get('/etle_data')
        def list_programming_languages():
            return {"data": list(etle_api_util.values())}

        @app.route('/programming_languages/<programming_language_name>')
        def get_programming_language(programming_language_name):
            return etle_api_util[programming_language_name]

        app.run(host='127.0.0.1', port=5000)
