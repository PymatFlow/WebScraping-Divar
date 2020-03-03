# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:45:12 2019

@author: Kz
"""

import bs4
import requests
import re

addres = 'https://divar.ir/s/mashhad/rent-office'
page = requests.get(addres)

cc = page.content

cc1 = page.text

coup = bs4.BeautifulSoup(cc1,'html.parser')

tagg = coup.find_all("div",{"class":"browse-post-list"})

taaa = tagg[0].find_all("a",{"class":"col-xs-12 col-sm-6 col-xl-4 p-tb-large p-lr-gutter post-card"})
Rents_value = []
Deposits = []
for item in range(len(taaa)):
    tabb_title = taaa[item].find("div",{"class":"subtitle-16 post-card__title"}).text

    tabb_descr = taaa[item].find("div",{"class":"post-card__description"}).text

    index_vad = tabb_descr.find("ودیعه: ")
    index_Rents = tabb_descr.find("اجاره ماهیانه: ")
    spl_str = tabb_descr.split(" تومان")

    str_Deposits = tabb_descr[0:index_Rents-1]
    str_Rents = tabb_descr[index_Rents:]

    str_Rents = str_Rents.replace(" تومان","").replace("اجاره ماهیانه: ","")
    str_Deposits = str_Deposits.replace(" تومان","").replace("ودیعه: ","")

    Rents_value.append(str_Rents)
    Deposits.append(str_Deposits)

import pandas
df = pandas.DataFrame([Rents_value,Deposits])


