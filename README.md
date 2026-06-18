# README - _seeker_bot (telegram_screenshot_bot)

A Telegram bot that captures desktop screenshots remotely.  
Run it on your PC and send `/capture` via Telegram to receive an instant image of your current desktop.

---

## Files Overview

- **.env file**: Contains the `TOKEN` necessary for authenticating the Telegram bot.  
- **_seeker_main.py**: The main Python script that runs the Telegram bot.  
- **start_bot.bat**: A batch file that allows you to run the Python script in CMD.  
- **requirements.txt**: List of Python dependencies.

**Note**: The `.exe` file was removed due to issues.

---

## Setup Instructions (Step-by-Step A-Z Guide)

### 1. Create Your Telegram Bot
1. Open Telegram and search for **@BotFather**.
2. Start a chat with it and send the command `/newbot`.
3. Follow the prompts: give your bot a name and a username (must end with `_bot`).
4. **BotFather** will give you an **API Token** (format like `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`).  
   **Copy and save this token securely.**

### 2. Prepare the `.env` File
1. In the project folder, create a new file named exactly `.env`.
2. Open it with Notepad (or any text editor) and add this single line:  
   `TOKEN={Telegram bot token goes here}`  
   (Replace `{Telegram bot token goes here}` with the token you received from BotFather).
3. Save the file.

### 3. Install Required Packages
1. Make sure **Python** is installed on your PC (download from python.org if needed).
2. Open **Command Prompt** (CMD) and navigate to the project folder (use `cd path\to\folder`).
3. Run this command:  
   `python -m pip install -r requirements.txt`

> ⚠️ **Python 3.14+ Compatibility Note:** If the bot instantly crashes on startup with a `typing.Union` or `AttributeError`, your local packages are outdated for your newer Python version. Force an update by running:
> ```cmd
> pip install --upgrade python-telegram-bot httpcore httpx
> ```

### 4. Run the Bot (Critical Instructions)
1. **You must keep a Command Prompt / Terminal window open at all times.** Closing the window will stop the bot and prevent screenshots from working.
2. Double-click `start_bot.bat` (recommended), **OR** run this command in CMD:  
   `python _seeker_main.py`
3. The terminal will show "Running bot now..." — leave this window open/minimized.
4. **Important limitations**:
   - Do **not** run this on a server, VPS, or any headless environment.
   - Do **not** use Task Scheduler, Auto-Start services, or run it in the background without an active logged-in Windows desktop session.
   - These methods usually result in **black/empty screenshots** because `pyscreenshot` needs a real graphical desktop environment.

### 5. How to Use the Bot
- Open Telegram and start a chat with your bot (search by the username you created).
- Send `/start` → Bot will reply with a welcome message.
- Send `/capture` → Bot will capture the current desktop screenshot and send it back to you.

---
## Video Walkthrough

<video src="https://github.com/user-attachments/assets/742a8235-e7c1-44c3-88ae-37cbe79ed041" controls width="100%" max-width="750px"></video>

---

## Important Information

### `.env` File
Without a correctly configured `.env` file, the bot will fail with the message:  
`You need to export TOKEN={Telegram bot token goes here}`

### `start_bot.bat`
This file helps launch the script. Keep the resulting terminal window open — it is required for the bot to function properly.

---

## Disclaimer
Read this README carefully before use.  
This tool is intended for **personal use on your own PC** only.  
I am not responsible for any security issues, misuse, or problems that may arise.

**Created by:** [Sevenplx / Chemitha Sathsilu](https://github.com/chemitha)
