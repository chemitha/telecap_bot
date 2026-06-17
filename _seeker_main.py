from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import pyscreenshot as ImageGrab
import os
import asyncio  
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

# Synchronous helper function for capturing and compressing the image
def take_and_serialize_screenshot():
    screenshot = ImageGrab.grab()
    screenshot_path = "screenshot.jpg"
    screenshot.convert("RGB").save(screenshot_path, "JPEG", quality=75)
    return screenshot_path

# Define the /capture command (asynchronous)
async def capture(update: Update, context: CallbackContext):
    """Handles the /capture command."""
    await update.message.reply_text("Capturing the screen in 1 seconds...")
    print("Heads up! Taking a new screenshot in 1 seconds.")  
    
    await asyncio.sleep(1)  

    # Capture the screenshot in a background thread
    screenshot_path = await asyncio.to_thread(take_and_serialize_screenshot)

    # Send the screenshot as a photo
    print("Sending screenshot...")
    try:
        with open(screenshot_path, 'rb') as photo:
            await update.message.reply_photo(
                photo=photo,
                write_timeout=60,
                read_timeout=60
            )
        print("Screenshot sent successfully.")
    except Exception:
        print("Failed to send screenshot.")

# Add the command handlers to the application
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('capture', capture))

# Start the bot
print("Running bot now... Press Ctrl+C to stop.")
application.run_polling()
