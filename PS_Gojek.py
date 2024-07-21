from google_play_scraper import app, reviews_all, Sort
import pandas as pd
import csv

# deklarasi variabel untuk menyimpan hasil scraping
scrapreview = reviews_all(
    'com.gojek.app',          # ID aplikasi
    lang='id',             # Bahasa ulasan (default: 'en')
    country='id',          # Negara (default: 'us')
    sort=Sort.MOST_RELEVANT, # Urutan ulasan (default: Sort.MOST_RELEVANT)
    count=1000             # Jumlah maksimum ulasan yang ingin diambil
)

# pengubahan data mentah menjadi dataframe
app_reviews_df = pd.DataFrame(scrapreview)
jumlah_ulasan, jumlah_kolom = app_reviews_df.shape

# Menyimpan ulasan dalam file format CSV
with open('ulasan_aplikasi_gojek.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])  # Menulis header kolom
    for review in scrapreview:
        writer.writerow([review['content']])  # Menulis konten ulasan ke dalam file CSV