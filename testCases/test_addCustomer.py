from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from selenium.webdriver.common.by import By
import string
import random
import pytest

class Test_003_addCustomer:
    baseurl=Readconfig.getApplicattionUrl()
    username=Readconfig.getUsername()
    password=Readconfig.getpassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info("********** Login Page ********")
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("******* Home Page ******")

        self.addcus=AddCustomer(self.driver)
        self.addcus.ClickOnCustomers()
        self.addcus.ClickOnCustomerMenu()
        self.addcus.ClickOnAddNew()
        self.email =random_generator() + "@gmail.com"
        self.addcus.setEmail(self.email)
        self.addcus.setPassword("test123")
        self.addcus.setFirstName("ABC")
        self.addcus.setLastName("xyz")
        self.addcus.setGender("Male")
        self.addcus.setDOB("12/12/1993")
        self.addcus.setCompanyName("asdf")
        self.addcus.clickIsTaxExempt()
        self.addcus.selectNewsletter("Test store 2")
        self.addcus.setCustomerRole("Guests")
        self.addcus.setManagerOfVendor("2")
        self.addcus.setAdminComment("hello")
        self.addcus.clickSave()

        self.logger.info("******* Saving Data ******")
        self.msgs=self.driver.find_element(By.XPATH,"/html/body").text
        print(self.msgs)
        if "customer has been added successfully." in self.msgs:
            assert True
        else:
            self.logger.save_screenshot(".\\Screenshots" + "test_addcustomer_scr.png")
            assert False

        self.driver.close()

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))

