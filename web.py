# Test 01

import requests
# sending a post request to the indicated url
req= requests.post("https://httpbin.org/anything", data ={"msg":"welcomeuser", "isadmin":1})

# print response status
# print(req.status_code, req.reason)

# print the Body
print(req.text)

#-------------------------------------------------#
# as a mobile user
