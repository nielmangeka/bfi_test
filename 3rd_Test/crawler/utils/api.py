import requests
import json
from datetime import datetime

class EtleApi:

    def etle_data(self) -> dict:
        plat_kendaraan = 'A1492RH'
        mesin_kendaraan = '4A91GD9541'
        rangka_kendaraan = 'MK2NCWHANJJ018193'
        endpoint = f'https://api.etlebanten.info:8443/public/violation/check-vehicle-data?plate-number={plat_kendaraan}&machine-number={mesin_kendaraan}&skeleton-number={rangka_kendaraan}'

        req = requests.get(endpoint)
        if req.status_code == 200:
            etle_data = json.loads(req.text)
            for ed in etle_data['data']:

                if ed['violation']['checkpoint']['location']:
                    location = ed['violation']['checkpoint']['location']
                else :
                    location = None
                
                if ed['violation']['penalty']:
                    penalty = ed['violation']['penalty']['typeID']
                    nominal = ed['violation']['penalty']['nominal']
                else :
                    penalty = None
                
                capture_date = int(ed['violation']['captureDate'])
                capture_date = datetime.fromtimestamp(capture_date / 1000.0).strftime('%Y-%m-%d')
                
                created_date = int(ed['createdAt'])
                created_date = datetime.fromtimestamp(created_date / 1000.0).strftime('%Y-%m-%d')

                clean_data = {
                    'plat_kendaraan' : plat_kendaraan,
                    'mesin_kendaraan' : mesin_kendaraan,
                    'rangka_kendaraan' : rangka_kendaraan,
                    'location': location,
                    'penalty' : penalty,
                    'nominal' : nominal,
                    'capture_date' : capture_date,
                    'created_date' : created_date
                }
                
                if not clean_data:
                    print('No Data')
                else:
                    return clean_data