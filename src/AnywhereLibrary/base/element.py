#coding=utf-8
from util import Util
from keywordgroup import KeywordGroup
from elementfinder import ElementFinder

class Element(KeywordGroup):

    def __init__(self):
        self._element_finder=ElementFinder()

    # Public
    def element_find(self,locator,requireRaise=True):
        """ General function to find single element, it will return this element.
        
        If it matchs more than one element, it will return the first one.
                
        *requireRaise* argument normally is not required.
        
        Example:
        | ${Element}= | Element Find | ${element_locator}   |
        
        """
        
        element=self._element_finder.find(locator)
        if not requireRaise and len(element)==0:
            return None
        if requireRaise and len(element)==0:
            raise ValueError("Element locator '%s' did not match any element."%locator)
        return element[0]        

    def click(self,locator):
        """ General click function which can be used for all platforms' elements.
                
        Example:
        | click | ${element_locator}  |
        
        """
        self._info("Clicking element '%s'." %locator)
        self.wait_for_element_present(locator,10)
        element=self.element_find(locator)
        element.click()
        if Util.captureScreenShot=="True":
            self.capture_page_screenshot()

    def type(self,locator,text):
        """General function for typing the given text into text field control.
                
        *text* argument specifies the text which you want to input.

        Example:
        | type | ${element_locator} | ${Text}  |
        """
        self._info("Typing text '%s' into text field '%s'" % (text, locator))
        self.wait_for_element_present(locator,10)
        self._input_text_into_text_field(locator, text)
        if Util.captureScreenShot=="True":
            self.capture_page_screenshot()
            
    def is_element_present(self,locator):
        """Return true or false if element presents in current page.
        """
        return (self.element_find(locator,False) != None)
        
    def page_should_contain_element(self,locator):
        """Verifies that current page contains element.
        """
        if self.is_element_present(locator):
            self._info('Current page contains element with locator %s'%locator)
        else:
            self._warn('Current page should not contain element with locator %s'%locator)


    def page_should_not_contain_element(self,locator):
        """Verifies that current page should not contain element.
        """
        if not self.is_element_present(locator):
            self._info('Current page should not contain element with locator %s'%locator)
        else:
            self._warn('Current page contains element with locator %s'%locator)
            
    def get_matching_element_count(self, locator):
        """Returns number of elements matching `locator`

        """
        count = len(self._element_finder.find(locator))
        return str(count)
           
    def get_text(self,locator):
        """Returns the text value of element identified by `locator`.
        """
        return self._get_text(locator)
    
    def get_value(self,locator):
        """Returns the value attribute of element identified by `locator`.
        """
        return self._get_value(locator)
    
    def verify_text(self,locator,expectedText):
        """Compare the expectedText given to the actualText which get from the element.
                               
       *expectedText* argument specifies the expectedtext you want.
        
         Example:
        | Verify text  | ${element_locator}  | ${text}  |
        
        """
        try:
            actualText=self._get_text(locator)
            assert actualText==expectedText
            self._info('Compare actual text(%s) with expected text(%s) passed'%(actualText,expectedText))
        except AssertionError:
            self._warn('Compare actual text(%s) with expected text(%s) failed'%(actualText,expectedText))
            
    def verify_value(self,locator,expectedValue):
        """Compare the expectedValue given to the actualValue which get from the element
                
        *expectedValue* argument specifies the expectedValue you want.
        
        Example:
        | Verify value  | ${element_locator}  | ${value}  |
        """
        try:
            actualValue=self._get_value(locator)
            assert actualValue==expectedValue
            self._info('Compare actual value(%s) with expected value(%s) passed'%(actualValue,expectedValue))
        except AssertionError:
            self._warn('Compare actual value(%s) with expected value(%s) failed'%(actualValue,expectedValue))
            
    def ie_certificate_error_handler(self):
        Util.driver.get(('javascript:document.getElementById("overridelink").click()'))   
        
    # Private
    def _input_text_into_text_field(self, locator, text):
        element = self.element_find(locator)
        element.send_keys(text)
            
    def _get_text(self,locator):
        element=self.element_find(locator)
        return (element.text).strip()
    
    def _get_value(self,locator):
        element=self.element_find(locator)
        return (element.get_attribute("value")).strip()

  

   