from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os

URL = 'https://www.linkedin.com/'

class LinkedinBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Chrome()

	def login(self):
		""" This function is used to login to LinkedIN """
		bot = self.bot
		bot.get(URL)
		time.sleep(2)
		sign_in = bot.find_element_by_class_name("nav__button-secondary").click()
		time.sleep(2)
		email = bot.find_element_by_id("username")
		email.send_keys(self.username)
		time.sleep(2)
		password = bot.find_element_by_id("password")
		password.send_keys(self.password)
		time.sleep(2)
		sign_in = bot.find_element_by_class_name("btn__primary--large.from__button--floating").click()

	def search_for(self,position,page_no):
		""" This function searches for position entered from user and returns people's profile link """
		bot = self.bot
		counter = 1
		unique_links = []
		while page_no >= counter:
			str_counter = str(counter)
			search_url = bot.get(URL+'search/results/people/?keywords='+position+'&origin=SWITCH_SEARCH_VERTICAL&page='+str_counter)
			profiles = bot.find_elements_by_xpath("//a[@data-control-name='search_srp_result']")

			for person in profiles:
				link = person.get_attribute('href')
				if link not in unique_links:
					unique_links.append(link)

			counter += 1
			time.sleep(5)
		return unique_links



	def download_resume(self, links):

		""" This function is used to download resume of all links passed to it """
		bot = self.bot

		for link in links:
			bot.get(link)
			time.sleep(5)
			more = bot.find_element_by_class_name("pv-s-profile-actions__overflow-toggle.artdeco-button").click()
			time.sleep(2)
			save_pdf = bot.find_element_by_class_name("pv-s-profile-actions--save-to-pdf").click()
			time.sleep(5)


l = LinkedinBot(os.environ['MAIL'], os.environ['LINKEDIN_PASS']) # LinkedinBot(Linkedin email, Linkedin password)
l.login()
time.sleep(5)
page_no = int(input('Enter number of pages you want to search for'))
links = l.search_for('Odoo Developer', page_no)
time.sleep(5)
l.download_resume(links)