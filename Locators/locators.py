from selenium.webdriver.common.by import By


class SabyMainPageLocators:
    CONTACT_BUTTOM = (By.CSS_SELECTOR, "div.sbisru-Header__menu-link.sbis_ru-Header__menu-link.sbisru-Header__menu-link--hover")#Кнопка контакты в шапке сайта
    CONTACT_HREF = (By.XPATH, '//span[contains(text(), "офисов в регионе")]')#Ссылка офисов в регионе
    DOWNLOAD_HREF = (By.XPATH, '//a[@href="/download"]')#Ссылка к разделу скачки


class SabyContactPageLocator:
    LOGO_TENSOR = (By.CSS_SELECTOR, 'a.sbisru-Contacts__logo-tensor.mb-12')#image Тензор
    CURRENT_REGION = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]')#Текущая область
    CHOOSER_REGION = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]')#Выбор региона
    PARTNERS = (By.CSS_SELECTOR, 'div.sbisru-Contacts-List__name.sbisru-Contacts-List--ellipsis.sbisru-Contacts__text--md.pb-4.pb-xm-12.pr-xm-32')#Список партнеров
    KAMCHATSKY_REGION = (By.XPATH, '//span[contains(text(), "Камчатский край")]')#Камчатский край


class TensorMainPageLocators:
    TEXT_POWER_PEOPEL = (By.CSS_SELECTOR, 'div.tensor_ru-Index__block4-content.tensor_ru-Index__card')#Блок с текстом "Сила в людях"
    HREF_MORE = (By.XPATH, '//a[@href="/about" and @class="tensor_ru-link tensor_ru-Index__link"]')#Ссылка Подробнее блока "Сила в людях"


class TensorAboutPageLocarots:
    TEXT_WORKING = (By.XPATH, '//h2[text()="Работаем"]')#Текс Работаем
    PHOTO_WORKING = (By.XPATH, '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]')#image Работаем


class SabyDownloadPageLocators:
    DOWNLOAD_HREF = (By.XPATH, '//a[@href="https://update.saby.ru/SabyDesktop/master/win32/saby-setup-web.exe"]')#Ссылка на скачивание