import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseurl=Readconfig.getApplicattionUrl()
    path=".//testData/LoginData.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_Login_DDT(self,setup):
        self.logger.info("*********** verify Test_002_DDT_Login ********** ")
        self.logger.info("*********** Verifying Login DDT Test ********** ")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,"Sheet1")
        print("Number of rows",self.rows)

        lst_status = []

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("****** Passed *****")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("****** Failed *****")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("****** Failed *****")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("****** Passes *****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("***** Login DDT test is passed****")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Login DDT test is failed****")
            self.driver.close()
            assert False

        self.logger.info("*******End of Login DDT Test*****")
        self.logger.info("*******Completed TC_login_DDT_002*****");








