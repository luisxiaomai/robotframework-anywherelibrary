#coding=utf-8
from util import Util

class ElementFinder(object):
   
    def __init__(self):
        self._strategies = {
            'class': self._find_by_class_name,
            'xpath': self._find_by_xpath
        }

    def find(self, locator):
        (prefix, criteria) = self._parse_locator(locator)
        if prefix is None:
            return self._find_by_xpath(criteria)
        else:
            strategy = self._strategies.get(prefix)
            if strategy is None:
                raise ValueError("Element locator with prefix '" + prefix + "' is not supported")
            return strategy(criteria)

    # Strategy routines, private

    def _parse_locator(self,locator):
        prefix = None
        criteria = locator
        if not locator.startswith('//'):
            locator_parts = locator.partition('=')
            if len(locator_parts[1]) > 0 and locator_parts[0].lower() in ["class","xpath"]:
                prefix = locator_parts[0].strip().lower()
                criteria = locator_parts[2].strip()
            elif len(locator_parts[1])==0:
                raise ValueError("Element locator(%s) is without '=' in your locator, wrong format"%locator)
        return (prefix, criteria)

    def _find_by_xpath(self,criteria):
        return Util.driver.find_elements_by_xpath(criteria)

    def _find_by_class_name(self,criteria):
        return Util.driver.find_elements_by_class_name(criteria)

class presence_of_element_located(object):
    """ An expectation for checking that an element is present on the DOM
    of a page. This does not necessarily mean that the element is visible.
    locator - used to find the element
    returns the WebElement once it is located
    """ 
    def __init__(self, locator):
        self.locator=locator

    def __call__(self,driver):
        return ElementFinder().find(self.locator)

