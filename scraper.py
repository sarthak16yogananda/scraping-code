import bs4 as bs
import lxml
import urllib.request
import os 
import csv
href=[]
table=[]
url=urllib.request.urlopen('https://karki23.github.io/Weather-Data/assignment.html').read()
source=bs.BeautifulSoup(url,'lxml')
for a in source.find_all('a'):
    href.append(a.get('href'))
for html in href:
    assignment='https://karki23.github.io/Weather-Data/'
    location=assignment+html
    url1=urllib.request.urlopen(location).read()
    source1=bs.BeautifulSoup(url1,'lxml')
    td=source1.find_all('table')
    th=source1.find_all('th')
    thd=[a.text for a in th]
    for row in td:
        tr=row.find_all('tr')
        for data in tr:
            td=data.find_all('td')
            rd=[a.text for a in td]
            table.append(rd)
    with open ("weatherdata.csv",'w') as writefile:
        writer=csv.writer(writefile)
        writer.writerow(thd)
        
    with open("weatherdata.csv",'a') as writefile:
        for j in table:
            writer=csv.writer(writefile)
            writer.writerow(j)
