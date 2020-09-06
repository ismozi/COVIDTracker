from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import requests
import time

#C:\Users\Ismaël Zirek\Downloads\chromedriver_win32
my_url = 'https://www.inspq.qc.ca/covid-19/donnees'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}

driver = webdriver.Chrome('/Users/Ismaël Zirek/Downloads/chromedriver_win32/chromedriver')
driver.get(my_url)

# Give the javascript time to render
time.sleep(1)

# starts the connection, grab the page
#page = requests.get(my_url, headers=headers)
#page_html = page.text


# stops the connection
#page.close

# html parsing
page_soup = soup(driver.page_source)

# creates the csv file and headers
filename = "products.csv"
f = open(filename, "w")
headers = "brand, title, prev_price, live_price, product_link\n"
f.write(headers)

# grabs each number

nbCas = page_soup.find("span", {"id": "cas"}).text
nbDeces = page_soup.find("span", {"id": "deces"}).text
nbHospi = page_soup.find("span", {"id": "hospit"}).text
nbSoin = page_soup.find("span", {"id": "soins"}).text
nbGueri = page_soup.find("span", {"id": "gueris"}).text

print("Nombre de cas: "+str(nbCas)+"\n"+"Nombre de décès: "+str(nbDeces)+"\n"+"Nombre d'hospitalisations:"+str(nbHospi)+"\n"+"Nombre soins intensifs:"+str(nbSoin)+"\n"+"Nombre de guéri: "+str(nbGueri))



# closes the file
f.close()
