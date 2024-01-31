import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup():
    # if browser =='chrome':
    serv_obj = Service("C:\\Users\\pruthvi.a.g\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    # elif browser == 'firefox':
    #     driver=webdriver.Firefox()
    # else:
    #     driver = webdriver.Ie()
    return driver


    # def pytest_addoption(parser):
    #     parser.addoption("--browser")
    #
    # @pytest.fixture()
    # def browser(request):
    #     return request.config.getoption("--browser")

def pytest_configure(config):
    # config._metadata['Project Name']= 'nop commerce'
    # config._metadata['Module Name'] = 'customers'
    # config._metadata['Tester'] = 'Pruthvi'
    config._metadata = {
        "Tester": "Pruthvi",
        "Project Name": "Hybrid Framework Practice",
        "Module Name":"Customers"
    }

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Java Home",None)
    metadata.pop("Plugins", None)
