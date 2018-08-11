from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# user has heard about an online to do app. She goes to the hompage
		self.browser.get('http://localhost:8000')
		# she notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# she is invited to add a new item right away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		# she types "buy stuff" into a text box
		inputbox.send_keys('buy stuff')
		# when she hits enter, the page and lists the item with a number
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1. buy stuff', [row.text for row in rows])

		# there is still a textbox to add a item. she adds "do stuff" and hits enter
		self.fail('finish the test!') 
		# the page updates again and now shows both items in the list

		# She wants to remember the page and sees that there is a unique URL provided for her

		# she opens the url in a new page, her list is still there.

		# yay, the end

if __name__ == '__main__':
	unittest.main(warnings='ignore')