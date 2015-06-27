# Supreme Cop Bot using Python and Selenium
#
#  To use

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

USER_CREDENTIAL = {
	'id': "",
	'pin': ""
}

TERM = "Summer"  # eg. Summer 2015
SUBJECT = "Computer Science"  # eg. Computer Science
COURSE = "2015"  # eg. 2080
SECTION = "A01"
TARGET = "http://www.supremenewyork.com/shop/new"  # login page of aurora student


def select_term(driver):
	term_select_elem = driver.find_element_by_id("term_input_id")
	Select(term_select_elem).select_by_visible_text(TERM)
	submit = driver.find_element_by_xpath("//input[@value='Submit']")
	submit.click()


def select_subject(driver):
	term_select_elem = driver.find_element_by_id("subj_id")
	Select(term_select_elem).select_by_visible_text(SUBJECT)
	search = driver.find_element_by_xpath("//input[@value='Course Search']")
	search.click()


def select_course(driver):
	courses = driver.find_elements_by_tag_name("tr")
	found = False
	for course in courses:
		if found:
			break
		for elem in course.find_elements_by_tag_name('td'):
			if elem.text == COURSE:
				found = True
				btn = course.find_element_by_xpath("//input[@value='View Sections']")
				btn.click()
				break


def automation(driver):
	driver.get(TARGET)

	username = driver.find_element_by_id("UserID")
	pin = driver.find_element_by_name("PIN")
	username.send_keys(USER_CREDENTIAL['id'])
	pin.send_keys(USER_CREDENTIAL['pin'])

	login_button = driver.find_element_by_xpath("//input[@value='Login']")
	login_button.click()

	enrolment_link = driver.find_element_by_link_text('Enrolment & Academic Records')
	enrolment = ActionChains(driver).move_to_element(enrolment_link).click()
	enrolment.perform()

	registration_link = driver.find_element_by_link_text('Registration and Exams')
	enrolment = ActionChains(driver).move_to_element(registration_link).click()
	enrolment.perform()

	lookup_link = driver.find_element_by_link_text('Look Up Classes')
	lookup = ActionChains(driver).move_to_element(lookup_link).click()
	lookup.perform()

	select_term(driver)
	select_subject(driver)
	select_course(driver)

	driver.close()


def cop(driver):
	#go to supreme new section of shop
	driver.get(TARGET)

	#boolean to break out of lop[
	found = 0

	#link strink to check if shop has been updated
	req = driver.find_element_by_class_name("inner-article")
	str1 = req.find_element_by_css_selector("a").get_attribute("href")


	print(str1)

	#while we have not found our item
	while found == 0:

		#refresh the website and create a new list of all the itemms
		driver.get(TARGET)
		req1 = driver.find_elements_by_class_name("inner-article")

		#check if the first item is the same, if so, continue refreshing
		str2 = req1[0].find_element_by_css_selector("a").get_attribute("href")
		print(str2)
		#if( str1 == str2):
			#continue

		#Once shop updates, get all of the links and check for keywords
		for i in range(len(req1)):
			link = req1[i].find_element_by_css_selector("a").get_attribute("href")
			if "white" in link and "short" in link:
				driver.get(link)
				found = 1
				break




	print(driver.current_url)





if __name__ == '__main__':
	driver = webdriver.Firefox()
	try:
		cop(driver)
	except Exception:
		print("it didn't work nigga")
		driver.close()
