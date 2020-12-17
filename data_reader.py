import pandas as pd
from time import sleep
def reqBuilder(pagenumber, postnumber):
    return r'https://asuntojen.hintatiedot.fi/haku/?z=%s&c=&cr=1&ps=%s&amin=&amax=&renderType=renderTypeTable&print=1&search=1&submit=Tulosta' % (pagenumber, postnumber)
data = None
empty = True
postinumerot = pd.read_csv('postinumerot_ja_vaestotiheydet.csv')
postinumero = postinumerot.values[:,1]
for postcode in postinumero:
    while(len(str(postcode)) < 5):
        postcode = "0" + str(postcode)
    i = 1
    print(postcode)

    while True:
        sleep(0.1)
        url = reqBuilder(i, postcode)
        tables = pd.read_html(url) # Returns list of all tables on page
        # print(tables[0]) # Select table of interest
        if len(tables[0]) <= 5:
            break
        tables[0]['postcode'] = postcode
        if empty:
            empty = False
            data = tables[0]
        else:
            data = pd.concat([data, tables[0]])
        i+=1
        if i>100:
            break

data.to_csv('postcode_data_copy.csv')
