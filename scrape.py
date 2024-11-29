import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


def scrape_website(website):
    print("Launching Website...")

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service= Service(chrome_driver_path),options = options)


    try:
        driver.get(website)
        print("Website successfully scraped...!")
        html = driver.page_source
        return html
    finally:
        print("Closing the browser...")
        driver.quit()
   
#TO GET ONLY THE BODY OD THE HTML FILE WHICH CONTAINS THE MAIN CONTENT
def body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_contents = soup.body
    if body_contents:
        return str(body_contents)
    else:
        print("No body contents found...!")
        return None

def cleared_content(raw_body_contents):
    soup = BeautifulSoup(raw_body_contents, 'html.parser')
    for script_or_style in soup(["script","style"]):
        script_or_style.extract()
    
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content

def split_content(dom_content, max_length=6000):
    return[dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]