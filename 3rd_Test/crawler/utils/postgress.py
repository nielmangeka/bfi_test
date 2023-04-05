import psycopg2
import pandas as pd
from psycopg2.extensions import AsIs

class PostgresUtils():
    def upload_to_db(self, etle_data):
        connection = psycopg2.connect(user="bfi_user",
                                      password="bfi",
                                      host="localhost",
                                      port="5432",
                                      database="bfi")
        cursor = connection.cursor()

        query_check_table = '''
        SELECT EXISTS(SELECT * FROM information_schema.tables 
              WHERE table_catalog='bfi' AND 
                    table_name='scrap_etle');
        '''

        query_create_table = '''
        CREATE TABLE scrap_etle (
            plat_kendaraan VARCHAR(255) PRIMARY KEY,
            mesin_kendaraan VARCHAR ( 255 ),
            rangka_kendaraan VARCHAR ( 255 ),
            location VARCHAR ( 255 ),
            penalty VARCHAR ( 500 ),
            nominal float,
            capture_date TIMESTAMP,
            created_date TIMESTAMP
        );

        '''
        cursor.execute(query_check_table)

        for check in cursor.fetchone():
            if check is not True:
                cursor.execute(query_create_table)
                connection.commit()
                print('Selesai create table')

        query_insert_data = """
            INSERT INTO scrap_etle(
                plat_kendaraan,
                mesin_kendaraan,
                rangka_kendaraan,
                location,
                penalty,
                nominal,
                capture_date,
                created_date
                )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """
        record_to_insert = tuple(etle_data.values())
        cursor.execute(query_insert_data, record_to_insert)
        connection.commit()