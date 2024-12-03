import os

os.system('cls')

with open('bron.txt', 'rt', encoding='utf-8') as bron_file:
    tekst = bron_file.read().strip()
with open('posities.txt', 'rt', encoding='utf-8') as posities_file:
    posities = posities_file.read().strip().split(',')
rslt = ''
for i in posities[::-1]:
    rslt += tekst[int(i)]
print('Antwoord: ' + rslt)
with open('bericht.txt', 'w', encoding='utf-8') as bericht_file:
    bericht_file.write(rslt)