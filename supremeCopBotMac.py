# Supreme Cop Bot using Python and Selenium
#
#  To use

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

# PARTS YOU SHOULD EDIT
###########################################
# Address location of you firefox profile (for autofill)
FIREFOX_PROFILE =  '/Users/aayang/Library/Application Support/Firefox/Profiles/dpij44wh.default'
				   # Mac: '/Users/aayang/Library/Application Support/Firefox/Profiles/dpij44wh.default'

# Make this an accessory link that already exists in the store you dont want to buy
CHECKOUT_BUFFER = "http://www.supremenewyork.com/shop/accessories/stash-pill-carabiner/red"

#Keywor
KEYWORD_ONE = "short"
KEYWORD_TWO = "white"

# if Item you are trying to buy has a size, then set ITEM_HAS_SIZE to 1, otherwise zero
ITEM_HAS_SIZE = 1
SIZE = "small" # Put size that you want; Note that it will buy the next bigger size if specified size is out


CUSTOM_AUTOFILL = 1   # Set this to 0 if you dont want to use the firefox autofill plugin
# your checkout details
NAME = "Aaron Yang"
EMAIL = "xxxxxx@yahoo.com"
TEL = "4126349863"
ADDRESS = "XXXXXX st"
ZIP = "99999"
CITY = "San Francisco"
STATE = "CA"
TYPE = "Visa"
NUMBER = "1111222233334444"
EXP_DATE_MONTH = "12"
EXP_DATE_YEAR = "2017"
CVV = "420"



# DON'T EDIT THIS
###########################################
TARGET = "http://www.supremenewyork.com/shop/new"  # login page of aurora student
CHECKOUT = "https://www.supremenewyork.com/checkout"
CART = "http://www.supremenewyork.com/shop/cart"

HREF = "href"
ITEM = "inner-article"

def bufferCheckout(driver):
	driver.get(CHECKOUT_BUFFER)

	driver.find_element_by_id("add-remove-buttons").find_element_by_class_name("button").click()
	driver.find_element_by_partial_link_text("checkout")
	driver.get(CHECKOUT)
	driver.get(CART)
	driver.find_element_by_class_name("cart-remove").find_element_by_css_selector("button").click()
	time.sleep(0.75)
	driver.get(TARGET)


def selectSize(driver):

	#pick size and check if checkout button is there to checkout
	if ITEM_HAS_SIZE:
		driver.find_element_by_id("size").send_keys(SIZE)
	driver.find_element_by_id("add-remove-buttons").find_element_by_class_name("button").click()
	driver.find_element_by_partial_link_text("checkout")
	driver.get(CHECKOUT)

def cop(driver):
	#go to supreme new section of shop
	driver.get(TARGET)

	#buffer the checkout
	bufferCheckout(driver)

	#link strink to check if shop has been updated
	req = driver.find_element_by_class_name(ITEM)
	str1 = req.find_element_by_css_selector("a").get_attribute(HREF)

	driver.get(TARGET)


	i = 0
	#while we have not found our item
	while 1:
		start = time.time()

		#refresh the website and create a new list of all the items
		driver.get(TARGET)
		req1 = driver.find_elements_by_class_name(ITEM)

		#check if the first item is the same, if so, continue refreshing
		str2 = req1[0].find_element_by_css_selector("a").get_attribute(HREF)

		if( str1 == str2):
			if(i == 3):    #if you are not testing, take out the if statement str1, and increment
				str1 = "hai"
			i = i + 1
			continue


		#Once shop updates, get all of the links and check for keywords
		for i in range(len(req1)):
			link = req1[i].find_element_by_css_selector("a").get_attribute(HREF)
			if KEYWORD_ONE in link and KEYWORD_TWO in link:
				driver.get(link)
				break
		break

	#selects size and adds to cart
	selectSize(driver)

	#if profile already has custom autofill, do not execute
	if( CUSTOM_AUTOFILL == 0):
		#fill out check form
		driver.find_element_by_id("order_billing_name").send_keys(NAME)
		driver.find_element_by_id("order_email").send_keys(EMAIL)


		tel_input = driver.find_element_by_id("order_tel")
		tel_input.click()
		tel_input.send_keys(TEL)

		driver.find_element_by_id("bo").send_keys(ADDRESS)

		zip_input = driver.find_element_by_id("order_billing_zip")
		zip_input.click()
		zip_input.send_keys(ZIP)

		driver.find_element_by_id("order_billing_city").send_keys(CITY)

		driver.find_element_by_id("order_billing_state").send_keys(STATE)

		driver.find_element_by_id("credit_card_type").send_keys(TYPE)

		card_input = driver.find_element_by_id("onb")
		card_input.click()
		card_input.send_keys(NUMBER)

		driver.find_element_by_id("credit_card_month").send_keys(EXP_DATE_MONTH)

		driver.find_element_by_id("credit_card_year").send_keys(EXP_DATE_YEAR)

		driver.find_element_by_id("number_v").send_keys(CVV)

	req = driver.find_element_by_id("order_billing_state")
	req.send_keys(STATE)
	req.submit()

	end = time.time()
	print(end - start)

if __name__ == '__main__':

	#define the driver to use the special firefox settings
	fp = webdriver.FirefoxProfile(FIREFOX_PROFILE)
	driver = webdriver.Firefox(fp)
	driver.implicitly_wait(10)

	try:
		cop(driver)
	except Exception:
		print("it didn't work nigga")
		driver.close()
