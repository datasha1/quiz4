from bs4 import BeautifulSoup
import requests
import csv
from time import sleep

i = 1
z = open("website.csv", "w", encoding='utf-8_sig', newline='\n')
write_obj = csv.writer(z)
write_obj.writerow(['ანიმეს სახელი:'])
write_obj.writerow([''])
an = []
while i <=4:
    url = "https://animetv.night-city.online/all/satavgadasavlo/" + "page/" + str(i)
    print(url)
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    anime = soup.find("body")
    animes = anime.find_all("div", class_="movie-item__label")
    an.append(soup.find_all("div", class_="movie-item__title"))
    i += 1
    sleep(4)
nam= []
for i in an[0]:
    write_obj.writerow(i)
    nam.append(i.text)
for i in an[1]:
    write_obj.writerow(i)
    nam.append(i.text)
for i in an[2]:
    write_obj.writerow(i)
    nam.append(i.text)
for i in an[3]:
    write_obj.writerow(i)
    nam.append(i.text)