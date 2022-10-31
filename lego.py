import requests

from bs4 import BeautifulSoup

url = input()

response = requests.get(url)

print('\nlink - ',url)

# https://www.onekitprojects.com/51515/cat

content = response.content

site = BeautifulSoup(content, 'html.parser')

title_section = site.find('section', attrs={'id': 'comp-l17yovxb'})

# titulo do objeto
titulo = title_section.find('h3', attrs={'class': 'font_3'})
print('\nTitulo - ',titulo.text ,'\n')

image_section = site.find('div', attrs={'id': 'comp-l17yovxi1'})

# imagem do objeto
image = image_section.find('img', attrs={'class': 'gallery-item-visible gallery-item gallery-item-preloaded'})
image = image.get('src')
print('\nimagem - ',image,'\n')

description_section = site.find('div', attrs={'id': 'comp-l17yovxm'})

description = description_section.find('p', attrs={'class': 'font_8'})
print('\nDescrição - ',description.text,'\n')

# more paragraphs is needed

