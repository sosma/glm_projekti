import pandas as pd
df = pd.read_csv('paavo_9_koko.csv', sep =";")
# print(df.columns)
df['Postinumeroalue'] = df['Postinumeroalue'].apply(lambda s: s[0:5])
df.to_csv('postinumerot_ja_vaestotiheydet.csv')
