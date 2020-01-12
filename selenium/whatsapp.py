#Simple bot to reply whatsapp messages

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import time

IMAGE_RESPONSE = "nice pic"

def be_responsive(message,group_name):
    #open chrome browser and go to web whatsapp page
    chrome = webdriver.Chrome()
    chrome.get("https://web.whatsapp.com")
    sleep(10)
    chat = chrome.find_element_by_xpath('//*[@title = "{}"]'.format(group_name))
    chat_name = chat.get_attribute('title')

    chat.click()
    sleep(3)
    text_box = chrome.find_element_by_xpath('//*[@contenteditable = "true"]')
    text_box.click()
    sleep(1)
    last_text = ""
    try:
        while True:
            messages_received = chrome.find_elements_by_class_name("message-in")
            last_message = messages_received[len(messages_received) - 1]
            data_author_class = last_message.find_element_by_class_name("copyable-text")
            data_author =  data_author_class.get_attribute('data-pre-plain-text')
            author = data_author.split(']')[1].split(':')[0].split()[]

            try:
                text = last_message.find_element_by_class_name("selectable-text")
                text = text.text
                if(text != last_text):
                    last_text = text
                    text_box.send_keys(message)
                    text_box.send_keys(Keys.ENTER)
            except:
                pass

            sleep(2)
    finally:
        chrome.close()

def main():
    afk_message = "Too busy, sorry"
    be_responsive(afk_message,"Test_contact)

main()
