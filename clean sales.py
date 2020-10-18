import pandas as pd
file='sales.xlsx'
sales=pd.read_excel(file)

sales2=sales[5:90]

serial=sales2['statement']
debit=sales2['Unnamed: 1']
credit=sales2['Unnamed: 2']
date=sales2['Unnamed: 3']
desc=sales2['Unnamed: 4']
serial_col=[]
del sales2['statement']
del sales2['Unnamed: 1']
del sales2['Unnamed: 2']
del sales2['Unnamed: 3']
del sales2['Unnamed: 4']
del sales2['Unnamed: 5']
del sales2['Unnamed: 6']
pd.to_numeric(debit)
pd.to_numeric(credit)
pd.to_datetime(date)
sales2.insert(0,"serial",serial)
sales2.insert(1,"debit",debit)
sales2.insert(2,"credit",credit)
sales2.insert(3,"date",date)
sales2.insert(4,"desc",desc)
sales2.index=serial
sales2.to_excel('result.xlsx')
