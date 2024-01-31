from selenium.webdriver.common.by import By


class SearchCustomer:
    txtEmail_xpath="//input[@name='SearchEmail']"
    txtFirstName_xpath="//input[@name='SearchFirstName']"
    txtLastName_xpath="//input[@name='SearchLastName']"
    btnSearch_id="search-customers"
    tablepath_xpath="//table[@id='customers-grid']"
    tablerow_xpath="//table[@id='customers-grid']/tbody/tr"
    tablecolumn_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setFirstName(self,Fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(Fname)

    def setLastName(self,Lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(Lname)

    def clickSearch(self):
        self.driver.find_element(By.ID,self.btnSearch_id).click()

    def getRowCount(self):
        return len(self.driver.find_elements(By.XPATH,self.tablerow_xpath))

    def getColumnCount(self):
        return len(self.driver.find_elements(By.XPATH,self.tablecolumn_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getRowCount()+1):
            table=self.driver.find_element(By.XPATH,self.tablepath_xpath)
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getRowCount()+1):
            table = self.driver.find_element(By.XPATH, self.tablepath_xpath)
            name = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name==Name:
                flag=True
                break
        return flag
    





