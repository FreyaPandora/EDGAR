import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def write_page(url, file_path):
    """Takes in the URL and writes the html file to the path specified."""
    driver = webdriver.Chrome()
    driver.get(url)
    
    try:
        xpath_convert_to_html = r"//a[@id='form-information-html']"
        xpath_button_click =r"//a[@id='menu-dropdown-link']"
        
        driver.find_element("xpath", xpath_button_click).click()
        correct_url =  driver.find_element("xpath", xpath_convert_to_html).get_attribute('href')
        
        driver.quit()
        driver = webdriver.Chrome()
        driver.get(correct_url)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        driver.quit()
    except:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        driver.quit()

def download_files_10k(ticker, dest_folder):
    """Downloads all the html 10-k files for the given ticker into the destination folder."""
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Construct the URL to search for the ticker's filings
    url = r'https://www.sec.gov/edgar/searchedgar/companysearch'

    # Open the search page and enter the ticker in the search box
    driver = webdriver.Chrome()
    driver.get(url)
    xpath_search_box = r'//*[@id="edgar-company-person"]'
    driver.find_element("xpath", xpath_search_box).send_keys(ticker,Keys.ENTER)

    # Wait for page to load and expand 10-K dropdown
    time.sleep(2)
    xpath_expand_selected = r'//*[@id="filingsStart"]/div[2]/div[3]/h5/a'
    driver.find_element("xpath", xpath_expand_selected).click()

    # views only 10-K and 10-Q data
    time.sleep(1)
    xpath_obtain_all_data = r'//*[@id="filingsStart"]/div[2]/div[3]/div/button[1]'
    driver.find_element("xpath", xpath_obtain_all_data).click()

    # Searches 10-K to only show the relevant filings
    xpath_search_10K = r'//*[@id="searchbox"]'
    driver.find_element("xpath", xpath_search_10K).send_keys('10-K',Keys.ENTER)

    # Download each 10-K filing
    
    # Download each 10-K filing
    table_xpath = r'//*[@id="filingsTable"]'
    wait = WebDriverWait(driver, 1)
    wait.until(EC.presence_of_element_located((By.XPATH, table_xpath)))
    table = driver.find_element(By.XPATH, table_xpath)
    rows = table.find_elements(By.XPATH, './tbody/tr')

    counter = 1
    for row in rows:
        cells = row.find_elements(By.XPATH, './td')
        filing_text = cells[2].text      
        xpath_url = '//*[@id="filingsTable"]/tbody/tr['+str(counter)+']/td[2]/div/a[1]'
        filing_url = driver.find_element("xpath", xpath_url).get_attribute('href')
        file_name = f"{ticker}_10-K_{filing_text}.html"
        file_path = os.path.join(dest_folder, file_name)
        counter += 1
        write_page(filing_url, file_path)
        
    driver.quit()



