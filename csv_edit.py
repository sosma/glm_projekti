import pandas as pd

df = pd.read_csv('postcode_data_copy.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.loc[:, ~df.columns.str.contains('^Energial')]
df = df.loc[:, ~df.columns.str.contains('^Energial')]
df = df.loc[:, ~df.columns.str.contains('^Kaupungin')]
df = df.loc[:, ~df.columns.str.contains('^Huoneisto')]
df.dropna(subset = ['m2 '], inplace=True)
df = df[df['m2 '] != df['€/m2 ']]
df = df.reset_index()
df = df.loc[:, ~df.columns.str.contains('^index')]
postinumerot = pd.read_csv('postinumerot_ja_vaestotiheydet.csv')
postinumerot['vaestontiheys'] = postinumerot['Asukkaat yhteens�, 2017 (HE)']/postinumerot['Postinumeroalueen pinta-ala']
df = df.merge(postinumerot)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
print(df)
df.to_csv('postcode_data.csv')
