# =============================================
# Alfa Bot Hoster — Sample bot.py template
# Replace this with your actual bot code
# =============================================

import os
import time
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

def main():
    logging.info("Bot started successfully!")
    logging.info("Alfa Bot Hoster — running on Railway.com")
    
    # Your bot logic here
    # Example: Telegram bot, Discord bot, etc.
    
    while True:
        logging.info("Bot is alive and running...")
        time.sleep(60)

if __name__ == "__main__":
    main()
