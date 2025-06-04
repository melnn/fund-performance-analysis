# %%
import pandas as pd

data = pd.read_csv("\001\data\1.ay.csv")

sayisal_kolonlar = ['1 Ay (%)', '3 Ay (%)', '6 Ay (%)', 'Yılbaşı (%)', '1 Yıl (%)', '3 Yıl (%)', '5 Yıl (%)']
for kolon in sayisal_kolonlar:
    data[kolon] = (
        data[kolon]
        .astype(str)
        .str.replace('.', '', regex=False)       # Tüm noktaları (binlik) kaldır
        .str.replace(',', '.', regex=False)      # Virgül → nokta (ondalık için)
        .replace('-', None)                      # "-" → None
        .astype(float)                           # Float'a çevir
    )

data.head()

# %%
print(data.dtypes)

# %%
print(data[sayisal_kolonlar].describe())

# %%
import matplotlib.pyplot as plt

ortalama_getiriler = data[sayisal_kolonlar].mean()

plt.figure(figsize=(8, 5))
plt.plot(ortalama_getiriler.index, ortalama_getiriler.values)
plt.title("Zaman Dilimlerine Göre Ortalama Fon Getirileri")
plt.ylabel("Ortalama Getiri (%)")
plt.savefig("/001/outputs/grafik1.png")
plt.show()

# %%
data['Ortalama Getiri'] = data[sayisal_kolonlar].mean(axis=1)
data['Volatilite'] = data[sayisal_kolonlar].std(axis=1)

plt.figure(figsize=(8, 6))
plt.scatter(data['Volatilite'], data['Ortalama Getiri'], alpha=0.6)
plt.xlabel("Getiri Dalgalanması (Standart Sapma)")
plt.ylabel("Ortalama Getiri (%)")
plt.title("Risk - Getiri İlişkisi (Tüm Fonlar)")
plt.savefig("001/outputs/grafik2.png")
plt.show()


