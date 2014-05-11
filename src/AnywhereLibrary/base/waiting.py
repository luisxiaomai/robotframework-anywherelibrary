#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from AnywhereLibrary.base import elementfinder as EC
from keywordgroup import KeywordGroup
from selenium.common.exceptions import TimeoutException  
from util import Util

class Waiting(KeywordGroup):

   
    # Public

    def wait_for_element_present(self,locator,timeout=30):
        """Waits until element specified with 'locator' present on current page.
            
        Fails if 'timeout' expires before the element appears.
        
        Default timeout is set to 10s, it can be used to override the default value.
            
        """
        try:
            WebDriverWait(Util.driver, float(timeout)).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self._warn("Wait for element '%s' timeout in '%s'"%(locator,float(timeout)))
            
    def wait_no_such_element_present(self,locator,timeout=30):
        """Waits until no element specified with 'locator' present on current page.
            
        Fails if 'timeout' expires before the element disappears.
        
        Default timeout is set to 10s, it can be used to override the default value.
        
            
        """
        try:
            WebDriverWait(Util.driver, float(timeout)).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self._warn("Wait until no such element '%s' timeout in '%s'"%(locator,float(timeout)))
            
   