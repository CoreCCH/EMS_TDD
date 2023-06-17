from selenium import webdriver
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
        self.fail('Finish the test!')

        # 他受邀輸入一個城市地區
        # (James住在新竹縣竹北市)

        # 當他按下enter時，網頁會更新，現在網頁列出
        # "現在天氣"

        # 他很滿意的出門了


if __name__ == '__main__':
    unittest.main(warnings='ignore')

