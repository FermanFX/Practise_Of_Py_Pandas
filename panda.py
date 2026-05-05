import pandas
import jupyterlab
# csv filesi yaratma ve okuma isi gorme
data = {
    "calisanlar": ["Ali", "Veli", "Ayse"],
    "maaslar": [5000, 6000, 7000]
}
df = pandas.DataFrame(data)
print(df)
# create csv file
df.to_csv("calisanlar.csv", index=False)
# read csv file
df_read = pandas.read_csv("calisanlar.csv")
print(df_read)