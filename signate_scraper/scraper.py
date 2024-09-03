from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from io import StringIO

class SignateScraper:
    def __init__(self, headless=True):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, email, password):
        self.driver.get('https://user.cloud.signate.jp/sign_in')
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, 'biz_user_email')))
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.ID, 'biz_user_password')
        password_input.send_keys(password)
        login_button = self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "サインイン")]')))
        login_button.click()
        self.wait.until(EC.url_contains('dashboard'))

    def get_latest_rank(self, competition_id):
        url = f'https://biz.quest.signate.jp/quests/{competition_id}'
        self.driver.get(url)
        challenge_link = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Challenge")]')))
        challenge_link.click()
        ranking_tab = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//li[contains(text(), "ランキング")]'))
        )
        # ポップアップを無視して無理やり押下
        self.driver.execute_script("arguments[0].click();", ranking_tab)

        # テーブルが表示されるまで待機
        table_element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "p-table-ranking")]//table'))
        )
        # テーブルのHTMLを取得
        table_html = table_element.get_attribute('outerHTML')
        # Pandasでテーブルを解析
        df = pd.read_html(StringIO(table_html))[0]  # 最初のテーブルを取得
        return df

    def close(self):
        self.driver.quit()
