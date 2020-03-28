#  Covid19 World Cases API
COVID-19 CORONAVIRUS PANDEMIC

Usage
---------

```python
from src.corona import Covid19

ndvl = Covid19()
print(ndvl.getdata()) # data global
# Output : {'cases': '622,888', 'deaths': '28,828', 'recovered': '137,391'}

print(ndvl.getdata()['cases'])  # data global [cases, deats, recovered]
# Output : 622,888

print(ndvl.getdata("indonesia")) # data by country
# Output : {'cases': '1,155', 'deaths': '102', 'recovered': '59'}

print(ndvl.getdata("indonesia")['recovered']) # data by country [cases, deats, recovered]
# Output : 59
```

License
------------

This open-source software is distributed under the MIT License. See LICENSE.md

Contributing
------------

All kinds of contributions are welcome - code, tests, documentation, bug reports, new features, etc...

* Send feedbacks.
* Submit bug reports.
* Write/Edit the documents.
* Fix bugs or add new features.
