import pymongo
import pprint
import pandas as pd 
pd.set_option("display.max_rows", None, "display.max_columns", None)
from measurement.utils import guess
pp = pprint.PrettyPrinter(indent=4)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Meds"]
mycol = mydb["drugsv1"]

x1 = mycol.find({"name": "Nyracta"})
dataframeList = []

for x in x1:
    
    #pp.pprint(x)
    rows_list = []
    ingr = x['ingredients']

    #pp.pprint(ingr)
    total = 0
    for key in ingr:
        value = ingr[key]
        if len(value) == 0:
            continue
        for i in value:
            try:
                d = {}
                r = i.split("Vikt:")
                #print(r)
                rr = r[1].strip().split()
                unit = rr[1].strip()
                v = float(rr[0])
                # print(r[0] + "\t \t", end= " ")
                # print(guess(v,unit).mg)
                d['name_of_ingredient'] = r[0]
                d['value_in_mg'] = guess(v,unit).mg
                rows_list.append(d)
                total = total + guess(v,unit).mg
                
            except:
                continue
    df = pd.DataFrame(rows_list)
    dataframeList.append(df)


print(pd.concat(dataframeList, axis=1).drop_duplicates(subset= "name_of_ingredient"))