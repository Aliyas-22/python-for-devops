import requests 

url =  "https://dummy-json.mock.beeceptor.com/todos"

response=requests.get(url=url)
#print(response.json())
for item in response.json():
    for key,value in item.items():
        if key == "title":
           print(f"{key} : {value}")


        data = response.json()
        with open("output1.txt", "w") as f:
                for item in data:
                    if  "title" in item:
                        f.write(f"title: {item['title']}\n")
