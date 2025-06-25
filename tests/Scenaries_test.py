from Locators.locators import SabyDownloadPageLocators as SabyDownload
from Locators.locators import SabyMainPageLocators as SabyMain
from Locators.locators import SabyContactPageLocator as SabyContact
from Locators.locators import TensorMainPageLocators as TensorMain
from Locators.locators import TensorAboutPageLocarots as TensorAbout
from Pages.saby_main_page import SabyMainPage
from conftest import driver


class TestSabyMain:
    BASE_URL = "https://saby.ru/"

    def test_scenario_one(self, driver):
        page = SabyMainPage(driver)
        page.open(self.BASE_URL)
        page.find_element(SabyMain.CONTACT_BUTTOM)
        page.click(SabyMain.CONTACT_BUTTOM)
        page.click(SabyMain.CONTACT_HREF)
        page.click(SabyContact.LOGO_TENSOR)
        page.switch_on_last_window()
        text_power_people = page.get_text(TensorMain.TEXT_POWER_PEOPEL)
        assert text_power_people[:12] == "Сила в людях"
        page.click(TensorMain.HREF_MORE)
        assert page.get_current_url() == 'https://tensor.ru/about'
        page.scroll_on_600_pixels()
        page.scroll_on_element(TensorAbout.TEXT_WORKING)
        photos = page.find_elements(TensorAbout.PHOTO_WORKING)
        assert all(photos[0].size == photo.size for photo in photos)

    def test_scenario_two(self, driver):
        page = SabyMainPage(driver)
        page.open(self.BASE_URL)
        page.find_element(SabyMain.CONTACT_BUTTOM)
        page.click(SabyMain.CONTACT_BUTTOM)
        page.click(SabyMain.CONTACT_HREF)
        home_region = page.get_text(SabyContact.CURRENT_REGION)
        assert home_region == 'Ярославская обл.'
        partners = page.find_elements(SabyContact.PARTNERS)[0].text
        assert partners, 'Партнеры не отображаются'
        page.click(SabyContact.CHOOSER_REGION)
        page.click(SabyContact.KAMCHATSKY_REGION)
        page.find_element(SabyContact.KAMCHATSKY_REGION)
        current_region = page.get_text(SabyContact.CURRENT_REGION)
        assert current_region == 'Камчатский край'
        current_partners = page.find_elements(SabyContact.PARTNERS)
        assert partners != current_partners[0].text
        assert page.get_title().removeprefix('Saby Контакты — ') == 'Камчатский край'
        assert page.get_current_url().removeprefix('https://saby.ru/contacts/').removesuffix('?tab=clients') == '41-kamchatskij-kraj'

    def test_scenario_tree(self, driver):
        page = SabyMainPage(driver)
        page.open("https://saby.ru/")
        page.find_element(SabyMain.DOWNLOAD_HREF)
        page.click(SabyMain.DOWNLOAD_HREF)
        href_download = page.find_element(SabyDownload.DOWNLOAD_HREF).get_attribute('href')
        filename = href_download.rsplit('/', 1)[-1]
        path_name = page.download_file(href_download, filename)
        size_download_file = f'{page.check_file_size(path_name):.2f}'
        size_on_website = page.get_text(SabyDownload.DOWNLOAD_HREF).removeprefix('Скачать (Exe ').removesuffix(' МБ)')
        assert size_on_website == size_download_file



