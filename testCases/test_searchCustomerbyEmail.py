import time
import pytest

from pageObjects.AddCustomer import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomer import SearchCustomer
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen



class Test_004_searchcustomer_email:
    baseurl=Readconfig.getApplicattionUrl()
    username=Readconfig.getUsername()
    password=Readconfig.getpassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("*********Test_004_searchcustomer_email********")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.logger.info("********** Login *********")
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("*********Customer Page*********")
        self.addcus=AddCustomer(self.driver)
        self.addcus.ClickOnCustomers()
        self.addcus.ClickOnCustomerMenu()

        self.logger.info("******Custer Search Page********")
        self.sc=SearchCustomer(self.driver)
        self.sc.setEmail("james_pan@nopCommerce.com")
        self.sc.clickSearch()
        time.sleep(5)
        status=self.sc.searchCustomerByEmail("james_pan@nopCommerce.com")
        assert True==status
        self.logger.info("**********Test_004_searchcustomer_email_finished******")

        self.driver.close();
