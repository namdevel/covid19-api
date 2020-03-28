from src.corona import Covid19

c = Covid19()
print(c.getdata()) # data global
print(c.getdata()['cases'])  # data global [cases, deats, recovered]

print(c.getdata("indonesia")) # data by country
print(c.getdata("indonesia")['recovered']) # data by country [cases, deats, recovered]

