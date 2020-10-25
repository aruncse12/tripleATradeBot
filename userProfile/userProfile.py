from eventLogger import eventLogger as logger
from pathList import pathList
from alice_blue import *    
import openpyxl

class userProfile:
    userProfileWorkBook=""
    profileName=""
    userName = ""
    password = ""
    apiSecret = ""
    accessToken = ""
    aliceObj = ""
    exchangeList = ['NSE']
    def __init__(self, profileName):
        self.userProfileWorkBook = openpyxl.load_workbook(pathList.userProfileFileName)
        self.profileName = profileName
        self.userName = self.userProfileWorkBook.get_sheet_by_name(self.profileName)['A1'].value
        self.password = self.userProfileWorkBook.get_sheet_by_name(self.profileName)['A2'].value
        self.apiSecret = self.userProfileWorkBook.get_sheet_by_name(self.profileName)['A3'].value

        logger.info(self.userName)
        logger.info(self.password)
        logger.info(self.apiSecret)
        
    def login(self):
        logger.info("login")
        self.accessToken =  AliceBlue.login_and_get_access_token(username=self.userName, password=self.password, twoFA='a',  api_secret=self.apiSecret)
        self.aliceObj = AliceBlue(username=self.userName, password=self.password, access_token=self.accessToken, master_contracts_to_download=self.exchangeList)
    
    def profileData(self):
        logger.info("profileData")
        print (self.aliceObj.get_profile())
        print (self.aliceObj.get_balance())
