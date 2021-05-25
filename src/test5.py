import os.path
import sys
import json
# opening json file
# The file holds information about a category including the products
f = open(os.path.join(sys.path[0],"data.json"))
#  data is a Python dictionary
data = json.loads(f.read())
# .read() => pass the file contents (a string) to json.loads(), not the file object itself
print (data)