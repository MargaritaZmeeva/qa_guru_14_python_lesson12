# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selene import Browser, Config
#
# from utils import attach
#
#
# @pytest.fixture(scope='function')
# def setup_chrome():
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": "100.0",
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": False
#         }
#     }
#     options.capabilities.update(selenoid_capabilities)
#
#     driver = webdriver.Remote(
#         command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=options
#     )
#     browser = Browser(Config(driver))
#
#     yield browser
#
#     attach.add_html(browser)
#     attach.add_screenshot()
#     attach.add_html(browser)
#     attach.add_video(browser)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from utils import attach

@pytest.fixture(scope='function')
def setup_chrome():
    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "100.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False
    })

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser = Browser(Config(driver=driver))

    yield browser  # Передаем объект browser в тест

    # Добавление вложений перед закрытием браузера
    attach.add_html(browser)
    attach.add_screenshot()

    driver.quit()  # Закрываем браузер после теста
