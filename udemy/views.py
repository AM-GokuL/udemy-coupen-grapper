from django.http import HttpResponse #importing django file
from django.shortcuts import render #importing django file
from bs4 import BeautifulSoup  #scrapping package
import requests 
import json 
#function
def scrape_category(name):
    base_url = 'https://udemycoupon.learnviral.com/coupon-category/' + name + '/' #scrapping 
    source = requests.get(base_url).text #converting from html to text
    soup = BeautifulSoup(source, 'html.parser') #initializing beautiful soup 
    contents = soup.find_all('div', class_='item-holder') 
    courses = [] #emptylist 
    for item in contents:
        heading = item.find('h3', {'class': 'entry-title'}).text.replace('[Free]', '')
        image = item.find('div', {'class': 'store-image'}).find('img')['src']
        course_link = item.find('a', {'class': 'coupon-code-link btn promotion'})['href']
        success_rate = item.find('span', {'class': 'percent'}).text
        courses.append({
            "heading": heading,
            "image": image.replace('240x135', '750x422'),
            "courselink"x: course_link,
            "successrate" : success_rate,
        })

    return courses


def index(req):
    result = {}  #empty dictionary
    for category in ("development", "it-software", "business", "office-productivity", "personal-development"," design", "marketing","language", "test-prep"):
        result[category] = scrape_category(category)

    data = json.dumps([result])  # oArr print([result])
    return HttpResponse(data.strip('"'), content_type="application/json") #alignment
 
def all(req):
    for category in ("development", "it-software", "business", "office-productivity", "personal-development"," design", "marketing","language", "test-prep"):
        data = json.dumps(scrape_category(category))
    return HttpResponse(data.strip('"'), content_type="application/json")

