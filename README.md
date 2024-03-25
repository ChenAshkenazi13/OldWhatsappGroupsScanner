# Old Whatsapp groups scanner

## Description
This project offers a convenient way to manage your participation in old WhatsApp groups.
Utilizing the power of Python, this tool scans all WhatsApp groups associated with your account and prompts you to decide whether you wish to remain in each group or leave.

## Project Motivation
This project was inspired by a personal incident: after switching to a new phone, I discovered that all my previous WhatsApp group texts were deleted. Rather than attempting to recover these messages, I saw this as an opportunity to declutter my digital life by exiting numerous WhatsApp groups that are no longer in use. Recognizing the manual process was inefficient, I decided to automate it.

# Prerequirements
1. You have python installed on your PC. If not please download it from: `https://www.python.org/downloads/`.
2. You have Google Chrome installed. If not install from: `https://support.google.com/chrome/answer/95346?hl=en&co=GENIE.Platform%3DDesktop#zippy=`.
3. You have Whatsapp Web connected to your phone's Whatsapp app on your default browser in your guest profile.

# Usage
## Getting started
1. Clone this repository. `git clone https://github.com/ChenAshkenazi13/OldWhatsappGroupsScanner.git`.
2. Open on your favorite text editor like VSCode.
3. Install the necessary libraries by running: `pip install selenium`.
4. Follow `Code changes`. See below.
5. Execute the script in your terminal or command prompt: `py ./index.py`. 
6. Follow the instructions of the code.
In summary enter:
* `leave` - To choose a group to leave from the printed chats list.
* `next` - To scroll down and load more chats.
* `quit` - To exit the program.

### Importent note
After following the instructions above when choosing to leave a number of groups from the printed list:
Instead of running script for each individual group you can enter the following format in order to leave and delete number of groups. 
`first_group_index::last_group_index`.

## Code changes
1. Update the `user_data_dir` to the location of your `Guest Profile` folder. The default location is:
`user_data_dir = 'C:/Users/<YOUR_USER>/AppData/Local/Google/Chrome/User Data/Guest Profile'`.


## Important Notes
- Double check if the chosen chat is indeed a group, if not the result may be unexpected as the list printed is different in comparison to a personal chat.
- This script is based on the current HTML structure of WhatsApp Web. If WhatsApp updates the UI, the script may require adjustments.

# Disclaimer
This script is for educational purposes only. Automating interactions with WhatsApp Web may violate WhatsApp's terms of service. Use it responsibly and at your own risk.

