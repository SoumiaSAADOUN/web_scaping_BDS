import os.path
import sys
import json
import logging
import csv

# opening json file
# The file holds information about a category including the products
f = open(os.path.join(sys.path[0],"data.json"))
data = json.loads(f.read()) # data is a Python dictionary
# .read() => pass the file contents (a string) to json.loads(), not the file object itself

availableProds = open("src/available.csv","w",encoding="utf8", newline='') #file to save the available products
hasHeader =False
for i in data ["Bundles"]:
    if (("Products" in i) and (i["Products"] )):
        if (('Name' in i["Products"][0])):
            productInfos= i["Products"][0]
        else:
            productInfos= i["Products"][1]   
        try:
            prodName= productInfos['Name'][0:30]
            if (productInfos['IsAvailable']):
                price= round(productInfos['Price'], 1)
                if (os.stat("src/available.csv").st_size == 0 and not hasHeader) :
                    writer = csv.DictWriter(availableProds, productInfos.keys())
                    writer.writeheader()
                    hasHeader =True
                writer.writerow(productInfos)
                print ("You can buy {} at our store at {} ".format(prodName,price))
            else:
                prodId= productInfos['Barcode']
                print ("Product unavailable: {} {}".format(prodName,prodId))
        except Exception:
                logging.exception("Error occured: A clue of the product’s availability can’t be found")             
           
availableProds.close()