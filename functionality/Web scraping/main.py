from selenium import webdriver
import time
import pandas as pd
import matplotlib.pyplot as plt
import os

PATH = os.path.join(os.getcwd(), 'chromedriver.exe') #"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

habilidades = ['Soft skills',
               'React',
                'Java',
               'C++',
               'Python']
websites = ["https://www.zonajobs.com.ar/"]
contador_de_ofertas = [0] * len(habilidades)
xpaths_por_website = [['//*[@id="query"]',
                       '//*[@id="search-form"]/button',
                       '//*[@id="listado"]/div[1]/div[2]/div[4]/div[2]/h1/strong',
                       '// *[ @ id = "navbar-zonajobs"] / div[1] / button[1] / i']]

for website,xpaths in zip(websites,xpaths_por_website):
    driver.get(website)
    time.sleep(3)
    for i,palabra_clave in enumerate(habilidades):
        driver.find_element_by_xpath(xpaths[0])\
            .send_keys(palabra_clave)
        driver.find_element_by_xpath(xpaths[1])\
            .click()
        time.sleep(1)
        numero_de_ofertas = int(driver.find_element_by_xpath(xpaths[2])\
            .text.replace('.', ''))
        contador_de_ofertas[i] = contador_de_ofertas[i] + numero_de_ofertas
        print(contador_de_ofertas)
        driver.find_element_by_xpath(xpaths[3]) \
            .click()
        time.sleep(1)

df = pd.DataFrame({'Habilidades':habilidades, 'Ofertas':contador_de_ofertas})
ax = df.plot.bar(x='Habilidades', y='Ofertas', rot=0)
plt.savefig('CantidadDeOfertas.png')

time.sleep(3)

driver.quit()