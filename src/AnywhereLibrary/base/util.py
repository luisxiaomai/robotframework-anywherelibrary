#coding=utf-8

import os
import time
import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException  
from selenium.common.exceptions import WebDriverException 
from xml.etree import ElementTree as ET
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import AnywhereLibrary

class Util():
    driver=None
    platform = None    
    device = None    
    xpathmap={}
    configtree=None
    captureScreenShot="False"

    
    #self.driver.implicitly_wait(20)
     
    def __init__(self):
        '''
        Constructor
    
        '''
    @staticmethod
    def initialDriver(platform,captureScreenShot="False",device="common"):
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
        Util.platform=platform
        Util.device=device
        Util.captureScreenShot=captureScreenShot
        if os.environ.get('ANYWHERE_LIBRARY_CONFIGURATION_FILE')!=None:
            configuration_file_path=os.environ['ANYWHERE_LIBRARY_CONFIGURATION_FILE']
        else:
            file_path=os.path.join(os.path.dirname(AnywhereLibrary.__file__),"cfg/configuration.xml")
            configuration_file_path=os.path.abspath(file_path)
        Util._loadConfigFile(configuration_file_path)
        if platform=='iphone':
            Util.driver = webdriver.Remote(
                                           command_executor=Util._getPara('remote_server'),
                                           desired_capabilities={
                                           'browserName': '',
                                           'device':Util._getPara('device'),
                                           #'platform': 'Mac',
                                           #'version': '6.1',
                                           'app': Util._getPara('app')
                                           })        
        elif platform=='ipad':
            Util.driver = webdriver.Remote(
                                           command_executor=Util._getPara('remote_server'),
                                           desired_capabilities={
                                           'browserName': '',
                                           'device': Util._getPara('device'),
                                           #'platform': 'Mac',
                                           #'version': '6.1',
                                           'app': Util._getPara('app')
                                           })
        elif platform in ['selendroid','android']:
            Util.driver = webdriver.Remote(command_executor=Util._getPara('remote_server'),
                                           desired_capabilities={
                                           'device': Util._getPara('device'),
                                           'app': os.path.abspath(Util._getPara('app')),
                                           #C:\\Users\\I072687\\Desktop\\workspace\\Anywhere\\app\\SAPAnywhereAndroid.apk
                                           #'app': '/Users/I072687/appium/app/SAPAnywhereAndroid.apk',
                                           #'app': "http://10.58.80.194:8081/store/anw/SAPAnywhereAndroid.apk",
                                           'app-package': Util._getPara('app-package'),
                                           'app-activity': Util._getPara('app-activity')
                                           })
        elif platform=='chrome':
            Util.driver=webdriver.Chrome()
            Util.driver.maximize_window()
            Util.driver.get(Util._getPara('url'))
        elif platform=='firefox':
            Util.driver=webdriver.Firefox()
            Util.driver.maximize_window()
            Util.driver.get(Util._getPara('url'))           
        elif platform=='ie':
	    caps = DesiredCapabilities.INTERNETEXPLORER
            caps['ignoreProtectedModeSettings'] = True
            Util.driver=webdriver.Ie(capabilities=caps)
            Util.driver.maximize_window()
            Util.driver.get(Util._getPara('url'))
       
    @staticmethod      
    def switch_to_webview():
        """ Using this method before you do action of any web element in mobile. 
        
        Example:
        | switch to webview  |
        """
        if Util.platform=='iphone' or Util.platform=='ipad':
            handle=Util.driver.window_handles[0]
            Util.driver.switch_to_window(handle)
            #for handle in self.driver.window_handles:
            #self.driver.switch_to_window(handle)
        elif Util.platform=='selendroid':
            Util.driver.switch_to_window('WEBVIEW')
    
    @staticmethod    
    def switch_to_native():
        """ Using this method before you do action of any native element in mobile. 
        
        Example:
        | switch to native  |
        """
        if Util.platform=='iphone' or Util.platform=='ipad':
            Util.driver.execute_script('mobile: leaveWebView')
        elif Util.platform=='selendroid':
            Util.driver.switch_to_window('NATIVE_APP')    
    
          
    @staticmethod
    def _loadConfigFile(filepath):
        try:
            filepath = os.path.abspath(filepath)
            Util.configtree = ET.fromstring(open(filepath).read())
        except:
            raise EnvironmentError('Loading configuration file failed ')                  
    
    @staticmethod
    def _getPara(paraname):
        lst_node = Util.configtree.iterfind('.//platform[@name="%s"]/para'%Util.platform)
        for child in lst_node:
            if child.attrib['name']==paraname:
                return child.attrib['value']
                break
        else:
            raise EnvironmentError('Can not find related para "%s" in "%s" node of configration file '%(paraname,Util.platform))

    @staticmethod
    def tearDownDriver():
        """ Tear down Driver is just quit current driver after finishing test cases execution.
        
        It's a pair with initialdriver method, recommend putting these two functions before/after to each test cases.
      
        Example:
        | tearDownDriver  |
        """
        Util.driver.quit()
        
