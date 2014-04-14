AnywhereLibrary for robotframework
==========

##Introduction

AnywhereLibrary is a cross platform(desktop browser,android,ios) testing library for Robot Framework that leverages the [Selenium 2(WebDriver)](<http://seleniumhq.org/docs/03_webdriver.html/>) libraries internally to control a web browser and [appium](<http://appium.io/>) as mobile test automation framework for use with native and hybrid app. 

This library is specially suitable for handling [SPA(single-page apps)](http://en.wikipedia.org/wiki/Single-page_application) with responsive design pattern. WIth this you only need generate a set of scripts to cover all platform(desktop browser ,android,ios). 

##Installation

The recommended installation method is using pip:
	
	pip install robotframework-anywherelibrary

##Directory Layout

doc/
    Keyword documentation
    
sample-code/
	A sample test case which can run in desktop browser, sample android and ios webview app with different platform parameter input.

src/base
    Python source code
    
src/cfg
	Confuguration file which stores all parameters for initialling driver

##Usage

To write tests with Robot Framework and AnywhereLibrary, 
AnywhereLibrary must be imported into your RF test suite.
See [Robot Framework User Guide](https://code.google.com/p/robotframework/wiki/UserGuide) for more information.

As it uses Appium for mobile solution, please make sure your Appium server is up and running.
For how to use Appium please refer to [Appium Documentation](http://appium.io/getting-started.html).

Before test case you must using *'Initial Driver'* keyword with platfrom value as paramter input, after test case you must using *'Tear Down Driver'* keyword to tear down related driver. Also you need do some modification in *`configuration.xml`* file in *`/AnywhereLibrary/cfg`*.

##Run sample case
	$ pybot --variable platform:chrome webviewTest.txt
	
##Documentation
* keyword glance

	- `Initial Driver`
	- `Tear Down Driver`
	- `click`
	- `type`
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

##FAQ

##License
MIT

