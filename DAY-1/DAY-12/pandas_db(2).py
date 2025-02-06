import pandas as pd
data={
    "name":["alice","bob","charlie","sarah"],
    "age":[28,32,29,26],
    "location":['hyd','mum','delhi','tokyo'],
    "department":["sales","IT","Human Resources","Accounts"]
}
df=pd.DataFrame(data)
df=df.set_index(['age','location','department'],inplace=True)
print(df)
