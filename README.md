# Web Scraping 

Web application that scrapes images, text, and a table from multiple websites, and displays them in a single HTML page.

## Description

This HTML page displays text, images, and a data table about the planet Mars, sourced from 4 different websites. 
<p align="center">
  <img src="https://user-images.githubusercontent.com/74067302/145475669-e5b72ec5-4f12-4cc2-962a-8942551f2378.png" alt="Webpage image"/>
</p>

Initial web scraping is done in Jupyter Notebook (mission_to_mars.ipynb) using BeautifulSoup, Pandas, and Requests/Splinter:
* BeautifulSoup is used to retrieve HTML elements, including text and image urls 
* Pandas is used to scrape information from a data table and store it as a string
* Splinter is used to navigate to enhanced image links

The Jupyter Notebook file (mission_to_mars.ipynb) was converted into a Python script (scrape_mars.py) with a function called scrape to execute the code. This scrape function returns one Python dictionary containing all of the scraped data.

Flask is used to render the HTML template (index.html) and connect to MongoDB. The flask app includes a route that triggers the scrape function and stores the data in Mongo as a Python dictionary. 

## Getting Started

### Technologies Used 

* Jupyter Notebook
* Pandas
* Python
* BeautifulSoup
* Requests/Splinter
* HTML
* MongoDB
* Flask

### Installing

* Clone this repository to your desktop.
* Run the app.py file.

### Websites scraped

* [Mars Planet Science Exploration Program](https://redplanetscience.com/)
* [Jet Propulsion Laboratory: California Institute of Technology](https://spaceimages-mars.com/)
* [Galaxy Facts: Mars](https://galaxyfacts-mars.com/)
* [AstropediaLunar and Planetary Cartographic Catalog](https://marshemispheres.com/)


## Authors

Katlin Bowman, PhD

E: klbowman@ucsc.edu

[LinkedIn](https://www.linkedin.com/in/katlin-bowman/)
