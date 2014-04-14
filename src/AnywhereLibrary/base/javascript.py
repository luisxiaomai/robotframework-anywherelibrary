#coding=utf-8
import os
from selenium.common.exceptions import WebDriverException
from keywordgroup import KeywordGroup
from util import Util


class JavaScript(KeywordGroup):
   
    # Public 
     def execute_javascript(self,code,*args):
        """Executes the given JavaScript code.

        `code`  The JavaScript to execute.It may contain multiple lines of code.
        
        `args` Any applicable argument for your JavaScript.
        
        """
        self._info("Executing JavaScript:\n%s" % code)
        return Util.driver.execute_script(code,*args)
       