from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#TODO: Remove .gitignore from commits 
options = webdriver.ChromeOptions() 

userdatadir = 'C:/Users/Chen1/AppData/Local/Google/Chrome/User Data/Guest Profile'
options.add_argument(f"--user-data-dir={userdatadir}")

driver = webdriver.Chrome(options=options)
driver.execute_script("document.body.style.zoom='50%'")
driver.get('https://web.whatsapp.com/')

wait = WebDriverWait(driver, 600)  # Adjust the timeout as needed
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'canvas[aria-label="Scan me!"]')))
# print("QR Code scanned. Logged in.")


wait.until(EC.presence_of_element_located((By.ID, 'side')))

# Find elements that represent chats (both individual and groups)
# Note: The class name ('_210SC') is likely to change; inspect the element to find the current class name
elements = driver.find_elements(By.ID, 'side')
print("Found chats:")
for element in elements:
    paneSide = element.find_element(By.ID, 'pane-side')
    className = paneSide.get_attribute('class')
    print(f'class = {className}')
    chats = paneSide.find_element(By.CLASS_NAME, '_3YS_f')
    chatsAttributes = str(chats.get_attribute('aria-label')) +  str(chats.get_attribute('role'))
    print(f'chatsAttributes = {chatsAttributes}')
    chatsForReal = chats.find_elements(By.CLASS_NAME, '_21S-L')
    count = 1
    for chat in chatsForReal:
        singleChat = chat.find_element(By.TAG_NAME, 'span')
        singleChatTitle = singleChat.get_attribute('title')
        print(f'{count}) {singleChatTitle[::-1]}')
        count += 1
    # chatsForReal[1].

    # paneSide.find_element(By.CLASS_NAME,)
# Filter out groups from the chats
# This is tricky because WhatsApp Web does not easily distinguish between groups and individual chats by class names or ids
# You might need to look for specific attributes or patterns that can help you distinguish groups from individual chats
# groups = [chat for chat in chats if "some distinguishing feature" in chat.text]

# Print or process the groups
# for group in groups:
#     print(group)  # or any other processing you want to do

print("DONE")
x = input()
driver.quit()