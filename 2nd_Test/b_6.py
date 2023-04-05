import pandas as pd
import time

data_kasus = [
    {"Kota": "Bandung", "Jumlah_Kasus": 5300,
        "Kasus_Sembuh": 2839, "Kasus_Meninggal": 2461},
    {"Kota": "Tegal", "Jumlah_Kasus": 4910,
        "Kasus_Sembuh": 3940, "Kasus_Meninggal": 970},
    {"Kota": "Balikpapan", "Jumlah_Kasus": 1319,
        "Kasus_Sembuh": 918, "Kasus_Meninggal": 401},
    {"Kota": "Sibolga", "Jumlah_Kasus": 2319,
        "Kasus_Sembuh": 974, "Kasus_Meninggal": 1345},
    {"Kota": "Binjai", "Jumlah_Kasus": 1311,
        "Kasus_Sembuh": 521, "Kasus_Meninggal": 790},
    {"Kota": "Probolinggo", "Jumlah_Kasus": 3483,
        "Kasus_Sembuh": 3193, "Kasus_Meninggal": 238},
    {"Kota": "Depok", "Jumlah_Kasus": 1991,
        "Kasus_Sembuh": 1413, "Kasus_Meninggal": 578},
    {"Kota": "Magelang", "Jumlah_Kasus": 3381,
        "Kasus_Sembuh": 3112, "Kasus_Meninggal": 269},
    {"Kota": "Samarinda", "Jumlah_Kasus": 3991,
        "Kasus_Sembuh": 2810, "Kasus_Meninggal": 1311},
    {"Kota": "Batam", "Jumlah_Kasus": 2647,
        "Kasus_Sembuh": 2344, "Kasus_Meninggal": 303},
    {"Kota": "Medan", "Jumlah_Kasus": 4410,
        "Kasus_Sembuh": 3344, "Kasus_Meninggal": 1066}
]

provinsi = {
    "Jawa Barat": ["Bandung", "Depok"],
    "Jawa Tengah": ["Tegal", "Magelang"],
    "Sumatera Utara": ["Sibolga", "Binjai"],
    "Jawa Timur": ["Probolinggo"],
    "Kalimantan Timur": ["Balikpapan"]
}

def exercise_6_1():
    df = pd.DataFrame(data_kasus)
    df['EDA_Jumlah_Kasus'] = df['Kasus_Sembuh'] + df['Kasus_Meninggal']
    df = df[['Kota', 'Kasus_Sembuh', 'Kasus_Meninggal',
             'Jumlah_Kasus', 'EDA_Jumlah_Kasus']]
    return df

def check_prov(nama_kota):
    for key, value in provinsi.items():
        for v in value:
            if nama_kota == v:
                return(key)
            
def exercise_6_2():
    new_data = []
    for dk in data_kasus:
        nama_kota = check_prov(dk['Kota'])
        dk['Provinsi'] = nama_kota
        new_data.append(dk)
    
    return new_data

if __name__ == "__main__":
    exercise_6_q1 = exercise_6_1()

    exercise_6_q2 = exercise_6_2()
    exercise_6_q2_df = pd.DataFrame(exercise_6_q2)

    exercise_6_q3_df = exercise_6_q2_df
    exercise_6_q3_df['Persentase_Kesembuhan'] = (exercise_6_q2_df['Kasus_Sembuh'] / (exercise_6_q2_df['Kasus_Sembuh'] + exercise_6_q2_df['Kasus_Meninggal'])) * 100
    
    exercise_6_q4_df = exercise_6_q3_df
    exercise_6_q4_df = exercise_6_q4_df[exercise_6_q4_df['Provinsi'].isin(['Jawa Barat', 'Sumatera Utara'])]
    exercise_6_q4_df = exercise_6_q4_df.groupby(['Provinsi']).mean()
    exercise_6_q4_df = exercise_6_q4_df['Kasus_Sembuh']

    print(exercise_6_q1)
    print(exercise_6_q2_df)
    print(exercise_6_q3_df.sort_values(by=['Persentase_Kesembuhan'],ascending=False))
    print(exercise_6_q4_df)
    
