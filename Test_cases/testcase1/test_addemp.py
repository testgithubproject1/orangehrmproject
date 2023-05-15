import time
import time

from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from Test_cases.pageObjects.AddEmp_Page import AddEmployee
from Test_cases.pageObjects.LoginPage import loginpage


class Test_Add_Emp:


    def test_addEmp_003(self, setup):
        self.driver = setup
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName("Admin")
        self.lp.Enter_Password("admin123")
        self.lp.Click_Login()
        self.ae = AddEmployee(self.driver)
        self.ae.Click_PIM()
        self.ae.Click_Add()
        time.sleep(2)
        self.ae.Enter_FirstName("Credence")
        self.ae.Enter_MiddleName("It")
        self.ae.Enter_LastName("Pune")
        time.sleep(2)
        self.ae.Click_Save()
        if self.ae.Add_Employee_stuats() == True:
            time.sleep(2)
            self.lp.Click_MenuButton()
            self.lp.Click_Logout()
            assert True
        else:
            assert False
        self.driver.close()

#
    # def test_addEmp_003(self, setup):
    #     self.driver = setup
    #     # driver = webdriver.Firefox()
    #     # driver.implicitly_wait(10)
    #     # driver.get("https://opensource-demo.orangehrmlive.com/")
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    #     self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    #     self.driver.find_element(By.XPATH,
    #                              "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space("
    #                              ")='PIM']").click()
    #     self.driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Credence")
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Credence")
    #     self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Credence")
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    #     try:
    #         self.driver.find_element(By.XPATH, "//h6[normalize-space()='Personal Details']")
    #         print("test_addEmp_002 is Passed")
    #         self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
    #         self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    #         addemp = True
    #     except Ec:
    #         print("test_addEmp_002 is Failed")
    #         print("test_addEmp_002 is completed")
    #         addemp = False
    #
    #     if addemp == True:
    #         assert True
    #     else:
    #         assert False
    #     self.driver.close()
