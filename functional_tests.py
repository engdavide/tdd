from selenium import webdriver
import unittest

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
		self.fail('finish the test!') 

		# she is invited to add a new item right away

		# she types "buy stuff" into a text box

		# when she hits enter, the page and lists the item with a number

		# there is still a textbox to add a item. she adds "do stuff" and hits enter

		# the page updates again and now shows both items in the list

		# She wants to remember the page and sees that there is a unique URL provided for her

		# she opens the url in a new page, her list is still there.

		# yay, the end

if __name__ == '__main__':
	unittest.main(warnings='ignore')