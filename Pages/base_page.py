from pathlib import Path
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os.path
import requests
import logging


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.download_dir = self._get_download_dir()
        self.logger = logging.getLogger(type(self).__name__)

    def _get_download_dir(self) -> Path:
        current_dir = Path(__file__).parent
        if current_dir.name == "tests":
            return current_dir / "tests"
        return current_dir.parent / "tests"

    def open(self, url:str) -> None:
        self.logger.info(f'Открываем {url}')
        return self.driver.get(url)

    def get_current_url(self) -> str:
        self.logger.info('Возвращаем текущий URL')
        return self.driver.current_url

    def get_title(self) -> str:
        self.logger.info('Возвращаю текущий заголовок')
        return self.driver.title


    def find_element(self, locator, timeout = 10):
        self.logger.debug(f'Ищу элемент с помощью локатора: {locator}')
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator),
            message = f'Не могу найти локатор:{locator}'
            )
            self.logger.debug(f'Элемент с локатором {locator} найден')
            return element
        except TimeoutException as e:
            self.logger.debug(f'Элемент с локатором {locator} не найден ')
            return e

    def find_elements(self, locator, timeout = 10):
        self.logger.debug(f'Ищу элемент с помощью локатора: {locator}')
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator),
            message = f'Не могу найти локатор:{locator}'
            )
            self.logger.debug(f'Элемент с локатором {locator} найден')
            return elements
        except TimeoutException as e:
            self.logger.debug(f'Элемент с локатором {locator} не найден ')
            return e

    def click(self, locator, timeout = 10) -> None:
        self.logger.info(f'Нажатие на элемент с локатором {locator}')
        element = self.find_element(locator, timeout)
        element.click()

    def get_text(self, locator, timeout = 10) -> str:
        self.logger.info(f'Получаем текст элемента {locator}')
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator),
            message = f'Не могу найти локатор:{locator}'
            )
            self.logger.debug(f'Элемент с локатором {locator} найден')
            return element.text
        except TimeoutException as e:
            self.logger.debug(f'Элемент с локатором {locator} не найден ')
            return e

    def switch_on_last_window(self) -> None:
        self.logger.info('Переключение на последнюю открытую вкладку')
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def scroll_on_600_pixels(self) -> None:
        self.logger.info('Скроллим вниз на 600 пикселей')
        ActionChains(self.driver).scroll_by_amount(0, 600)

    def scroll_on_element(self, locator, timeout = 10) -> None:
        self.logger.info(f'Переход к элементу {locator}')
        element = self.find_element(locator, timeout)
        element.location_once_scrolled_into_view

    def download_file(self, url:str, filename:str) -> Path:
        self.logger.info(f'Скачиваем файл по ссылке {url}')
        filename = self.download_dir / filename
        respons = requests.get(url)
        if respons.status_code == 200:
            with  open(filename, 'wb') as file:
                file.write(respons.content)
            self.logger.info(f'Файл {filename} успешно скачан')
        else:
            self.logger.info(f'Ошибка при загрузке файла {filename}')
        return filename

    def check_file_size(self, filename:str) -> float:
        return os.path.getsize(filename) / (1024 * 1024)

