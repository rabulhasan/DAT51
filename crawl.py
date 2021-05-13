from urllib.request import urlopen
def news(url, topics):
    response = urlopen(url)
    html = response.read()
    content = html.decode().lower()
    for topic in topics:
        num = content.count(topic)    
        print("{} appears {} times".format(topic, num))
    return("")
print(news(input("enter the url: "),["মামুনুল","লকডাউন","করোনা","প্রধানমন্ত্রী"]))

