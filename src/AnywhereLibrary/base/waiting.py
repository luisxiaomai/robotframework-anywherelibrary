#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0from keywordgroup import KeywordGroup
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException  
from time import sleep
from util import Util
from keywordgroup import KeywordGroup



class Waiting(KeywordGroup):

    # Public

    def wait_for_element_present(self,xpathLocator,timeout=30):
        """Waits until element specified with 'xpathlocator' present on current page.
            
        Fails if 'timeout' expires before the element appears.
        
        Default timeout is set to 10s, it can be used to override the default value.
            
        """
        try:
            WebDriverWait(Util.driver, float(timeout)).until(EC.presence_of_element_located((By.XPATH, xpathLocator)))
        except TimeoutException:
            self._warn("Wait for element '%s' timeout in '%s'"%(xpathLocator,float(timeout)))
            
    def wait_no_such_element_present(self,xpathLocator,timeout=30):
        """Waits until no element specified with 'xpathlocator' present on current page.
            
        Fails if 'timeout' expires before the element disappears.
        
        Default timeout is set to 10s, it can be used to override the default value.
        
            
        """
        try:
            WebDriverWait(Util.driver, float(timeout)).until_not(EC.presence_of_element_located((By.XPATH, xpathLocator)))
        except TimeoutException:
            self._warn("Wait until no such element '%s' timeout in '%s'"%(xpathLocator,float(timeout)))
            
   