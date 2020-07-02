from selenium import webdriver
from config import data
import time

def run():
    driver.find_elements_by_xpath('//*[@id="add-remove-buttons"]/input')[0].click()
    time.sleep(.5)
    driver.find_elements_by_xpath('//*[@id="cart"]/a[2]')[0].click()
    
    # change to Canada
    driver.find_elements_by_xpath('//*[@id="order_billing_country"]/option[2]')[0].click();
    driver.find_elements_by_xpath('//*[@id="order_billing_state"]/option[10]')[0].click();
    
    # fill form
    driver.find_elements_by_xpath('//*[@id="order_billing_name"]')[0].send_keys(data["name"])
    driver.find_elements_by_xpath('//*[@id="order_email"]')[0].send_keys(data["email"])
    driver.find_elements_by_xpath('//*[@id="order_tel"]')[0].send_keys(data["tel"])
    driver.find_elements_by_xpath('//*[@id="bo"]')[0].send_keys(data["address"])
    driver.find_elements_by_xpath('//*[@id="order_billing_zip"]')[0].send_keys(data["zip"])
    driver.find_elements_by_xpath('//*[@id="order_billing_city"]')[0].send_keys(data["city"])
    driver.find_elements_by_xpath('//*[@id="rnsnckrn"]')[0].send_keys(data["card_num"])
    driver.find_elements_by_xpath('//*[@id="orcer"]')[0].send_keys(data["card_cvv"])
    driver.find_elements_by_xpath('//*[@id="credit_card_year"]/option[2]')[0].click();
    driver.find_elements_by_xpath('//*[@id="credit_card_month"]/option[3]')[0].click();
    
    # check aggrement and pay
    driver.find_elements_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins')[0].click();
    driver.find_elements_by_xpath('//*[@id="pay"]/input')[0].click();
    
if __name__ == '__main__':
    while True:
        driver = webdriver.Chrome('./chromedriver')
        driver.get(data["url"])
        run()
        time.sleep(30)    
    