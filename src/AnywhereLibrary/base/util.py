#coding=utf-8

import os
from selenium import webdriver
from appium import webdriver as appiumdriver
from xml.etree import ElementTree as ET
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from keywordgroup import KeywordGroup
import AnywhereLibrary

class Util(KeywordGroup):
    driver=None
    platform = None     
    device = None    
    configtree=None
    captureScreenShot="False"

    def initial_driver(self,platform,captureScreenShot="False",device="common"):
        """ Initial Driver for specific platform according to the platform which you input.
   
        It's a pair with teardowndriver method.
                
        *platform* argument specifies the platfrom which you want to input.
        
        Possible values for platform are as follows:

        | firefox   |  
        | chrome    |
        | ie        | 
        | android---handle native android app where android device must be of API level 17 or higher.   |
        | selendroid---handle hybrid app or older android platforms |
        | ipad      | 
        | iphone    |

        *captureScreenShot* argument : trigger for deciding if to take captureScreenShot.
        
        *device* argument specify device like samsung, xiaomi,normally it dosen't need specify.
        
        Possible values for device are as follows: | samsung   |  
        
       *filepath* argument specify platform specific parameters stored path if env variable "ANYWHERE_LIBRARY_CONFIGURATION_FILE" is not set, default path is ".../Python27/Lib/site-packages/AnywhereLibrary/cfg/configuration.xml".
        
        Example:
        | initialDriver  | ${platform}  | 
        
        """
        Util.platform=platform.lower()
        Util.device=device
        Util.captureScreenShot=captureScreenShot
        if os.environ.get('ANYWHERE_LIBRARY_CONFIGURATION_FILE')!=None:
            configuration_file_path=os.environ['ANYWHERE_LIBRARY_CONFIGURATION_FILE']
        else:
            file_path=os.path.join(os.path.dirname(AnywhereLibrary.__file__),"cfg/configuration.xml")
            configuration_file_path=os.path.abspath(file_path)
        self._loadConfigFile(configuration_file_path)
        if Util.platform=='iphone':
            Util.driver = appiumdriver.Remote(
                                           command_executor=self._getPara('remote_server'),
                                           desired_capabilities={
                                           'deviceName':self._getPara('deviceName'),
                                           'platformName':self._getPara('platformName'),
                                           'platformVersion':self._getPara('platformVersion'),
                                           'app': self._getPara('app')
                                           })        
        elif Util.platform=='ipad':
            Util.driver = appiumdriver.Remote(
                                           command_executor=self._getPara('remote_server'),
                                           desired_capabilities={
                                           'deviceName': self._getPara('deviceName'),
                                           'platformName':self._getPara('platformName'),
                                           'platformVersion':self._getPara('platformVersion'),
                                           'app': self._getPara('app')
                                           })
        elif Util.platform=='android':
            Util.driver = appiumdriver.Remote(command_executor=self._getPara('remote_server'),
                                           desired_capabilities={
                                           'deviceName': self._getPara('deviceName'),
                                           'platformName':self._getPara('platformName'),
                                           'app': os.path.abspath(self._getPara('app')),
                                           'appPackage': self._getPara('appPackage'),
                                           'appActivity': self._getPara('appActivity')
                                           })
        elif Util.platform =='selendroid':
            Util.driver = appiumdriver.Remote(command_executor=self._getPara('remote_server'),
                                           desired_capabilities={
                                           'deviceName': self._getPara('deviceName'),
                                           'platformName':self._getPara('platformName'),
                                           'automationName': os.path.abspath(self._getPara('automationName')),
                                           'app': os.path.abspath(self._getPara('app')),
                                           'appPackage': self._getPara('appPackage'),
                                           'appActivity': self._getPara('appActivity')
                                           })

        elif Util.platform=='chrome':
            Util.driver=webdriver.Chrome()
            Util.driver.maximize_window()
            self.navigate_to_url(self._getPara('url'))
        elif Util.platform=='firefox':
            Util.driver=webdriver.Firefox()
            Util.driver.maximize_window()
            self.navigate_to_url(self._getPara('url'))
        elif Util.platform=='ie':
	    caps = DesiredCapabilities.INTERNETEXPLORER
            caps['ignoreProtectedModeSettings'] = True
            Util.driver=webdriver.Ie(capabilities=caps)
            Util.driver.maximize_window()
            self.navigate_to_url(self._getPara('url'))
       
    def switch_to_webview(self,index=1):
        """ Using this method before you do action of any web element in mobile. 

        *index* argument specifies which webview you want to switch.
        
        Example:
        | switch to webview  |
        """
        self._info('Current app contains below contexts(%s)'%Util.driver.contexts)
        if Util.platform=='iphone' or Util.platform=='ipad':
            Util.driver.switch_to.context('WEBVIEW_%s'%index)
        elif Util.platform=='selendroid':
            index=int(index)-1
            Util.driver.switch_to.context('WEBVIEW_%s'%index)
       
    def switch_to_native(self):
        """ Using this method before you do action of any native element in mobile. 
        
        Example:
        | switch to native  |
        """
        self._info('Current app contains below contexts(%s)'%Util.driver.contexts)
        if Util.platform=='iphone' or Util.platform=='ipad':
            Util.driver.switch_to.context('NATIVE_APP')
        elif Util.platform=='selendroid':
            Util.driver.switch_to.context('NATIVE_APP')    
    
    def navigate_to_url(self,url):
        """ Using this method if you want to navigate to specified url. 

        In device, the keyword is available for navigate to url in webview.

        *captureScreenShot* argument : the specified url you want to navigated to.

        Example:
        | switch to native  |
        """
        self._info('Navigate to url %s'%url)
        if Util.platform in ['chrome','firefox','ie']:
            self.driver.get(url)
        elif Util.platform in ['iphone','ipad','android','selendroid']:
            self.switch_to_webview()
            self.driver.execute_script('document.location.href=arguments[0]',url) 

    def _loadConfigFile(self,filepath):
        try:
            filepath = os.path.abspath(filepath)
            Util.configtree = ET.fromstring(open(filepath).read())
        except:
            raise EnvironmentError('Loading configuration file failed ')                  
    
    def _getPara(self,paraname):
        lst_node = Util.configtree.iterfind('.//platform[@name="%s"]/para'%Util.platform)
        for child in lst_node:
            if child.attrib['name']==paraname:
                return child.attrib['value']
                break
        else:
            raise EnvironmentError('Can not find related para "%s" in "%s" node of configration file '%(paraname,Util.platform))

    def tear_downDriver(self):
        """ Tear down Driver is just quit current driver after finishing test cases execution.
        
        It's a pair with initialdriver method, recommend putting these two functions before/after to each test cases.
      
        Example:
        | tearDownDriver  |
        """
        Util.driver.quit()
        
