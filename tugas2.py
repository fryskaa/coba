import pandas as pd
df = pd.read_csv('food_delivery_datasets.csv')
print (df.head(10))
resto = df['resto_id']
print (resto)
modus = resto.mode()
print ("Restoran yang paling sering dipesan memiliki resto_id yaitu : ",modus[0])
