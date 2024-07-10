import sys
import pytest
from selenium.webdriver import Chrome, Remote
from selenium.webdriver.chrome.options import Options


@pytest.fixture(name="driver")
def driver_fixture() -> Chrome:

    options = Options()
    options.add_argument("--start-maximized")
    driver = Chrome(options=options)
    # if sys.platform == "win32":
    #     driver = Chrome(options=options)
    # else:
    #     driver = Remote(
    #         command_executor="http://selenium__standalone-chrome:4444/wd/hub",
    #         options=options
    #     )

    yield driver
    driver.quit()
