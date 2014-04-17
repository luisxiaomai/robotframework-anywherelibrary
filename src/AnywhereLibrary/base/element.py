#coding=utf-8
from util import Util
from keywordgroup import KeywordGroup
from selenium.webdriver.common.by import By

class Element(KeywordGroup):
   
    # Public

    def click(self,xpathLocator):
        """ General click function which can be used for all platforms' elements.
        
        *xpathLocator* argument specifies the element's xpath.
        
        Example:
        | click | ${element_xpath}  |
        
        """
        self._info("Clicking element '%s'." %xpathLocator)
        self.wait_for_element_present(xpathLocator,10)
        element=self.element_find(xpathLocator)
        self.element_find(xpathLocator).click()
        if Util.captureScreenShot=="True":
            self.capture_page_screenshot()


    def element_find(self,xpathLocator,requireRaise=True):
        """ General function to find single element, it will return this element.
        
        If it matchs more than one element, it will return the first one.
        
        *xpathLocator* argument specifies the elements' xpath.
        
        *requireRaise* argument normally is not required.
        
        Example:
        | ${Element}= | Element Find | ${Element_xpath}   |
        
        """
        element=Util.driver.find_elements(by="xpath", value=xpathLocator)
        if not requireRaise and len(element)==0:
            return None
        if requireRaise and len(element)==0:
            raise ValueError("Element locator '%s' did not match any element."%xpathLocator)
        return element[0]        
   
    def type(self,xpathLocator,text):
        """General function for typing the given text into text field control.
        
        *xpathLocator* argument specifies the element's xpath.
        
        *text* argument specifies the text which you want to input.

        Example:
        | type | ${element_xpath} | ${Text}  |
        """
        self._info("Typing text '%s' into text field '%s'" % (text, xpathLocator))
        self.wait_for_element_present(xpathLocator,10)
        self._input_text_into_text_field(xpathLocator, text)
        if Util.captureScreenShot=="True":
            self.capture_page_screenshot()
            
    def is_element_present(self,xpathLocator):
        """Return true or false if element presents in current page.
        """
        return (self.element_find(xpathLocator,False) != None)
        
    def page_should_contain_element(self,xpathLocator,errorMessage=None):
        """Verifies that current page contains element.
        """
        if self.is_element_present(xpathLocator):
            self._info('Current page contains element with xpathlocator %s'%xpathLocator)
        else:
            if errorMessage is not None:
                self._error(errorMessage)
            else:
                self._error('Current page does not contain element with xpathlocator %s'%xpathLocator)


    def page_should_not_contain_element(self,xpathLocator,errorMessage=None):
        """Verifies that current page should not contain element.
        """
        if not self.is_element_present(xpathLocator):
            self._info('Current page should not contain element with xpathlocator %s'%xpathLocator)
        else:
            if errorMessage is not None:
                self._error(errorMessage)
            else:
                self._error('Current page contains element with xpathlocator %s'%xpathLocator)
            
    def get_matching_xpath_count(self, xpathLocator):
        """Returns number of elements matching `xpath`

        """
        count = len(self.elements_find(xpathLocator))
        return str(count)
           
    def get_text(self,xpathLocator):
        """Returns the text value of element identified by `xpathLocator`.
        """
        
        return self._get_text(xpathLocator)
    
    def get_value(self,xpathLocator):
        """Returns the value attribute of element identified by `xpathLocator`.
        """
        return element._get_value(xpathLocator)
    
    def verify_text(self,xpathLocator,expectedText):
        """Compare the expectedText given to the actualText which get from the element.
                        
       *xpathLocator* argument specifies the element's xpath.
       
       *expectedText* argument specifies the expectedtext you want.
        
         Example:
        | Verify text  | ${element_xpath}  | ${text}  |
        
        """
        try:
            actualText=self._get_text(xpathLocator)
            assert actualText==expectedText
            self._info('Compare actual text(%s) with expected text(%s) passed'%(actualText,expectedText))
        except AssertionError, e:
            self._warn('Compare actual text(%s) with expected text(%s) failed'%(actualText,expectedText))
            
    def verify_value(self,xpathLocator,expectedValue):
        """Compare the expectedValue given to the actualValue which get from the element
        
        *xpathLocator* argument specifies the element's xpath.
        
        *expectedValue* argument specifies the expectedValue you want.
        
        Example:
        | Verify value  | ${element_xpath}  | ${value}  |
        """
        try:
            actualValue=self._get_value(xpathLocator)
            assert actualValue==expectedValue
            self._info('Compare actual value(%s) with expected value(%s) passed'%(actualValue,expectedValue))
        except AssertionError, e:
            self._warn('Compare actual value(%s) with expected value(%s) failed'%(actualValue,expectedValue))
            
    def ie_certificate_error_handler(self):
        Util.driver.get(('javascript:document.getElementById("overridelink").click()'))   
        
    # Private
    def _input_text_into_text_field(self, xpathLocator, text):
        element = self.element_find(xpathLocator)
        element.send_keys(text)
            
    def _get_text(self,xpathLocator):
        element=self.element_find(xpathLocator)
        return (element.text).strip()
    
    def _get_value(self,xpathLocator):
        element=self.element_find(xpathLocator)
        return (element.get_attribute("value")).strip()

  

   