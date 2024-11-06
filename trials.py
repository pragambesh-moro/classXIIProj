import datetime as dt
import json

tm = dt.datetime.now()
print(tm)

mydict = {"name": "Allen",
          "DOB": "1971-01-01",
          "ui": "XXXX"}

print(mydict)
pd = json.dumps(mydict, indent=4)
print(pd)

