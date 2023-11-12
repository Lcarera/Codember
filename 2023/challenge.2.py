import urllib.request

url = "https://codember.dev/data/message_02.txt"
response = urllib.request.urlopen(url)
data = response.read().decode()

result = ""
accumulator = 0
for symbol in data:
    if symbol == "#":
        accumulator += 1
    elif symbol == "@":
        accumulator -= 1
    elif symbol == "*":
        accumulator *= accumulator
    elif symbol == "&":
        result += str(accumulator)

print(f"submit {result}")