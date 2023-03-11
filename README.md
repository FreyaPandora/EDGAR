# EDGAR
EDGAR is a package containing 4 modules with the function to web scrape 10-K reports from companies in the S&P100 and then perform a sentimental analysis to obtain a count of all the words of interest. This analysis can then be used to see if there is a correlation between the 10-K filings and the stock prices changes.

## Edgar Downloader

- By obtaining the ticker, goes to sec.gov and obtains a list of all the 10-K filings from the last 10 years. 
- Stores each 10-K filing as a html in a folder.

## Edgar Cleaner

- Opens each html from a folder
- Removes tags, special characters, numbers and letters from the html code
- Performs text pre-processing, which includes, lower casing, tokenization, lemmatization and string joining.
- Saves the cleaned string in a text document

## Ref Data

### Get SP100
- This downloads all the tickers in the S&P100 from en excel document

### Get Yahoo Data
- Downloads all the yahoo financials data for each ticker which we are interested in for a given period of time and stores it in a csv file

### Get Sentiment Word Dictionary
- Uses the Loughran-McDonald csv to generate a dictionary that classifies different words for their sentimental value

## Write Document Sentiments
- Using the Loughran-McDonald doctionary and the text documents saved, count the number of words belonging to particular sentiment and output data into a csv file.

---
The Jupyter notebook file 'run_me.ipynb' performs each of the above steps to give sentiment factors for each company from each report. The financial data is outputted to the file 'daily_stock_prices_df.csv' which contains the price fluctuation and daily return calculations for 1,2,3, 5 and 10 business days over a period of 10 years.

*All coding and work in this reposetory was developed and completed by members of the Brixton Pod.*
