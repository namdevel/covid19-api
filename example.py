from src.corona import Covid19

ndvl = Covid19()
print(ndvl.getdata()) # data global
print(ndvl.getdata()['cases'])  # data global [cases, deats, recovered]

print(ndvl.getdata("indonesia")) # data by country
print(ndvl.getdata("indonesia")['recovered']) # data by country [cases, deats, recovered]

