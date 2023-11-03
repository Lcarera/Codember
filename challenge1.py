
import urllib.request

url = "https://codember.dev/data/message_01.txt"
response = urllib.request.urlopen(url)
data = response.read().decode()
result = {}
for word in data[:-1].split(" "):
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

submit = ""
for key, value in result.items():
    submit += key + value.__str__()

print("submit " + submit)