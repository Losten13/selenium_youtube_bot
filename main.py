import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import bruteforce

email = "sample@gmail.com"
password = "samplepassword"
video_url = "https://www.youtube.com/watch?v=zwpEBGOv6Nc&t=5s"
predicts = bruteforce.get_predict()
nicknames = bruteforce.read_nick()
youtube_accounts = bruteforce.read_youtube_acc('youtube.txt')

driver = webdriver.Chrome()
driver.fullscreen_window()
driver.get("https://accounts.google.com/ServiceLogin?passive=true&service=youtube&uilel=3&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fnext%3D%252F%26hl%3Duk%26app%3Ddesktop%26action_handle_signin%3Dtrue&hl=uk")


def login(email, password):
    input_email = driver.find_element_by_xpath("//*[@id='identifierId']")
    input_email.send_keys(email)

    time.sleep(5)
    button = driver.find_element_by_xpath("//*[@id='identifierNext']")
    button.click()
    time.sleep(5)

    input_pass = driver.find_element_by_xpath(
        "//*[@id='password']/div[1]/div/div[1]/input")
    input_pass.send_keys(password)

    button = driver.find_element_by_xpath("//*[@id='passwordNext']")
    button.click()
    time.sleep(5)


def comment_video(video_url, predict):

    driver.get(video_url)
    time.sleep(5)
    element = driver.find_element_by_xpath("//*[@id='movie_player']")
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)
    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(5)

    button = driver.find_element_by_xpath("//*[@aria-label='Reply']")
    button.click()
    time.sleep(5)

    input_predict = driver.find_element_by_xpath(
        "//*[@contenteditable='true' and @aria-label='Add a public reply...' ]")
    time.sleep(3)
    input_predict.send_keys(predict)
    time.sleep(3)

    button = driver.find_element_by_xpath("//*[@id='submit-button']")
    button.click()
    time.sleep(2)


def create_acc(nickname):
    time.sleep(5)

    button = driver.find_element_by_xpath("//*[@id='avatar-btn']")
    button.click()
    time.sleep(1)
    button = driver.find_elements_by_xpath("//*[@href='/account']")[1]
    button.click()
    time.sleep(5)

    button = driver.find_element_by_xpath(
        "//*[@id='creator-page-content']/div/div[2]/div[2]/a")
    button.click()
    time.sleep(10)

    nickname_available = True
    try:
        driver.find_element_by_link_text(nickname)
    except NoSuchElementException as exception:
        nickname_available = False
    if nickname_available:
        return False
    else:
        button = driver.find_element_by_xpath(
            "//*[@id='ytcc-existing-channels']/li[1]/a")
        button.click()
    time.sleep(5)
    input_nick = driver.find_element_by_xpath("//*[@id='PlusPageName']")
    input_nick.send_keys(nickname)
    time.sleep(5)
    button = driver.find_element_by_xpath("//*[@id='submitbutton']")
    button.click()


def change_chanenl(nickname):
    driver.get(
        "https://www.youtube.com/channel_switcher?next=%2Faccount&feature=settings")
    time.sleep(3)

    button = driver.find_element_by_xpath(
        "//*[contains(text(), '" + nickname + "')]/../../../..")

    button.click()


def main():
    print(predicts)
    login(email, password)

    for i in range(len(nicknames)):
        time.sleep(5)
        change_chanenl(nicknames[i])
        comment_video(video_url, predicts[i])

    time.sleep(10)
    driver.close()


if __name__ == "__main__":
    main()
