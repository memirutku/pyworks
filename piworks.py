import csv
with open('country_vaccination_stats.csv', 'r') as dosya:
    piworks = csv.reader(dosya)
    for degerler in piworks:
        for i, deger in enumerate(degerler): 
            if not deger:
                degerler[i] = '0'
        print(degerler)


