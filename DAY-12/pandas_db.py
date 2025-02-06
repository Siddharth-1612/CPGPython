import pandas as pd
data={
    'name':['alice','bob','john'],
    'age':[25,26,28],
    'city':['new york','tokyo','mumbai']    
}
dt=pd.DataFrame(data)
df=pd.read_csv('/home/iamsid/Downloads/customers-100.csv')
df.to_json("customer.JSON",orient="records",indent=4)
df=df.sort_values(by='First Name',ascending=False)
print(df[1:5])
