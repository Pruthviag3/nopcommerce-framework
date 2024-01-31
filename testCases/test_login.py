import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseurl=Readconfig.getApplicattionUrl()
    username=Readconfig.getUsername()
    password=Readconfig.getpassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_HomePageTitle(self,setup):
        self.logger.info("*********** Test_001_Login ********** ")
        self.logger.info("*********** Verifying Home Page Title ********** ")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        act_title=self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********** Home Page Title is passed ********** ")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("*********** Home Page Title is failed ********** ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("*********** verify login test ********** ")
        self.logger.info("*********** Verifying Login Page Title ********** ")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*********** Login Page Title is passed ********** ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            self.logger.error("*********** Login Page Title is passed ********** ")
            assert False

