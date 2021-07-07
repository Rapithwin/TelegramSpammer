from selenium import webdriver
import time

driver = None
def browser():
    global driver
    driver_name = input("\nWhat browser do you want to use?(chrome, edge, firefix, safari): ")
    driver_path = input("\nEnter the diver's exact path: ")
    if driver_name.lower() == "chrome":
        driver = webdriver.Chrome(driver_path)
    elif driver_name.lower() == "edge":
        driver = webdriver.Edge(driver_path)
    elif driver_name.lower == "firefox" or "fire fox":
        driver = webdriver.Firefox(driver_path)
    elif driver_name.lower == "safari":
        driver = webdriver.Safari(driver_path)

def login():
    # Open Telegram Web
    try:
        driver.get("https://web.telegram.org/k/")  
    except Exception as e:
        print(e)
    print("\nOpen the browser and login to your telegram account, then press enter to continue.")
    input(">")

def send_message(username, message, message_count):
    while True:
        # Find search bar
        search_bar = driver.find_element_by_xpath('//*[@id="column-left"]/div/div/div[1]/div[2]/input')
        search_bar.click()
        time.sleep(1)
        search_bar.send_keys(username)
        time.sleep(1)
        target = driver.find_element_by_xpath('//*[@id="search-container"]/div[2]/div/div/div[1]/div/div[1]/ul/li/div[1]')
        target.click()
        # Find message box
        msg_box = driver.find_element_by_xpath('//*[@id="column-center"]/div/div/div[4]/div/div[1]/div[6]/div[1]/div[1]')

        target_check = input("\nIs the chat page openned in you browser right?(y/n)")
        if target_check.lower() == "y":
            # Find send button and send the message
            for a in range(message_count):
                msg_box.send_keys(message)
                send_msg = driver.find_element_by_xpath('//*[@id="column-center"]/div/div/div[4]/div[1]/div[4]/button/div')
                send_msg.click()
            break
        elif target_check.lower() == "n":
            # Enter correct username or saved name
            cor_tlg_usrname = input("\nEnter your target's username or exact saved name: ")
            continue


if __name__ == "__main__":

    browser()
    while True:
        login()
        tlg_username = input("\nEnter your target's username or exact saved name: ")
        msg = input("\nEnter the message : ")
        count = int(input("\nHow many times do you want to send it? : "))
        send_message(tlg_username, msg, count)

        again = input("\nDo you want to spam again?(y/n)")
        if again.lower() == "n":
            time.sleep(2)
            driver.close()
            raise SystemExit
        elif again.lower() == "y":
            continue
        else:
            raise ValueError
            continue