from bs4 import BeautifulSoup

soup = BeautifulSoup(open("MWSU_schedule_classes.html"), features="lxml")

#print(soup.prettify())

final_link = soup.p.a
final_link.decompose()

trs = soup.find_all('tr')
for tr in trs:
    print(tr)
    
links = soup.find_all('a')

for link in links:
    names = link.contents[0]
    fullLink = link.get('href')
    print(names)
    print(fullLink)