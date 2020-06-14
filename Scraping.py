import requests
from bs4 import BeautifulSoup

url='https://www.imdb.com/chart/moviemeter/?sort=ir,desc&mode=simple&page=1'

page=requests.get(url)
#print(page.ok)  #True means requests got confirmed .. working
soup=BeautifulSoup(page.content,'html.parser')
movies=list()
title=soup.find_all('td',class_='titleColumn')
star=soup.find_all('td',class_='ratingColumn imdbRating')

for i,j in zip(title,star):
    name=i.a.text
    year=i.span.text
    rating=j.strong
    if rating==None:
        rating=''
    else:
        rating=j.strong.text
    movies.append((name,year,rating))


import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='IMDB movies'
sheet['a1']='Movie name'
sheet['b1']='Year'
sheet['c1']='Rating'
for movie in movies:
    sheet.append(movie)

wb.save('Top_Rated100.xlsx')