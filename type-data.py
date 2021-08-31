# tipe data skalar => tipe data sederhana
anak1 = 'Muhammad'
anak2 = 'Mufassir'
anak3 = 'Quran'

print(anak1)
print(anak2)
print(anak3)
print('-'*10)

# tipe data list/daftar/array
anak = ['Muhammad', 'Mufassir', 'Quran']
print(anak)
anak.append('Kareem')
print(anak)
print('-'*10)

# Panggil anak ke-...
print(f'Hallo {anak[1]}!')
print('-'*10)

# Panggil Semua data anak
for a in anak:
    print(f'Hallo {a}!')

print('-'*10)
# Panggil Semua anak : cara lain
for a in range (0, len(anak)):
    print(f'{a+1}. Hallo {anak[a]}!')
