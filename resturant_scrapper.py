from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import sqlite3

# Constants
URL = "https://www.tripadvisor.com/Search?q="
DATABASE_PATH = './databases/data.db'
JSON_OUTPUT_FILE = 'tripAdvisorData.json'
REVIEWS_XPATH = "//span[@class='reviews_header_count']"
PRICEPOINT_XPATH = "//a[@class='dlMOJ']"
RATING_XPATH = "//span[@class='ZDEqb']"
RANKING_XPATH = "//div[@class='cNFlb']/b/span"

def query_database():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    data = c.execute('SELECT name, address, state FROM resturants').fetchall()
    conn.close()
    return data

def get_restaurant_data(driver, name, addy, state):
    driver.get(URL + name + "+" + state)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'" + addy +"')]"))
    ).click()

    # Switch to the new tab
    WebDriverWait(driver, 10).until(
        lambda d: len(d.window_handles) > 1
    )
    driver.switch_to.window(driver.window_handles[-1])

    count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, REVIEWS_XPATH))
    ).text
    pricepoint = driver.find_element(By.XPATH, PRICEPOINT_XPATH).text
    rating = driver.find_element(By.XPATH, RATING_XPATH).text
    ranking = driver.find_element(By.XPATH, RANKING_XPATH).text

    return {
        "name": name,
        "address": addy,
        "state": state,
        "count": count,
        "pricepoint": pricepoint,
        "rating": rating,
        "ranking": ranking,
    }

def main():
    driver = webdriver.Chrome()
    restaurant_data = query_database()
    total_data = []

    for name, addy, state in restaurant_data:
        try:
            data = get_restaurant_data(driver, name, addy, state)
            total_data.append(data)
        except Exception as e:
            print(f"Error processing {name} in {state}: {e}")

    with open(JSON_OUTPUT_FILE, 'w') as outfile:
        json.dump(total_data, outfile)

    driver.close()

if __name__ == "__main__":
    main()
