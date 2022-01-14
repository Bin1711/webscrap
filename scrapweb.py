import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter.font as font
import html
import csv
mylist = []
# open the file in the write mode
with open('company_data.csv', 'r', encoding='UTF8') as f:
    reader = csv.reader(f)
    mylist = list(reader)
    # create the csv writer


    response = requests.get('https://trangvangvietnam.com/categories/484645/logistics-dich-vu-logistics.html')
    # print('Visited URL: {}'.format(response.url))
    # print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding="utf-8")
    # soup = BeautifulSoup(response.body, from_encoding="utf-8")

    company = soup.find_all('div', class_="boxlistings")
    # print(company)
    company_name = []
    company_image = []
    company_address = []
    company_tel = []
    company_extentsection = []
    other = []
    email = []
    web = []
    for i, j in enumerate(company):
        if i < 35:
            main_content = j.find('div', class_='noidungchinh')
    
            # name
            name = main_content.find('h2', class_='company_name')
            res_name = name.find('a')
            # result_name = res_name.text
            result_name = res_name.text #.encode("utf-8")
            mylist[i + 1][1] = result_name
    
            #image
            image = main_content.find('img')
            src = image.get('src')
            mylist[i + 1][2] = src

            #address
            address_list = main_content.find('div', class_='address_listings')
            address = address_list.find_all('p')
            result_address = address[1].text
            company_address.append(result_address)
            mylist[i + 1][3] = result_address
            #phone number
            tel = address[2].text
            company_tel.append(tel)
            mylist[i + 1][4] = tel
            #extend section
            extend = address[3].text
            mylist[i + 1][5] = extend
    
            #other
            other_thing = j.find('div', class_='textquangcao')
            others = other_thing.text 
            mylist[i + 1][6] = others


    #email
    emails = soup.find_all('div', class_='email_text')
    for i, j in enumerate(emails):
        if i < 35:
            link = j.find('a')
            href_email = link.get('href')
            mylist[i+ 1][7] = href_email
    
    #web
    webs = soup.find_all('div', class_='website_text')
    for i, j in enumerate(webs):
        if i < 35:
            link_web = j.find('a')
            href_web = link_web.get('href')  
            mylist[i + 1][8] = href_web
    f.close()

with open('scrapwebdata.csv', 'w', encoding='UTF8') as t:
    writer = csv.writer(t)
    writer.writerows(mylist)

t.close()

# df_company = pd.DataFrame(data={'name': company_name, 'image:': company_image, 'address': result_address, 'tel': company_tel, 'extendsection': company_extentsection, 'other': other, 'email': email, 'web': web})
# df_csv = df_company.to_csv('company_data.csv', index = True)