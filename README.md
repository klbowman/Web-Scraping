# Web Scraping 

Web application that scrapes images, text, and a table from multiple websites, and displays them in a single HTML page.

## Description

This HTML page displays data and images on the planet Mars, sourced from 4 different websites. 
<p align="center">
  <img src="https://user-images.githubusercontent.com/74067302/145475669-e5b72ec5-4f12-4cc2-962a-8942551f2378.png" alt="Webpage image"/>
</p>

Initial web scraping was done in Jupyter Notebook (mission_to_mars.ipynb) using BeautifulSoup, Pandas, and Requests/Splinter.
* BeautifulSoup used to retrieve latest news headline and paragrpah text image url
* Pandas used to scrape table and store as string
* Splinter used to navigate to enhanched image links

This repository is designed to visualize taxonomic data using charts, and display metadata in an organized panel. The [data](http://robdunnlab.com/projects/belly-button-biodiversity/results-and-data/) comes from a study that sequenced the microbiome of 153 human belly buttons (Hulcr et al., 2012), and is stored in the samples.json file. Individual samples are identified by a numerical code and accompanied by metadata including age, gender, ethnicity, etc. Operational taxonomic units (OTUs) id numbers and counts are provided for each sample.

The dashboard includes a drop-down menu that displays the numerical code for each individual sample. When a sample is selected, the “Demographic Info” panel is populated with metadata and the following three charts are populated with data:
* Bar graph displaying the top 10 OTUs by count
* Gauge plot showing the belly button scrubs per week
* Bubble plot displaying OTU counts for the entire sample

<p align="center">
  <img src="https://user-images.githubusercontent.com/74067302/145448320-bbe43cc2-f2fc-4fb7-955d-1c9fcb553b96.png" alt="Dashboard Image"/>
</p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/74067302/145448339-7e38f680-868a-4b75-85b9-0467e83002c9.png" alt="Dashboard Image"/>
</p>



## Getting Started

### Technologies Used 

* Jupyter Notebook
* Pandas
* Pyton
* BeautifulSoup
* Requests/Splinter
* HTML
* MongoDB
* Flask

### Installing

* Clone this repository to your desktop....run app.py files...
* Navitage to the home directory and open index.html in your browser.

### Websites scraped

* [Mars Planet Science Exploration Program](https://redplanetscience.com/)
* [Jet Propulsion Laboratory: California Institute of Technology](https://spaceimages-mars.com/)
* [Galaxy Facts: Mars](https://galaxyfacts-mars.com/)
* [AstropediaLunar and Planetary Cartographic Catalog](https://marshemispheres.com/)


## Authors

Katlin Bowman, PhD

E: klbowman@ucsc.edu

[LinkedIn](https://www.linkedin.com/in/katlin-bowman/)
