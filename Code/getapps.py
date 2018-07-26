#!/usr/bin/env python
#-*- coding: utf-8 -*-
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup as bsoup
import requests
br = mechanize.Browser()

# cookie jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Firefox/12.0')]
category = ["APPLICATION","GAME","ART_AND_DESIGN","AUTO_AND_VEHICLES","BEAUTY","BOOKS_AND_REFERENCE","BUSINESS","COMICS","COMMUNICATION","DATING","EDUCATION","ENTERTAINMENT","EVENTS","FINANCE","FOOD_AND_DRINK","HEALTH_AND_FITNESS","HOUSE_AND_HOME","LIFESTYLE","MAPS_AND_NAVIGATION","MEDICAL","MUSIC_AND_AUDIO","NEWS_AND_MAGAZINES","PARENTING","PERSONALIZATION","PHOTOGRAPHY","PRODUCTIVITY","SHOPPING","SOCIAL","SPORTS","TOOLS","TRAVEL_AND_LOCAL","VIDEO_PLAYERS","WEATHER","LIBRARIES_AND_DEMO","GAME_ARCADE","GAME_PUZZLE","GAME_CARD","GAME_CASUAL","GAME_RACING","GAME_SPORTS","GAME_ACTION","GAME_ADVENTURE","GAME_BOARD","GAME_CASINO","GAME_EDUCATIONAL","GAME_MUSIC","GAME_ROLE_PLAYING","GAME_SIMULATION","GAME_STRATEGY","GAME_TRIVIA","GAME_WORD","ANDROID_WEAR"]
for i in range(0,len(category)):
    url = "https://play.google.com/store/apps/category/"+category[i]+"/collection/topselling_free?hl=ja"
    
    html = requests.get(url).text
    soup = bsoup(html)
    
    urlslist = soup.findAll("a", { "class" : "card-click-target" })
    urls = []
    #open the file to keep the list
    filename = url[44:-33] + ".txt"
    fo = open(filename, 'w')
    
    #Url list
    for a in urlslist:
        link = "https://play.google.com" + a['href']
        urls.append(link)
    url = urls[::4]
    for item in url:
        item = item[46:] #list as package name
        fo.write("%s\n" % item)
    
    fo.close()
