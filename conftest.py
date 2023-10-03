import pytest


@pytest.fixture

def chrome_options(chrome_options):
    chrome_options.binary_location = ('C:/chromedriver-win32/chromedriver.exe')
    chrome_options.add_extension('/path/to/extension.crx')
    chrome_options.add_argument('--kiosk')
    return chrome_options


