import requests
from fake_useragent import UserAgent
keyword = ""
keyword.replace(" ", "+")
url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword

ua = UserAgent()
headers = {"user-agent": ua.chrome}
response = requests.get(url, headers=headers, verify=False)
data = response.text
data1 = data.split("[]")
data1 = data1[0].replace("[","")
data1 = data1.replace("]","")
data1 = data1.split(",")
for i in range(1,len(data1)):
    print(data1[i])
