from bs4 import BeautifulSoup as bs
from requests import get
from os.path import isdir

class Username:
    def __init__(self,username):
        self.username = username.lower()
        self.url = "https://t.me/{}".format(username)
        response = get(self.url)
        content = response.content.decode()
        self.page = bs(content,"html.parser")

    def getType(self):
        button_label = self.page.find("a" , "tgme_action_button_new")
        button_label = button_label.text

        if "View in Telegram" in button_label:
            members = self.page.find("div", "tgme_page_extra")
            members = members.text

            if "online" in members:
                return "Group"
            else:
                return "Channel"
            
        elif "Send Message" in button_label:
            if self.username[-3:] == "bot":
                return "bot"
            else:
                return "Personal Account"
        return "Unknow Type"
    def getMembers(self):
        if self.getType() == "Channel":
            members = self.page.find("div" , "tgme_page_extra")
            members = members.text.replace(" members", "")
            members = members.replace(" ","")
            return int(members)
        elif self.getType() == "Group":
            members = self.page.find("div" , "tgme_page_extra")
            mnum = members.text.split(",")[0]
            members = mnum.replace(" members","")
            members = members.replace(" ","")
            return int(members)
        else:
            return None
    def getBio(self):
        bio = self.page.find("div" , "tgme_page_description")
        bio = bio.text
        return bio
    def getProfilePhoto(self,path="."):
        img = self.page.find("img" , "tgme_page_photo_image")
        link = img.attrs["src"]
        photo = get(link)
        if isdir(path):
            path = path+"/{}".format(self.username)
        file = open(path , "wb")
        file.write(photo.content)
        file.close()
        
    
        
