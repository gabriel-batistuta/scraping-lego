import requests

from bs4 import BeautifulSoup

print('\nPor favor digite uma url de um objeto lego que está no domínio: onekitprojects.com\n')

url = input()

response = requests.get(url)

print('\nlink do objeto - ',url)

# https://www.onekitprojects.com/51515/cat

content = response.content

site = BeautifulSoup(content, 'html.parser')

title_section = site.find('section', attrs={'id': 'comp-l17yovxb'})

# titulo do objeto
titulo = title_section.find('h3', attrs={'class': 'font_3'})
print('\nTitulo do objeto - ',titulo.text ,'\n')

image_section = site.find('div', attrs={'id': 'comp-l17yovxi1'})

# imagem do objeto
image = image_section.find('img', attrs={'class': 'gallery-item-visible gallery-item gallery-item-preloaded'})
image = image.get('src')
print('imagem do objeto - ',image,'\n')

description_section = site.find('div', attrs={'id': 'comp-l17yovxm'})

description = description_section.find('p', attrs={'class': 'font_8'})
print('Descrição do objeto - ',description.text,'\n')

# more paragraphs is needed

