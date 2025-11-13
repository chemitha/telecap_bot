# README - _seeker_bot (telegram_screenshot_bot)
A Telegram bot that captures desktop screenshots remotely.<br>
Run it on your PC and send `/capture` via Telegram to receive an instant image of your current desktop.

---

## Files Overview
- **.env file**: Contains the `TOKEN_KEY` necessary for authenticating the Telegram bot.  
- **_seeker_main.py**: The main Python script that runs the Telegram bot.  
- **_seeker_main.exe**: Executable version of the `.py` file (The `.exe` file still contains some errors/issues, so ***I removed it***).  
- **start_bot.bat**: A batch file that allows you to run the Python script in CMD.

---

## Important Information

### .env File
The `.env` file is crucial for the proper functioning of the bot. It contains the bot's authentication token, which is required to connect to the Telegram API.  
Without this file or its correct configuration, the bot will not function, and you will receive the following message:  
`You need to export TOKEN=YOUR_TELEGRAM_BOT_TOKEN`

### start_bot.bat
The `start_bot.bat` file can be used to run the bot in the background.  
This batch file is designed to loop every 20 minutes due to issues encountered with the Telegram bot/Python.  
You may configure it to automatically start when your computer boots up by following the steps below:

---

## Setting Up Auto-Start with Task Scheduler
To run the bot automatically when your PC starts, use Task Scheduler:

1. Open **Task Scheduler** by searching for it in the Start menu.  
2. Click on **Create Task**.  
3. In the **General** tab, provide a name for the task (e.g., “Run Seeker Bot”).  
4. In the **Triggers** tab, set the trigger to **At startup**.  
5. In the **Actions** tab, click **New** and set the action to **Start a Program**:
   - Select the `.bat` file (`start_bot.bat`) or Python executable (`_seeker_bot.exe`).  
     *(I prefer using .bat files due to certain issues encountered with .exe files.)*  
   - Provide the full path to the `_seeker_main.py` script as an argument.  
6. In the **Conditions** tab, uncheck **"Stop if the computer switches to battery power"** to ensure the bot continues running.  
7. Click **OK** to create the task.

---

## Disclaimer
Please ensure you read this `README.md` file carefully before attempting to run the Telegram bot.  
Failure to follow the instructions may result in issues with bot functionality.  
All files within this folder are essential for the bot to operate correctly.  
Ensure that the `.py`, `.bat`, or `.exe` file has been successfully executed on at least one computer (or server) before using the bot.  
I don't accept any responsibility for security concerns or any issues that may arise from the use or deployment of this bot.

**Created by:** [Sevenplx / Chemitha Sathsilu](https://github.com/Sevenplx)

