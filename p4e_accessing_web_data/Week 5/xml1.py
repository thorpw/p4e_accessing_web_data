import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    url = input('Enter URL: ')
    if len(url) < 1: break
    print('Retrieving', url)

    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    # print(data.decode())
    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment')

    listy = []
    counter = 0
    for item in lst:
        newnum = lst[counter].find('count').text
        counter  += 1
        listy.append(int(newnum))

    print(sum(listy))
