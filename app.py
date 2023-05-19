from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)

# Set up Selenium WebDriver
driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_option)  # Assuming you have Chrome WebDriver installed

# Open Reddit in the browser
driver.get("https://www.youtube.com")

# Find the search input element and enter the search query
search_input = driver.find_element("name", "search_query")
search_input.send_keys("anime")

# Submit the search query
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load
driver.implicitly_wait(5)  # Adjust the wait time as needed
time.sleep(1)

# Find the search input element and enter the search query
search_input = driver.find_element("name", "search_query")
search_input.clear()
search_input.send_keys("games")

# Submit the search query
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load
driver.implicitly_wait(5)  # Adjust the wait time as needed

# Process the search results
results = driver.find_elements("xpath", "//div[@data-click-id='body']/a")

# Print the titles and URLs of the search results
for result in results:
    title = result.text
    url = result.get_attribute("href")
    print(f"Title: {title}")
    print(f"URL: {url}")
    print()

# Close the browser
driver.quit()
