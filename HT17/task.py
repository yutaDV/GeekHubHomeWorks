"""Автоматизувати процес замовлення робота за допомогою Selenium
1. Отримайте та прочитайте дані з "https://robotsparebinindustries.com/orders.csv".
Увага! Файл має бути прочитаний з сервера кожного разу при запускі скрипта,
не зберігайте файл локально.
2. Зайдіть на сайт "https://robotsparebinindustries.com/"
3. Перейдіть у вкладку "Order your robot"
4. Для кожного замовлення з файлу реалізуйте наступне:
    - закрийте pop-up, якщо він з'явився. Підказка: не кожна кнопка його закриває.
    - оберіть/заповніть відповідні поля для замовлення
    - натисніть кнопку Preview та збережіть зображення отриманого робота. Увага!
    Зберігати треба тільки зображення робота, а не всієї сторінки сайту.
    - натисніть кнопку Order та збережіть номер чеку. Увага! Інколи сервер тупить
    і видає помилку, але повторне натискання кнопки частіше всього вирішує проблему. Дослідіть цей кейс.
    - переіменуйте отримане зображення у формат <номер чеку>_robot. Покладіть зображення в директорію output
    (яка має створюватися/очищатися під час запуску скрипта).
    - замовте наступного робота (шляхом натискання відповідної кнопки)
5. Для загального розуміння можна переглянути відео https://www.youtube.com/watch?v=0uvexJyJwxA&ab_channel=Robocorp
** Додаткове завдання (необов'язково)
    - окрім збереження номеру чеку збережіть також HTML-код всього чеку
    - збережіть отриманий код в PDF файл
    - додайте до цього файлу отримане зображення робота (бажано на одній сторінці, але не принципово)
    - збережіть отриманий PDF файл у форматі <номер чеку>_robot в директорію output. Окремо зображення робота зберігати
     не потрібно."""
import time
import os
import shutil
from pathlib import Path

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

import read_csv

class RobotsPlacer:
    def __init__(self, head, body, legs, address):
        self.url = 'https://robotsparebinindustries.com/#/robot-order'
        self.driver: Chrome | None = None
        self.head = head
        self.body = body
        self.legs= legs
        self.address = address


    def __enter__(self):
        self.driver = self.__init_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()

    def __init_driver(self):
        service = Service(ChromeDriverManager().install())
        chrome_options = ChromeOptions()

        service_args = [
            '--no-sandbox',
            '--disable-web-security',
            '--allow-running-insecure-content',
            '--hide-scrollbars',
            '--disable-setuid-sandbox',
            '--profile-directory=Default',
            '--ignore-ssl-errors=true',
            '--disable-dev-shm-usage'
        ]
        for argument in service_args:
            chrome_options.add_argument(argument)

        chrome_options.add_experimental_option(
            'excludeSwitches', ['enable-automation']
        )

        chrome_options.add_experimental_option(
            'prefs', {
                'profile.default_content_setting_values.notifications': 2,
                'profile.default_content_settings.popups': 0
            }
        )

        driver = Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        return driver

    def flow(self):
        self.open_site()
        self.go_to_order()
        self.close_pop()
        self.input_head()
        self.input_body()
        self.input_legs()
        self.input_address()
        self.preview()
        self.save_screen()
        self.saved_order()
        self.rename_screen()
        return

    def open_site (self):
        self.driver.get('https://robotsparebinindustries.com/')
        self._wait_for_element('a.nav-link')
        return

    def _wait_for_element(self, selector: str, by: By = By.CSS_SELECTOR, timeout: int = 5, silent: bool = True) -> WebElement | None:
        try:
            condition = EC.presence_of_element_located((by, selector))
            element = WebDriverWait(self.driver, timeout).until(condition)
            return element
        except TimeoutException:
            if silent:
                return
            raise

    def go_to_order(self):
        self.driver.get(self.url)
        return

    def close_pop(self):
        close = self._wait_for_element('button.btn.btn-dark')
        close.click()
        return

    def input_head(self):
        head= Select(self._wait_for_element('#head'))
        head.select_by_value(self.head)
        return

    def input_body(self):
        selector = f'#root > div > div.container > div > div.col-sm-7 > form > div:nth-child(2) > div > div:nth-child({self.body}) > label'
        body = self._wait_for_element(selector)
        body.click()
        return

    def input_legs(self):
        legs=self._wait_for_element('input.form-control')
        legs.send_keys(self.legs)
        return

    def input_address(self):
        address=self._wait_for_element('#address')
        address.send_keys(self.address)
        return

    def preview(self):
        preview = self._wait_for_element('#preview')
        preview.click()
        return

    def save_screen(self):
        screen = Path.cwd()
        robot_screen = self._wait_for_element('#robot-preview-image')
        robot_screen.screenshot(str(Path(screen, 'robot.png')))
        return

    def saved_order(self):
        preview = self._wait_for_element('#order')
        preview.click()
        return

    def check_number(self):
        check_number = self.driver.find_element(By.CLASS_NAME, 'badge.badge-success').text
        return check_number

    def rename_screen(self):
        new_name = self.check_number() + '_robot.png'
        os.rename('robot.png', new_name)
        return

    def move_file(self):
        file_name = self.rename_screen()
        way = Path.home()
        source_path = "/HT17/"
        destination_path = "HT17/output/"
        os.rename(source_path + file_name, destination_path + file_name)
        return


if __name__ == '__main__':

    os.rmdir('output')
    os.mkdir('output')
    file = read_csv.CsvFile()
    robot_param = file.read_file()
    for order in robot_param:
        with RobotsPlacer(order[0], order[1], order[2], order[3]) as placer:
            placer.flow()
            pass

