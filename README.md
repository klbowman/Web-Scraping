# Web Scraping 

Images and text scraped from multiple websites displayed in a single HTML page.

## Description

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

* Clone this repository to your desktop.
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
