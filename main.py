# Please read the README, and feel free to follow the bot on Twitter @Carti_Bot

import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import tweepy
import time

# Tweet ever 5 hours
INTERVAL = 60 * 60 * 5

options = webdriver.ChromeOptions()

browser = webdriver.Chrome(ChromeDriverManager().install())


# Gets the randomized sentence
def get_sentence():

    browser.get("https://randomwordgenerator.com/sentence.php")

    generate_button = browser.find_element_by_name("submit")
    generate_button.click()
    sentence = browser.find_element_by_class_name("support-sentence")
    print(sentence.text)
    return sentence.text

# Gets the cartified sentence
def get_carti():

    sentence = get_sentence()
    browser.get("https://cartivoice.com")
    input_box = browser.find_element_by_id("userinput")
    input_box.send_keys(sentence)
    do_that_shit = browser.find_element_by_id("dothatshit")
    do_that_shit.click()
    carti_text = browser.find_element_by_id("cartitext").get_attribute("value")
    return carti_text

# Posts the tweet
def tweet():
    # Twitter API authorization keys are not included here on Github, since I wouldn't want anyone
    # doing nefarious things to my app :)
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)

    api.update_status(get_carti())

while True:
    tweet()
    time.sleep(INTERVAL)