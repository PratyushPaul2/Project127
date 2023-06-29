from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("C:/Users/prita/OneDrive/Desktop/PRO-C127-Student-Boilerplate-Code-main/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

stars_data = []
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )
        soup=BeautifulSoup(browser.page_source,'html.parser')
        for ul_tag in soup.find_all('ul',attrs={'class','wikitable sortable jquery-tablesorter'}):
            li_tags=ul_tag.find_all('li')
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append('')
            
            stars_data.append(temp_list)
        



        
# Calling Method    
scrape()

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
planet_df_1=pd.DataFrame(planets_data,columns=headers)

# Convert to CSV
planet_df_1.to_csv('Scraped_Data.csv',index=True,index_label='id')

    


