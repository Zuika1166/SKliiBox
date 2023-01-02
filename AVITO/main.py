from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

URL = 'https://www.avito.ru/moskva/avtomobili/daewoo/matiz-ASgBAgICAkTgtg2AmCjitg2~qig?cd=1&f=ASgBAQECAkTgtg2AmCjitg2~qigBQPbEDRS~sDoBRcaaDBZ7ImZyb20iOjAsInRvIjoxNTAwMDB9&radius=500&s=104'
PAUSE_DURATION_SECONDS = 5


def main():
    driver.get(URL)
    sleep(PAUSE_DURATION_SECONDS)


    


if __name__ == '__main__':
    try:
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        main()

        a = find_more_element = driver.find_element_by_class_name("iva-item-content-rejJg")
        soup = BeautifulSoup(driver.page_source, "lxml")

        div_full = soup.find("div", class_="iva-item-content-rejJg").text.strip()
        div_price = soup.find("span", class_="price-text-_YGDY").text.strip()
        div_image = soup.find("img", class_="photo-slider-image-YqMGj").get_attribute_list('src')

        # i can't show phone number
        div_phone_number = soup.find("span", class_="price-text-_YGDY").text.strip()
        div_reload = soup.find("span", class_="price-text-_YGDY").text.strip()
        

        hover = driver.find_element_by_xpath("//div[@id='i2673054118']")  # Наведение мыши

      
        print(div_reload)
        print(div_price)
        print(div_image)


    except Exception as e:
        print(e)
    finally:
        driver.quit()



