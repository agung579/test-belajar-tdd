from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrive_it_later(self):
    # checkout homepage
    self.browser.get('http://localhost:8000')

    # title and header mention to-do lists
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the Test!')

    # [...rest of comments as before]

if __name__ == '__main__':
  unittest.main(warnings='ignore')
# browser = webdriver.Firefox()





# Limbago has heard about a cool new online. She goes to
# checkout its homepage
# browser.get('http://localhost:8000')

# He notices the page title and header mention to-do lists
# assert 'To-Do' in browser.title, "Browser title was " + browser.title

# She invited to enter a to-do item straight away

# She types "Buy peacock feather" into a text box (Limbago's hobby
# is typing fly-fishing lures)

# When he hits enter, the page updates, and now the pag list
# "1: Buy peacock..."


# browser.quit()