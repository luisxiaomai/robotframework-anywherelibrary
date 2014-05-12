from base import *
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
execfile(os.path.join(THIS_DIR, 'version.py'))

__version__ = VERSION

class AnywhereLibrary(
    Element, 
    Util,
    Logging,
    RunOnFailure,
    Screenshot,
    Waiting,
    JavaScript,
):
    """AnywhereLibrary is a cross platform(desktop browser,android,ios) testing library for Robot Framework.

    It uses the Selenium 2 (WebDriver) libraries internally to control a web browser.
    See http://seleniumhq.org/docs/03_webdriver.html for more information on Selenium 2
    and WebDriver. 

    It uses appium as mobile test automation framework for use with native and hybrid app.
	See http://appium.io/.
	
	Best practice for using this library is for SPA(single page application) with design pattern which means you only need a set of scripts to cover all platform.
	
    *Before running tests*

    Prior to running test cases using AnywhereLibrary, AnywhereLibrary must be
    imported into your Robot test suite , and the `Initial Driver` keyword must
     be used to initial a driver to the desired location and `Tear Down Driver` driver after finishing executing test cases(see `initial driver`,`teardown driver` keyword).

    *Locating elements*

    All keywords in AnywhereLibrary that need to find an element on the page
    take an argument, `locator`.  AnywhereLibrary support a subset of the WebDriver locator strategies:
    currently available locator strategies are using:

    find by *"class"* (i.e., ui component type)
    
    find by *"xpath"* (i.e., an abstract representation of a path to an element, with certain constraints)

    Supported strategies are:

    | *Strategy* | *Example*                               | *Description*                                |
    | xpath      | Click `|` //div[@id='my_element']       | Matches with arbitrary XPath expression      |
    | xpath      | Click `|` xpath=//div[@id='my_element'] | Matches with arbitrary XPath expression      |
    | class      | Click `|` class=android.widget.Button   | Matches another element by their class name  |
    | ......     | Coming soon ......                      | Coming soon.....                             |
     
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION
    


    def __init__(self,run_on_failure='Capture Page Screenshot'):
        """
        | Library `|` AnywhereLibrary   | # Import library into where you will use |
        """
        for base in AnywhereLibrary.__bases__:
            base.__init__(self)
        self.register_keyword_to_run_on_failure(run_on_failure)
    
