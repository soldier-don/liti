import time
import os
import psutil  # To check running processes

def is_bot_running(process_name):
    """Check if the bot process is running."""
    for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            if process.info['cmdline'] and process_name in " ".join(process.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False

def restart_bot():
    """Restart the bot if it's not running."""
    os.system("python3 rb.py &")  # Start p.py in the background

if name == "main":
    bot_process_name = "rb.py"  # The main bot script
    while True:
        if not is_bot_running(bot_process_name):
            print("Bot is OFF. Restarting...")
            restart_bot()
            time.sleep(5)  # Short delay before checking again
        else:
            print("Bot is running. Checking again in 1 minute.")
            time.sleep(60)  # Check every 1 minute
