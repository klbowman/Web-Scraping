#Import dependencies
import pymongo
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time


def scrape_info():
    #Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit the NASA news URL
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)
    
    # Scrape page into soup
    html = browser.html
    soup = bs(html, 'html.parser')

     # Retrieve the parent divs for all articles
    title = soup.find('div', class_= 'content_title').text
    paragraph = soup.find('div', class_= 'article_teaser_body').text
    
    # Connect browser to image url
    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)

    time.sleep(1)

    # Use splinter to find the full image url
    full_size_url = browser.links.find_by_partial_text('FULL IMAGE')['href']

    # URL of news page to be scraped
    facts_url = 'https://galaxyfacts-mars.com/'
    # Use Panda's `read_html` to parse the url
    table = pd.read_html(facts_url)
    mars_df = table[0]
    mars_df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
    mars_df = mars_df.drop([0])
    mars_df = mars_df.set_index(['Mars-Earth Comparison'])
    mars_table = mars_df.to_html()
    mars_table = mars_table.replace("\n", "")

    # Connect browser to image url
    images_url = 'https://marshemispheres.com/'
    browser.visit(images_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Create empty list to hold titles
    img = []

    for i in range (4):

        browser.links.find_by_partial_text('Enhanced').click()
            
        html = browser.html
        soup = bs(html, 'html.parser')
        # Retrieve all elements that contain book information
        images = soup.find('img', class_="wide-image")['src']
        img.append(images_url + images)
        browser.back()

    # Connect browser to image url
    images_url = 'https://marshemispheres.com/'
    browser.visit(images_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Create empty list to hold titles
    labels = []

    # Retrieve hemisphere titles
    results = soup.find_all('div', class_='item')

    for result in results:
        titles = result.find('h3').text
        labels.append(titles) 
    
    
    #Append the dictionary with the image url string and the hemisphere title to a list.
    mars_scrape = {
        "title1": labels[0], "img_url1": img[0],
        "title2": labels[1], "img_url2": img[1],
        "title3": labels[2], "img_url3": img[2],
        "title4": labels[3], "img_url4": img[3],
        "news_title": title,
        "text": paragraph,
        "full_image": full_size_url,
        "table": mars_table}
    

    # Close the browser after scraping
    browser.quit()

    #Return results
    return mars_scrape

if __name__ == "__main__":
    app.run(debug=True)
