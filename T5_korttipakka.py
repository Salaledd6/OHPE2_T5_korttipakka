import random

korttipakka = set()
maat = ['Pata', 'Hertta', 'Risti', 'Ruutu']
varit = ['Musta', 'Punainen']

for i in range(4):
    for j in range(13):
        korttipakka.add( (maat[i], j+1, varit[i%2]))

kortti = korttipakka.pop()
print("Arvottu kortti on: ", kortti)