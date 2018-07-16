import urllib.request, urllib.parse, urllib.error
import json

while True:
    url = input('Enter url: ')
    if len(url) < 1: break

    uh = urllib.request.urlopen(url)
    data = uh.read()
    decode_data = data.decode()
    info = json.loads(decode_data)

    listy = []
    counter = 0
    info = info['comments']

    for item in info:
        listy.append(int(info[counter]["count"]))
        counter += 1

    print(sum(listy))
