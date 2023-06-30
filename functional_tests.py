from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_show_weather(self):
        # James聽到一個很酷的氣象查詢網頁
        # 他要去看它的首頁
        self.browser.get('http://localhost:8000')
        
        # 他發現網頁標題與標題顯示現在天氣
        self.assertIn('Weather', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME,'h1')
        self.assertIn('Weather', header_text)


        # 他受邀輸入一個城市地區
        inputbox = self.browser.find_element(By.ID,'id_new_city')
        self.assertEqual(
            inputbox.get_attribute('palceholder'),
            'Enter a city name'
        )

        # 他在文字方塊輸入"TAIWAN"
        inputbox.send_keys("Tainan")


        # 當他按下enter時，網頁會更新，現在網頁列出
        # "現在天氣"
        inputbox.send_keys(Keys.ENTER)

        Label = self.browser.find_element(By.ID, 'msg_label')
        self.assertTrue(
            Label.text == "Tainan weather now is"
        )
        
        self.fail("finish the test!")
        
        # 他很滿意的出門了


if __name__ == '__main__':
    unittest.main(warnings='ignore')

