from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import pyscreenshot as ImageGrab
import os
import asyncio  # Changed: added for async sleeping
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the bot token from environment variables
token = os.getenv('TOKEN')
if not token:
    print("You need to export TOKEN=YOUR_TELEGRAM_BOT_TOKEN")
    exit()

# Initialize the Application
application = Application.builder().token(token).build()

# Define the /start command (asynchronous)
async def start(update: Update, context: CallbackContext):
    """Handles the /start command."""
    await update.message.reply_text(
        "Welcome! Send a /capture request to take a screenshot of the bot's desktop."
    )

# Define the /capture command (asynchronous)
async def capture(update: Update, context: CallbackContext):
    """Handles the /capture command."""
    await update.message.reply_text("Capturing the screen in 1 seconds...")
    print("Heads up! Taking a new screenshot in 1 seconds.")  
    
    await asyncio.sleep(1)  # Changed: proper non-blocking async sleep

    # Capture the screenshot
    screenshot = ImageGrab.grab()
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path, "PNG")

    # Send the screenshot as a photo
    print("Sending screenshot...")
    with open(screenshot_path, 'rb') as photo:
        await update.message.reply_photo(photo=photo)
    print("Screenshot sent successfully.")

# Add the command handlers to the application
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('capture', capture))

# Start the bot
print("Running bot now... Press Ctrl+C to stop.")
application.run_polling()
