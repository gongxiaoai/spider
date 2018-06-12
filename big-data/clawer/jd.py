import re
import urllib.request


def craw(url, page):
    htmlr = urllib.request.urlopen(url).read()
    html1 = str(htmlr)
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    # print(result1)
    pat2 = '<img width="220" height="220" data-img="1" src=\"[^>]*?\">'
    imagelist = re.compile(pat2).findall(result1)
    # print(imagelist)
    x = 1
    for imageurl in imagelist:
        imagename = 'img/' + str(page) + str(x) + ".jpg"
        pat3='\//.*?\.jpg'
        imageurl=re.compile(pat3).findall(imageurl)
        imageurl="".join(imageurl)
        imageurl='http:'+imageurl
        print(imagename)
        print(imageurl)
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x += 1
            if hasattr(e, "reason"):
                x += 1
        x += 1


for i in range(1,12):
    url = "http://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
    craw(url, i)
    print(url)
#https://item.jd.com/10554712973.html#crumb-wrap
#http://effbot.org/imagingbook/