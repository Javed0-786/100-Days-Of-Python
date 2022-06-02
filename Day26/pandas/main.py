import pandas

data = pandas.read_csv("weather-data.csv")
for (index, rows) in data.iterrows():
    print(rows.day)
