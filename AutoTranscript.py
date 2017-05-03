from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class AutoTranscript (object):
    def __init__(self,username, password):
        self.username = username;
        self.password = password;
        self.driver = self.configureDriver()

    def configureDriver(self):
        ''' Allow Selenium to acces the Microphone'''    
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver


    def login(self):
        ''' Log into your Google account'''
        driver = self.driver

        driver.get('https://www.google.com/accounts/Login')
        driver.find_element_by_id("Email").send_keys(self.username)
        driver.find_element_by_id("next").click()
        time.sleep(1)
        driver.find_element_by_id("Passwd").send_keys(self.password)
        driver.find_element_by_id("signIn").click()

    def createGDoc(self, file_name):
        ''' Creates a new Gdoc file for trancription'''
        driver = self.driver

        driver.get('https://docs.google.com')
        new_doc = driver.find_element_by_id(':1d')
        new_doc.click()
        doc_title = driver.find_element_by_class_name('docs-title-input')
        doc_title.send_keys(file_name)
        doc_title.send_keys(Keys.ENTER)
        driver.find_element_by_id('docs-tools-menu').click()
        driver.find_element_by_class_name('docs-icon-mic').click()

    
    def startTranscribing(self):
        driver = self.driver

        record_botton = driver.find_element_by_class_name('docs-mic-control')
        record_botton.click()
        flag = 0

        while True:
            recording = None
            hearing = None
            

            try:
                recording = driver.find_element_by_class_name('docs-mic-control-recording')
                hearing = driver.find_element_by_class_name('docs-mic-control-hearing')
            except Exception:
                pass

            if hearing == None and recording == None:
                # It's not hearing nor recording
                print "All off"
                flag = 100
            elif hearing == None:
                # It's not hearing but recording
                print "Not hearing"
                flag += 1
                print flag
            else:
                # It's hearing and recording
                print "All Good"
                flag = 0
                
            
            if flag >= 7:
                record_botton.click()
                print 'Restarting All'
                flag = 0
                
            elif flag == 6:
                record_botton.click()
                record_botton.click()
                flag = 0
                print 'Restarting Hearing'

            time.sleep(0.5)
        



    def exit(self):
        self.driver.close()
