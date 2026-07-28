import json
import urllib.request

url = "http://py4e-data.dr-chuck.net/comments_2427467.json"

uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)

nums = list()
for item in info['comments']:
    nums.append(item['count'])
print (sum(nums))
    
