import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import tweepy
import time
from os import environ

# The Twitter API keys are in my Heroku environment variables
# since I don't want them public on Github
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# Path variables for Heroku to access Chromedriver
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google_chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"

# Tweet ever 5 hours
INTERVAL = 15

options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

options.binary_location = GOOGLE_CHROME_PATH

# If running the script on a local machine
# uncomment the line below and remove the chrome path variables
#browser = webdriver.Chrome(ChromeDriverManager().install())

browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
chrome_options=options)

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
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)

    api.update_status(get_carti())

while True:
    tweet()
    time.sleep(INTERVAL)