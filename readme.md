#AnywhereLibrary for robotframework

##Introduction

AnywhereLibrary is a cross platform(desktop browser,android,ios) testing library for Robot Framework that leverages the [Selenium 2(WebDriver)](<http://seleniumhq.org/docs/03_webdriver.html/>) libraries internally to control a web browser and [appium](<http://appium.io/>) as mobile test automation framework for use with native and hybrid app. 

This library is specially suitable for handling [SPA(single-page apps)](http://en.wikipedia.org/wiki/Single-page_application) with responsive design pattern. WIth this you only need generate a set of scripts to cover all platform(desktop browser ,android,ios). 

On the other hand, no any UI test automation framework is made for your real business. If this library can't be suitable for your business, it's highly recommed that you can fork this repository as your prototype for UI test automation. According to your real business requirements to customize your own anywherelibrary.

##Installation

The recommended installation method is using [pip](http://www.pip-installer.org/en/latest/):
	
	pip install robotframework-anywherelibrary

##Directory Layout

####doc/
>Keyword documentation.
    
####sample-code/
>A sample test case which can run in desktop browser, sample android and ios webview app with different platform parameter input.

####src/base
>Python source code.
    
####src/cfg
>Confuguration file which stores all parameters for initialling driver.

##Usage

To write tests with Robot Framework and AnywhereLibrary, 
AnywhereLibrary must be imported into your RF test suite.
See [Robot Framework User Guide](https://code.google.com/p/robotframework/wiki/UserGuide) for more information.

As it uses Appium for mobile solution, please make sure your Appium server is up and running.
For how to use Appium please refer to [Appium Documentation](http://appium.io/getting-started.html).

#####Before test case
You must using *'Initial Driver'* keyword with platfrom value as paramter input, after test case you must      using *'Tear Down Driver'* keyword to tear down related driver. Also you need do some modification in *`configuration.xml`* file in *`/AnywhereLibrary/cfg`*.

#####Locating elements

All keywords in AnywhereLibrary that need to find an element on the page take an argument, `locator`.  AnywhereLibrary support a subset of the WebDriver locator strategies.Currently available locator strategies are using:
    
    find by "class" (i.e., ui component type)
    find by "xpath" (i.e., an abstract representation of a path to an element, with certain constraints)
Supported strategies are:

    | *Strategy* | *Example*                               | *Description*                                |
    | xpath      | Click `|` //div[@id='my_element']       | Matches with arbitrary XPath expression      |
    | xpath      | Click `|` xpath=//div[@id='my_element'] | Matches with arbitrary XPath expression      |
    | class      | Click `|` class=android.widget.Button   | Matches another element by their class name  |
    | ......     | Coming soon ......                      | Coming soon.....                             |
     
##Run sample case
	$ pybot --variable platform:chrome webviewTest.txt
	$ pybot --variable platform:firefox webviewTest.txt
	$ pybot --variable platform:iphone webviewTest.txt
	
##Documentation
* keyword glance

	- `Initial Driver`
	- `Tear Down Driver`
	- `Click`
	- `Type`
	- `Element Find`
	- `Get Text`
	- `Get Value`
	- `Verify Text`
	- `Verify Value`
	- `Is Element Present`
	- `Page Should Contain Element`
	- `Page Should Not Contains Element`
	- `Wait For Element Present`
	- `Wait No Such Element Present`
	- `Switch To Native`
	- `Switch To Webview`
	- `Capture Page Screenshot`
	- `Execute Javascript`
* mobile gestures
	- `Coming Soon...`
	
	
More details about keyword documentation could be found at [Keyword Documentation](http://luisxiaomai.github.io/robotframework-anywherelibrary/doc/AnywhereLibraryDocument.html>)

##Plan
* AnywhereLibrary 1.1.0 version which is mainly adapt to appium 1.0(In process).
* Add more locator strategy.



##FAQ

##License
MIT

