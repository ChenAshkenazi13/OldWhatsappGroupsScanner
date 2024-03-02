from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def initialize_driver(user_data_dir):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=options)
    driver.get('https://web.whatsapp.com/')
    return driver

def wait_for_whatsapp_to_load(driver):
    wait = WebDriverWait(driver, 600)  # Adjust the timeout as needed
    wait.until(EC.presence_of_element_located((By.ID, 'side')))

def scroll_chat_list(driver):
    panel = driver.find_element(By.ID, 'pane-side')
    scroll_amount = 300
    last_height = driver.execute_script("return arguments[0].scrollTop;", panel)

    while True:
        driver.execute_script(f"arguments[0].scrollTop += {scroll_amount};", panel)
        time.sleep(0.1)  # Adjust based on the load time of your chat content
        new_height = driver.execute_script("return arguments[0].scrollTop;", panel)
        if new_height == last_height:
            break
        last_height = new_height

def extract_chat_names(driver):
    panel = driver.find_element(By.ID, 'pane-side')
    chat_list = panel.find_elements(By.CLASS_NAME, '_21S-L')
    chat_set = set()
    count = 1

    for chat in chat_list:
        try:
            singleChat = chat.find_element(By.TAG_NAME, 'span')
            singleChatTitle = singleChat.get_attribute('title')
            if singleChatTitle not in chat_set:
                chat_set.add(singleChatTitle)
                print(f'{count}) {singleChatTitle[::-1]}')  # Prints in reverse for Hebrew 
                count += 1
        except Exception as e:
            print("Error processing a chat:", e)
    return chat_list

def leave_group(driver, chat_list, group_index : int):
    chosen_chat = chat_list[group_index-1].find_element(By.TAG_NAME, 'span')
    chat_title = chosen_chat.get_attribute('title')
    
    yes_or_no = input(f'Is this the group you want to leave?: {chat_title[::-1]}')  # Prints in reverse for Hebrew 
    if yes_or_no != 'yes':
        print('Fine! Not leaving then')
        return
    
    driver.execute_script("arguments[0].scrollIntoView();", chosen_chat)
    
    # Right-click on the chosen chat to open the context menu
    actions = ActionChains(driver)
    actions.context_click(chosen_chat).perform()
    
    time.sleep(2)

    # The exact number of presses required may vary.
    actions.send_keys(Keys.ARROW_DOWN)  # Adjust the number of presses as necessary
    actions.send_keys(Keys.ARROW_DOWN)  # Adjust the number of presses as necessary
    actions.send_keys(Keys.ARROW_DOWN)  # Adjust the number of presses as necessary
    
    time.sleep(2)

    actions.send_keys(Keys.ENTER).perform()

    time.sleep(2)

    exit_group_button = driver.find_element(By.XPATH, "//div[text()='Exit group']")    # Handle the confirmation dialog that appears when trying to exit a group
    exit_group_button.click()
    return chat_title
 
def delete_group(driver, chat_list, group_index : int):
    chosen_chat = chat_list[group_index-1].find_element(By.TAG_NAME, 'span')
    chat_title = chosen_chat.get_attribute('title')
    
    yes_or_no = input(f'Is {chat_title[::-1]} the group you want to leave?(yes/no)   ')  # Prints in reverse for Hebrew 
    if yes_or_no != 'yes':
        print('Fine! Not leaving then')
        return
    
    driver.execute_script("arguments[0].scrollIntoView();", chosen_chat)

    actions = ActionChains(driver)
    actions.context_click(chosen_chat).perform()
    
    time.sleep(2)

    actions.send_keys(Keys.ARROW_DOWN)  # Adjust the number of presses as necessary
    actions.send_keys(Keys.ARROW_DOWN)  # Adjust the number of presses as necessary

    actions.send_keys(Keys.ENTER).perform()

    exit_group_button = driver.find_element(By.XPATH, "//div[text()='Delete group']")    # Handle the confirmation dialog that appears when trying to exit a group
    exit_group_button.click()

if __name__ == "__main__":
    user_data_dir = 'C:/Users/Chen1/AppData/Local/Google/Chrome/User Data/Guest Profile'

    driver = initialize_driver(user_data_dir)
    wait_for_whatsapp_to_load(driver)

    # scroll_chat_list(driver)
    chat_list = extract_chat_names(driver)
    leave_chat_index = input('Choose group to delete')
    # group_name = leave_group(driver, chat_list, int(leave_chat_index))
    # print('Left group now deleting')
    delete_group(driver, chat_list, int(leave_chat_index))
    # Example usage: leave_group(driver, "Group Name To Leave")
    input("Press any key to exit...")
    driver.quit()
