# # Scraping

# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import tweepy
import time
import pandas as pd

# Scrape function
def Scrape():

    print("COMMENCING SCRAPE")
    print("----------------------------------")

    # Empty dictionary
    mars_dict = {}

    # ## NASA Mars News

    # Mars News URL
    url = "https://mars.nasa.gov/news/"

    # Retrieve page with the requests module
    html = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html.text, 'html.parser')

    # Get title & description
    news_title = soup.find('div', 'content_title', 'a').text
    news_p = soup.find('div', 'rollover_description_inner').text

    # Adding to dict
    mars_dict["news_title"] = news_title
    mars_dict["news_p"] = news_p

    print("NEWS TITLE & DESCRIPTION ACQUIRED")


    # ## JPL Mars Space Images

    # JPL Mars URL
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through the pages
    time.sleep(5)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Get featured image
    results = soup.find('article')
    extension = results.find('figure', 'lede').a['href']
    link = "https://www.jpl.nasa.gov"
    featured_image_url = link + extension

    mars_dict["featured_image_url"] = featured_image_url

    print("FEATURED IMAGE ACQUIRED")


    # ## Mars Weather
 # set path to mars weather report Twitter page
weather_url = "https://twitter.com/MarsWxReport?lang=en"
browser.visit(weather_url)
time.sleep(2)

# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# find the paragraph tab, 
mars_soup = soup.find_all("p", class_="TweetTextSize")

weather_list = []

for weather in mars_soup:
    if re.search("Sol ", weather.text):
        weather_list.append(weather.text)

# pull just the first weather report from the list       
mars_weather = weather_list[0]

print(mars_weather)


    print("WEATHER ACQUIRED")


    # ## Mars Facts

    # Mars Facts URL
    url = "https://space-facts.com/mars/"

    # Retrieve page with the requests module
    html = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html.text, 'html.parser')

    # Empty dictionary for info
    mars_profile = {}

    # Get info
    results = soup.find('tbody').find_all('tr')

    # Storing profile information
    for result in results:
        key = result.find('td', 'column-1').text.split(":")[0]
        value = result.find('td', 'column-2').text
        
        mars_profile[key] = value
        
    # Creating a DataFrame
    profile_df = pd.DataFrame([mars_profile]).T.rename(columns = {0: "Value"})
    profile_df.index.rename("Description", inplace=True)

    # Converting to html
    profile_html = "".join(profile_df.to_html().split("\n"))

    # Adding to dictionary
    mars_dict["profile_html"] = profile_html

    print("FACTS ACQUIRED")


    # ## Mars Hemispheres

    # Mars Hemispheres URL
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Empty list of image urls
    hemisphere_image_urls = []


    # ### Valles Marineris

    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    valles_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    valles_marineris = {
        "title": "Valles Marineris Hemisphere",
        "img_url": valles_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(valles_marineris)


    # ### Cerberus

    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    cerberus_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    cerberus = {
        "title": "Cerberus Hemisphere",
        "img_url": cerberus_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(cerberus)


    # ### Schiaparelli

    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    schiaparelli_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    schiaparelli = {
        "title": "Schiaparelli Hemisphere",
        "img_url": schiaparelli_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(schiaparelli)


    # ### Syrtis Major

    # Setting up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    syrtis_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    syrtis_major = {
        "title": "Syrtis Major Hemisphere",
        "img_url": syrtis_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(syrtis_major)

    # Adding to dictionary
    mars_dict["hemisphere_image_urls"] = hemisphere_image_urls

    print("HEMISPHERE IMAGES ACQUIRED")
    print("----------------------------------")
    print("SCRAPING COMPLETED")

    return mars_dict