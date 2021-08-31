"""
Tipe data Dictionari untuk menghubungkan antara Key dan Value
KVP = Key Value Pair
"""
kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ibu'])

print('-'*10)

data_dari_server_gojek = {
    'tanggal': '2021-08-31',
    'driver_list': [
        {'nama': 'Muhammad', 'jarak': 10},
        {'nama': 'Mufassir', 'jarak': 25},
        {'nama': 'Quran', 'jarak': 50},
    ]
}

print(data_dari_server_gojek)
print(f"Driver disekitar anda {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][1]}")

print('-'*10)
print(f"Jarak Driver Terdekat {data_dari_server_gojek['driver_list'][1]['jarak']} meter")

for a in data_dari_server_gojek['driver_list']:
    if (a['jarak'] < 30):
        print(f"Driver {a['nama']} berjarak {a['jarak']} Meter")


