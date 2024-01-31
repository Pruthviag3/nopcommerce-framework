import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    lnkCustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddNew_xpath="//a[normalize-space()='Add new']"
    txtEmail_xpath="//input[@name='Email']"
    txtpassword_xpath="//input[@name='Password']"
    txtFirstName_xpath="//input[@name='FirstName']"
    txtLastName_xpath="//input[@name='LastName']"
    rdMale_xpath="//input[@value='M']"
    rdFemale_xpath="//input[@value='F']"
    txtDateOfBirth_xpath="//input[@name='DateOfBirth']"
    txtCompanyName_xpath="//input[@name='Company']"
    cbIsTaxExempt_xpath="//input[@data-val-required='The Is tax exempt field is required.']"
    txtNewsletter_xpath="//div[@class='input-group-append']//div[@role='listbox']"
    lstitmYourStoreName_xpath="//span[normalize-space()='Your store name']"
    lstitmTestStory2_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"
    txtCustomerRoles_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitmAdministtrator_xpath="//*[@class='k-list k-reset']//li[contains(text(),'Administrators')]"
    lstitmForumModeraators_xpath="//*[@class='k-list k-reset']//li[contains(text(),'Forum Moderators')]"
    lstitmGuests_xpath="//*[@class='k-list k-reset']//li[contains(text(),'Guests')]"
    lstitmRegistered_xpath="//*[@class='k-list k-reset']//li[contains(text(),'Registered')]"
    lstitmVendors_xpath="//*[@class='k-list k-reset']//li[contains(text(),'Vendors')]"
    drbMangerOfVendor_xpath="//select[@name='VendorId']"
    cbActive_xpath="//input[@checked='checked']"
    txtAdminComment_xpath="//textarea[@name='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def ClickOnCustomers(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def ClickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def ClickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtpassword_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastname)

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH,self.rdMale_xpath).click()
        elif gender=="Female":
            self.driver.find_element(By.XPATH, self.rdFemale_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMale_xpath).click()

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH, self.txtDateOfBirth_xpath).send_keys(dob)

    def setCompanyName(self,companyname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(companyname)

    def clickIsTaxExempt(self):
        self.driver.find_element(By.XPATH,self.cbIsTaxExempt_xpath).click()


    def selectNewsletter(self,newsletter):
        self.driver.find_element(By.XPATH, self.txtNewsletter_xpath).click()
        if newsletter=='Your store name':
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitmYourStoreName_xpath)
        else:
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitmTestStory2_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.lstitem)

    def setCustomerRole(self,role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        if role=='Register':
            self_lstitem=self.driver.find_element(By.XPATH,self.lstitmRegistered_xpath)
        elif role=='Administrators':
            self_lstitem = self.driver.find_element(By.XPATH, self.lstitmAdministtrator_xpath)
        elif role=='Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitmGuests_xpath)
        elif role=='Forum Moderators':
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitmForumModeraators_xpath)
        elif role=='Vendors':
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitmVendors_xpath)
        else:
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitmGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.lstitem)

    def setManagerOfVendor(self,value):
        # self.driver.find_elements(By.XPATH, self.lstitmVendors_xpath).click()
        drp=Select(self.driver.find_element(By.XPATH,self.drbMangerOfVendor_xpath))
        drp.select_by_value(value)

    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH,self.txtAdminComment_xpath).send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()







