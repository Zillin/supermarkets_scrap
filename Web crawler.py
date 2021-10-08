# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:35:41 2021

@author: Zi Lin

Press Ctrl+Shift+I to inspect the website before scrapping
"""

import os
os.chdir("C:/Users/林梓/Downloads")
import requests as re
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://www.treffpunkt-detaillisten.ch/laeden/"
page = re.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="wlyapp")
#print(results.prettify())
laeden = results.find_all("div", class_="store__results__item")

response = {"listItemHtml":"<div class=\"store__results__item\">\n    <div class=\"row\">\n        <div class=\"col s12 xl3 m4\">\n            <div class=\"store__image\">\n                <a href=\"https:\/\/www.treffpunkt-detaillisten.ch\/laeden\/pfisters-molki\/\"\n                   title=\"Pfister\u2019s Molki\">\n                                                    <img src=\"https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/30f3997f-IMG_2434_75_57.jpg\" data-src=\"https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/30f3997f-IMG_2434_560_406.jpg\"\n                         srcset=\"https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/30f3997f-IMG_2434_560_406.jpg 560w,\n                                      https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/30f3997f-IMG_2434_160_120.jpg 160w,\n                                      https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/30f3997f-IMG_2434_200_150.jpg 200w,\n                                      https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/30f3997f-IMG_2434_290_218.jpg 290w,\n                                      https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/30f3997f-IMG_2434_248_186.jpg 248w,\n                                      https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/30f3997f-IMG_2434_275_207.jpg 275w\"\n                         sizes=\"(max-width: 600px) 560px,\n                                (max-width: 767px) 160px,\n                                (max-width: 992px) 200px,\n                                (max-width: 1199px) 290px,\n                                (max-width: 1310px) 248px,\n                                (min-width: 1311px) 275px\"\n                         class=\"lazyload\"\n                            alt=\"Fritz + Marianne Pfister\"\n                            title=\"Fritz + Marianne Pfister\">\n                                    <div class=\"store__owner\">\n                        Pfister\u2019s Molki\n                    <\/div>\n                <\/a>\n            <\/div>\n        <\/div>\n        <div class=\"col xl3 m8 l4 s12 offset-xl1\">\n            <div class=\"store__adress\">\n                <p class=\"title is-2\"><strong>Fritz + Marianne Pfister<\/strong><\/p>\n                <p>Gantrischstr. 1<br \/>\n3052 Zollikofen<\/p>\n\n                            <\/div>\n        <\/div>\n\n        <div class=\"col xl3 m8 l4 s12\">\n            <div class=\"store__opening-hour\">\n\n                <div class=\"store__opening-hour__content\">\n                                                                    <p><strong>heutige \u00d6ffnungszeiten<\/strong><\/p>\n                        <ul>\n                                                    <li>07:30 - 12:15<\/li>\n                                                            <li>14:30 - 18:30<\/li>\n                                                        <\/ul>\n                                                            <\/div>\n\n                                    <div class=\"store__services\">\n                                                                        <div class=\"store__icon\">\n                                <svg width=\"25\" height=\"30\" viewBox=\"0 0 25 30\" xmlns=\"http:\/\/www.w3.org\/2000\/svg\"><path d=\"M24.055 25.933L22.337 6.589a.827.827 0 00-.822-.755h-3.533A5.931 5.931 0 0012.055 0 5.931 5.931 0 006.13 5.834H2.595a.822.822 0 00-.822.755L.055 25.933c0 .024-.006.049-.006.073C.05 28.21 2.067 30 4.552 30h15.006c2.485 0 4.503-1.791 4.503-3.994 0-.024 0-.049-.006-.073zm-12-24.277a4.274 4.274 0 014.27 4.178h-8.54a4.274 4.274 0 014.27-4.178zm7.503 26.688H4.552c-1.558 0-2.822-1.031-2.846-2.301L3.35 7.497h2.773v2.515c0 .46.368.828.828.828.46 0 .828-.368.828-.828V7.497h8.546v2.515c0 .46.368.828.828.828.46 0 .829-.368.829-.828V7.497h2.773l1.65 18.546c-.025 1.27-1.295 2.3-2.847 2.3z\" fill=\"#171817\" fill-rule=\"nonzero\"\/><\/svg>\n                                <div class=\"store__icon__description\">\n                                    Pickup                                <\/div>\n                            <\/div>\n                                                                                                <div class=\"store__icon\">\n                                <svg width=\"45\" height=\"30\" viewBox=\"0 0 45 30\" xmlns=\"http:\/\/www.w3.org\/2000\/svg\"><path d=\"M36.224 21.935a4.106 4.106 0 00-2.887 1.183c-.776.77-1.21 1.774-1.21 2.85 0 1.075.425 2.079 1.21 2.85A4.122 4.122 0 0036.224 30a4.033 4.033 0 000-8.065zm0 6.273c-1.245 0-2.292-1.022-2.292-2.24 0-1.219 1.047-2.24 2.292-2.24a2.23 2.23 0 012.22 2.24 2.23 2.23 0 01-2.22 2.24zM37.27 8.504a.88.88 0 00-.604-.233h-4.628a.902.902 0 00-.903.896v7.347c0 .493.406.896.903.896h7.344a.902.902 0 00.902-.896v-4.919a.894.894 0 00-.298-.663L37.27 8.504zm1.21 7.114h-5.54v-5.564h3.374l2.165 1.935v3.63zm-24.288 6.317a4.106 4.106 0 00-2.887 1.183c-.776.77-1.21 1.774-1.21 2.85 0 1.075.425 2.079 1.21 2.85A4.122 4.122 0 0014.192 30a4.033 4.033 0 000-8.065zm0 6.273c-1.245 0-2.292-1.022-2.292-2.24 0-1.219 1.047-2.24 2.292-2.24a2.23 2.23 0 012.22 2.24 2.23 2.23 0 01-2.22 2.24zm-6.018-5.17H6.361v-2.384a.902.902 0 00-1.805 0v3.28c0 .493.406.896.902.896h2.716a.902.902 0 00.902-.896.902.902 0 00-.902-.896zm4.574-4.884a.902.902 0 00-.902-.896H.902a.902.902 0 00-.902.896c0 .493.406.896.902.896h10.944a.896.896 0 00.902-.896zM2.734 14.92l10.944.063a.908.908 0 00.91-.887.89.89 0 00-.892-.905l-10.944-.063h-.01a.894.894 0 00-.901.887.89.89 0 00.893.905zm1.84-4.068h10.944a.902.902 0 00.902-.896.902.902 0 00-.902-.896H4.574a.902.902 0 00-.902.896c0 .493.406.896.902.896zm39.4-1.21l-6.46-5.313a.892.892 0 00-.577-.206H29.34V.896A.902.902 0 0028.438 0H5.458a.902.902 0 00-.902.896v6.56a.902.902 0 001.805 0V1.791h21.184v21.246h-7.399a.902.902 0 00-.902.896c0 .493.406.896.902.896h11.016a.902.902 0 00.903-.896.902.902 0 00-.903-.896H29.35V5.914h7.272l5.882 4.839-.063 12.267h-.938a.902.902 0 00-.902.896c0 .493.406.896.902.896h1.831a.894.894 0 00.903-.887l.072-13.584a.944.944 0 00-.334-.7z\" fill=\"#171817\" fill-rule=\"nonzero\"\/><\/svg>\n                                <div class=\"store__icon__description\">\n                                    Heimlieferung                                <\/div>\n                            <\/div>\n                                                                <\/div>\n                            <\/div>\n        <\/div>\n        <div class=\"col xl2 l12 s12 m8 offset-l0 offset-m4\">\n            <div class=\"store__detail-link\">\n                <a href=\"https:\/\/www.treffpunkt-detaillisten.ch\/laeden\/pfisters-molki\/\"\n                           class=\"button--arrow\"\n                           title=\"Zum Laden Pfister\u2019s Molki\">\n                        Zum Laden                    <svg width=\"20\" height=\"15\" viewBox=\"0 0 20 15\" xmlns=\"http:\/\/www.w3.org\/2000\/svg\"><path d=\"M13.468.211a.706.706 0 00-1.008 0 .711.711 0 000 .998l5.11 5.111H.707A.702.702 0 000 7.026a.71.71 0 00.706.716H17.57l-5.111 5.101a.724.724 0 000 1.008.706.706 0 001.008 0l6.32-6.32a.694.694 0 000-.998L13.469.21z\" fill=\"#171817\" fill-rule=\"nonzero\"\/><\/svg>\n                <\/a>\n            <\/div>\n        <\/div>\n    <\/div>\n<\/div><div class=\"store__results__item\">\n    <div class=\"row\">\n        <div class=\"col s12 xl3 m4\">\n            <div class=\"store__image\">\n                <a href=\"https:\/\/www.treffpunkt-detaillisten.ch\/laeden\/baeckerei-konditorei-lebensmittel-zumholz\/\"\n                   title=\"B\u00e4ckerei-Konditorei-Lebensmittel Zumholz\">\n                                                    <img src=\"https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/dc0ff257-IMG_2453_75_57.jpg\" data-src=\"https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/dc0ff257-IMG_2453_560_406.jpg\"\n                         srcset=\"https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/dc0ff257-IMG_2453_560_406.jpg 560w,\n                                      https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/dc0ff257-IMG_2453_160_120.jpg 160w,\n                                      https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/dc0ff257-IMG_2453_200_150.jpg 200w,\n                                      https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/dc0ff257-IMG_2453_290_218.jpg 290w,\n                                      https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/dc0ff257-IMG_2453_248_186.jpg 248w,\n                                      https:\/\/www.treffpunkt-detaillisten.ch\/app\/uploads\/fly\/dc0ff257-IMG_2453_275_207.jpg 275w\"\n                         sizes=\"(max-width: 600px) 560px,\n                                (max-width: 767px) 160px,\n                                (max-width: 992px) 200px,\n                                (max-width: 1199px) 290px,\n                                (max-width: 1310px) 248px,\n                                (min-width: 1311px) 275px\"\n                         class=\"lazyload\"\n                            alt=\"Markus und Maria Zosso\"\n                            title=\"Markus und Maria Zosso\">\n                                    <div class=\"store__owner\">\n                        B\u00e4ckerei-Konditorei-Lebensmittel Zumholz\n                    <\/div>\n                <\/a>\n            <\/div>\n        <\/div>\n        <div class=\"col xl3 m8 l4 s12 offset-xl1\">\n            <div class=\"store__adress\">\n                <p class=\"title is-2\"><strong>Markus und Maria Zosso<\/strong><\/p>\n                <p>Eggersmatt 32<br \/>\n1719 Zumholz<\/p>\n\n                            <\/div>\n        <\/div>\n\n        <div class=\"col xl3 m8 l4 s12\">\n            <div class=\"store__opening-hour\">\n\n                <div class=\"store__opening-hour__content\">\n                                                                    <p><strong>heutige \u00d6ffnungszeiten<\/strong><\/p>\n                        <ul>\n                                                    <li>06:00 - 12:00<\/li>\n                                                            <li>14:00 - 18:00<\/li>\n                                                        <\/ul>\n                                                            <\/div>\n\n                                    <div class=\"store__services\">\n                                                                        <div class=\"store__icon\">\n                                <svg width=\"25\" height=\"30\" viewBox=\"0 0 25 30\" xmlns=\"http:\/\/www.w3.org\/2000\/svg\"><path d=\"M24.055 25.933L22.337 6.589a.827.827 0 00-.822-.755h-3.533A5.931 5.931 0 0012.055 0 5.931 5.931 0 006.13 5.834H2.595a.822.822 0 00-.822.755L.055 25.933c0 .024-.006.049-.006.073C.05 28.21 2.067 30 4.552 30h15.006c2.485 0 4.503-1.791 4.503-3.994 0-.024 0-.049-.006-.073zm-12-24.277a4.274 4.274 0 014.27 4.178h-8.54a4.274 4.274 0 014.27-4.178zm7.503 26.688H4.552c-1.558 0-2.822-1.031-2.846-2.301L3.35 7.497h2.773v2.515c0 .46.368.828.828.828.46 0 .828-.368.828-.828V7.497h8.546v2.515c0 .46.368.828.828.828.46 0 .829-.368.829-.828V7.497h2.773l1.65 18.546c-.025 1.27-1.295 2.3-2.847 2.3z\" fill=\"#171817\" fill-rule=\"nonzero\"\/><\/svg>\n                                <div class=\"store__icon__description\">\n                                    Pickup                                <\/div>\n                            <\/div>\n                                                                <\/div>\n                            <\/div>\n        <\/div>\n        <div class=\"col xl2 l12 s12 m8 offset-l0 offset-m4\">\n            <div class=\"store__detail-link\">\n                <a href=\"https:\/\/www.treffpunkt-detaillisten.ch\/laeden\/baeckerei-konditorei-lebensmittel-zumholz\/\"\n                           class=\"button--arrow\"\n                           title=\"Zum Laden B\u00e4ckerei-Konditorei-Lebensmittel Zumholz\">\n                        Zum Laden                    <svg width=\"20\" height=\"15\" viewBox=\"0 0 20 15\" xmlns=\"http:\/\/www.w3.org\/2000\/svg\"><path d=\"M13.468.211a.706.706 0 00-1.008 0 .711.711 0 000 .998l5.11 5.111H.707A.702.702 0 000 7.026a.71.71 0 00.706.716H17.57l-5.111 5.101a.724.724 0 000 1.008.706.706 0 001.008 0l6.32-6.32a.694.694 0 000-.998L13.469.21z\" fill=\"#171817\" fill-rule=\"nonzero\"\/><\/svg>\n                <\/a>\n            <\/div>\n        <\/div>\n    <\/div>\n<\/div>","newLimit":60}
response = list(response.values())[0]
s1 = BeautifulSoup(response, "html.parser")
laeden = s1.find_all("div",class_="store__results__item")

df=pd.DataFrame(columns=["Name","Website","Contact","Adress","Opening hours","Angebot","Email"])
for laden in laeden:
    Name = laden.find("div", class_="store__image").text.strip()
    website = laden.find("div", class_="store__image").find("a").attrs["href"]
    laden_page = re.get(website)
    laden_soup = BeautifulSoup(laden_page.content, "html.parser")
    laden_results = laden_soup.find(id="wlyapp")
    contact = laden_results.find("div", class_="store-detail__contact").find_all("a")[1]["href"]
    adress = laden_results.find("div", class_="store-detail__adress").text.strip()
    open_hours = laden_results.find("div", class_="store-detail__opening-times").find('table').text.strip()
    angebot = laden_results.find("div", class_="store-detail__offer").find('table').text.strip()
    email = laden_results.find("div", class_="store-detail__links").find_all("a")[0]["href"]
    temp_df = pd.Series(data=[Name,website,contact,adress,open_hours,angebot,email],
                        index=["Name","Website","Contact","Adress","Opening hours","Angebot","Email"],
                        name=Name)
    df = df.append(temp_df)

df.to_excel("Treffpunkt list.xlsx")

# Volg https://www.volg.ch/standorte-oeffnungszeiten/detail/volg-vrin/
# All Volg stores: https://www.profital.ch/de/fl/72147-volg-filialen

df=pd.DataFrame(columns=["Name","Postleitzahl","Address","url"])
for i in range (1,11):#41
    URL = "https://www.profital.ch/de/fl/72147-volg-filialen?page={}".format(i)
    page = re.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="main")
    laeden = results.find("ul", class_="list-store").find_all("li")
    laeden_list = list(range(len(laeden)))
    del laeden_list [3]
    try:
        for x in laeden_list:
            laden = laeden[x]
            affix = laden.find("a").attrs["href"]
            website = "https://www.profital.ch"+affix
            laden_page = re.get(website)
            laden_soup = BeautifulSoup(laden_page.content, "html.parser")
            laden_results = laden_soup.find(id="main")
            address = laden_results.find("h1", class_="title-figure").text.strip()
            temp_str = address.split(", ")[1]
            plz = temp_str.split(" ")[0]
            temp_str = temp_str[5:]
            url = "https://www.volg.ch/standorte-oeffnungszeiten/detail/volg-"+temp_str
            temp_df = pd.Series(data=[temp_str,plz,address,url],
                        index=["Name","Postleitzahl","Address","url"],
                        name=temp_str)
            df = df.append(temp_df)
            df = df.drop_duplicates(subset=['Address'],ignore_index=True)
    except Exception as e:
        print("[E]: failed to get url:", i, e)
    df = df.append(df)
    df = df.drop_duplicates(subset=['Address'],ignore_index=True)

df = df.drop_duplicates(subset=['Address'],ignore_index=True)
df.to_excel("Volg 1-10.xlsx")

# VOI https://www.voi-migrospartner.ch/de-CH/filialen#id
# Find preview of all stores in dev tool and copy paste to a txt file

data = pd.read_fwf("voi.txt", encoding='utf-8')
name_list = list(data.loc[data["Unnamed: 1"]=='"localized_slugs": {'].index)
data = data[["Unnamed: 1"]].values.tolist()

df=pd.DataFrame(columns=["VOI id","Name","Address","Zip","City"])
for v in range(len(name_list)):
    i = name_list[v]
    voi_id = data[i + 29]
    name = data[i + 9]
    address = data[i + 25]
    plz = data[i + 23]
    city = data[i + 26]
    temp_df = pd.Series(data=[voi_id,name,address,plz,city],
                        index=["VOI id","Name","Address","Zip","City"],
                        name=v)
    df = df.append(temp_df)
 
df = df.drop_duplicates(subset=['Address'],ignore_index=True)
    
for v in (19,25,27,39,47,53):
    i = name_list[v]
    df["VOI id"][v] = data[i + 27]
    df["Name"][v] = data[i + 7]
    df["Address"][v] = data[i + 23]
    df["Zip"][v] = data[i + 21]
    df["City"][v] = data[i + 24]

for v in range(len(name_list)):
    df["VOI id"][v] = df["VOI id"][v][0].split('"')[3]
    df["Name"][v] = df["Name"][v][0].split('"')[3]
    df["Address"][v] = df["Address"][v][0].split('"')[3]
    df["Zip"][v] = df["Zip"][v][0].split('"')[3]
    df["City"][v] = df["City"][v][0].split('"')[3]

df.to_excel("VOI list.xlsx")

# Prima https://www.prima.ch/standorte/
# Find preview of all stores in dev tool and copy paste to a txt file

data = pd.read_fwf("prima.txt", encoding='utf-8')
name_list = list(data.loc[data["Unnamed: 1"]=='},'].index)
name_list.insert(0,0)
data = data["Unnamed: 1"].tolist()

df=pd.DataFrame(columns=["Name","Address","Zip","City"])
for v in range(len(name_list)):
    i = name_list[v]
    name = data[i + 3]
    address = data[i + 11 ]
    plz = data[i + 12]
    city = data[i + 13]
    temp_df = pd.Series(data=[name,address,plz,city],
                        index=["Name","Address","Zip","City"],
                        name=v)
    df = df.append(temp_df)
    
for v in range(len(name_list)):
    df["Name"][v] = df["Name"][v].split('"')[3]
    df["Address"][v] = df["Address"][v].split('"')[3]
    df["Zip"][v] = df["Zip"][v].split('"')[3]
    df["City"][v] = df["City"][v].split('"')[3]

df=df.drop_duplicates(subset=['Name'],ignore_index=True)
df.to_excel("Prima list.xlsx")