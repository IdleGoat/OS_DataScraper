# OS_DataScraper
OS_DataScraper is a Python script for scraping data from HTML files and saving it to a CSV file. It uses the BeautifulSoup library to extract information from the HTML files.
## Getting Started
To use OS_DataScraper, you'll need to have Python 3 and the BeautifulSoup library installed on your computer. You can install BeautifulSoup using pip:
```python
pip install beautifulsoup4
```
Once you have Python and BeautifulSoup installed, you can run the script by running the following command in your terminal:
```python
python scraper.py
```
## Usage
OS_DataScraper is designed to scrape data from HTML files in a specific format. The HTML files should contain multiple "question divs", each with a "question text" and a set of "answer options". The correct answer should also be marked in the HTML file.

To use OS_DataScraper with your own HTML files, you'll need to modify the scraper.py script to match the format of your HTML files. You may also need to modify the CSV output to match your specific needs.

## Contributing
If you find a bug or have a feature request, please open an issue on the [GitHub repository](https://github.com/IdleGoat/OS_DataScraper/issues). Pull requests are also welcome!

## Acknowledgments
This project was inspired by the need to quickly scrape data from HTML files for a research project. Thanks to the developers of BeautifulSoup for creating such a useful library!




