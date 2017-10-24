#from bs4 import BeautifulSoup

import req
import io
link ='http://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/sunpharmaceuticalindustries/SPI'
#link ='<div class="PB10"><div class="FL gry10">zz</div>'
#page =urllib2.urlopen(link)
#page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

html = urllib3.urlopen(link)
print(html)

    #re(link).re
#re = html.read()
f = io.TextIOWrapper(html,encoding='utf-8')
#soup = BeautifulSoup(html,"html.parser")
#for div in soup.find_all('a', attrs={'class': 'stockDsl'}):
#for div in soup.find_all('a'):
# s = div.string

fo = open("c:\\Nitesh\\html.txt","w")
fo.write(mybytes)
fr = open("c:\\Nitesh\\html.txt","r")
for line in fr:
    str = line
    str = str.lstrip()
    str = str[:500]
  #  print(str)
fr = open("c:\\Nitesh\\html.txt","r")
for line in fr:
    str = line
    str = str.lstrip()
    str = str[:500]
    instr = str.find("NSE:")
    if instr>0:
        st1=str[instr:len(str)]
        sp =st1.find("<span")
        print(st1[4:sp])

#close price
found =0
count =0
fr = open("c:\\Nitesh\\html.txt","r")
for line in fr:
    str = line
    str = str.lstrip()
    str = str[:500]
    instr = str.find("best_5_box_table")

    if instr>0 and found==0:
       found =1
       print(instr)
    if found>0:
       count = count +1
       #print(count)
       #print(str)
    if count == 51:
        sp = str.find("</td>")
        print(str[4:sp])

#Open Price
found =0
found1 =0
count =0
count1 = 0
fr = open("c:\\Nitesh\\html.txt","r")
for line in fr:
    str = line
    str = str.lstrip()
    str = str[:500]
    instr = str.find("PT3 PB3 UC gL_10")
    instr1 = str.find("Today's Low/High")
    instr2 = str.find("VOLUME")
      #  print(instr)
    if instr>0:
       found = str.find("Open Price")

    if found>0:
       count = count +1

    if count == 11:
        instr = str.find("n_open")
        if instr>0:
         sp = str.find("</strong>")
         print(str[43:sp])

    if instr1>0:
        found1 = str.find("gL_10 UC PR10")

    if found1>0:
       count1 = count1 +1
    if count1 == 270:
        instr = str.find("n_low_sh")
        if instr>0:
         sp = str.find("</span>")
         print(str[32:sp])
    if count1 == 274:
        instr = str.find("n_high_sh")
        if instr > 0:
            sp = str.find("</span>")
            print(str[34:sp])
    if instr2>0:
        instr = str.find("nse_volume")
        if instr > 0:
            sp = str.find("</strong>")
            print(str[97:sp].replace(",",""))
