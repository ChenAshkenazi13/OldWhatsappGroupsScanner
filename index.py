from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

dramatic_effect_time = 2  #Wait time in minutes for dramatic effect
scroll_amount = 1000      #Adjust as needed
web_driver_wait = 600     #Adjuest as needed

def wait_for_dramatic_effect():
    time.sleep(dramatic_effect_time)

def initialize_driver(user_data_dir):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=options)
    driver.get('https://web.whatsapp.com/')
    return driver

def wait_for_whatsapp_to_load(driver):
    wait = WebDriverWait(driver, web_driver_wait)  
    wait.until(EC.presence_of_element_located((By.ID, 'side')))

def scroll_chat_list(driver):
    panel = driver.find_element(By.ID, 'pane-side')
    driver.execute_script(f"arguments[0].scrollTop += {scroll_amount};", panel)

def extract_chat_names(driver):
    panel = driver.find_element(By.ID, 'pane-side')
    chat_list = panel.find_elements(By.CLASS_NAME, '_21S-L')
    count = 0

    for chat in chat_list:
        try:
            singleChat = chat.find_element(By.TAG_NAME, 'span')
            singleChatTitle = singleChat.get_attribute('title')
            print(f'{count}) {singleChatTitle[::-1]}')  # Prints in reverse for Hebrew 
            count += 1

        except Exception as e:
            print("Error processing a chat:", e)
    return chat_list


def perform_leave_group(actions):
    try:
        for _ in range(3):
            actions.send_keys(Keys.ARROW_DOWN) 
      
        actions.send_keys(Keys.ENTER).perform()
        wait_for_dramatic_effect()

        driver.find_element(By.XPATH, "//div[text()='Exit group']").click()
    except Exception as e:
        raise e
    
def perform_delete_group(actions):
    try:
        for _ in range(2):
            actions.send_keys(Keys.ARROW_DOWN) 

        actions.send_keys(Keys.ENTER).perform()
        wait_for_dramatic_effect()

        driver.find_element(By.XPATH, "//div[text()='Delete group']").click()
    except Exception as e:
        raise e

def perform_group_action(driver, chat_list, group_index : int):
    chosen_chat = chat_list[group_index].find_element(By.TAG_NAME, 'span')
    chat_title = chosen_chat.get_attribute('title')
    
    # Prints in reverse for Hebrew 
    if input(f'Is this the group you want to leave?: {chat_title[::-1]}  - ') != 'yes': 
        print('Fine! Not leaving then')
        return
    
    try:
        driver.execute_script("arguments[0].scrollIntoView();", chosen_chat)
        actions = ActionChains(driver)
        
        actions.context_click(chosen_chat).perform() # Right-click on the chosen chat to open the context menu
        
        wait_for_dramatic_effect()

        perform_leave_group(actions)
        wait_for_dramatic_effect()
        driver.execute_script("arguments[0].scrollIntoView();", chosen_chat)

        actions.context_click(chosen_chat).perform()
        perform_delete_group(actions)

    except Exception as e:
                print("Error processing a chat:", e)        



if __name__ == "__main__":
    user_data_dir = 'C:/Users/Chen1/AppData/Local/Google/Chrome/User Data/Guest Profile'
    driver = initialize_driver(user_data_dir)
    wait_for_whatsapp_to_load(driver)

    print('\n\nHello and welcome!\n Enter "leave" for leaving and deleting the chosen WhatsApp group.\n Enter "next" for loading more groups.\n Enter "quit" for quit')
   
    chat_list = extract_chat_names(driver)
    user_command = input('What would you like to do? (leave/next/quit): ')
    
    while user_command != 'quit':
        match user_command:
            case 'leave':
                leave_chat_index = input('Choose group to delete: ')
                perform_group_action(driver, chat_list, int(leave_chat_index))

            case 'next':
                scroll_chat_list(driver)
                chat_list = extract_chat_names(driver)

            case _:
                print('Unknow command. Try again')

        user_command = input('What would you like to do? (leave/next/quit): ')


    print("\n\n BYE!")
    driver.quit()