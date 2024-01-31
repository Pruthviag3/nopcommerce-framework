import time
import pytest

from pageObjects.AddCustomer import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomer import SearchCustomer
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_005_searchCustomerByName:
    baseurl=Readconfig.getApplicattionUrl()
    username=Readconfig.getUsername()
    password=Readconfig.getpassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("*********Test_005_searchCustomerByName********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.logger.info("*********Login*********")
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("**********Customer*********")
        self.addcus=AddCustomer(self.driver)
        self.addcus.ClickOnCustomers()
        self.addcus.ClickOnCustomerMenu()

        self.logger.info("*********Search page********")
        self.sn=SearchCustomer(self.driver)
        self.sn.setFirstName("Arthur")
        self.sn.setLastName("Holmes")
        self.sn.clickSearch()
        time.sleep(5)
        status=self.sn.searchCustomerByName("Arthur Holmes")
        assert True==status
        self.logger.info("*********Test_005_searchCustomerByName Ended********")
        self.driver.close();


