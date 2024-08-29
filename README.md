
# Telegram Scraper

This is a simple Telegram scraper that listens for new messages in your Telegram account and searches for a specified phrase. When it finds a matching phrase, it plays an alert sound.

## Features
- Search for a specific phrase in incoming Telegram messages.
- Play an alert sound when the phrase is found.

## Requirements
- Python 3.7 or higher
- `telethon` library for interacting with Telegram API.
- `pygame` library for playing sound alerts.

## Setup Instructions

### 1. Clone the Repository
If you haven’t cloned your code yet, use the following command:

``bash
git clone git@github.com:TertiusN/simple-tg-scraper.git
cd your-repo`` 

### 2. Create a Virtual Environment

To create a virtual environment, follow these steps:

#### On macOS/Linux:

`python3 -m venv venv` 

#### On Windows:

`python -m venv venv` 

### 3. Activate the Virtual Environment

#### On macOS/Linux:

`source venv/bin/activate` 

#### On Windows:

`venv\Scripts\activate` 

### 4. Install Dependencies

Once the virtual environment is activated, install the required libraries:

`pip install telethon pygame` 

### 5. Configure Your Script

Before running the script, make sure to replace the following placeholders with your actual credentials in the script:

-   `api_id`: Your Telegram API ID.
-   `api_hash`: Your Telegram API hash.
-   `phone_number`: Your phone number associated with your Telegram account.

### 6. Prepare the Alert Sound

Make sure you have an alert sound file named `uwu.mp3` in the same directory as your script, or modify the `alert_sound` variable in the script to point to your desired audio file.

### 7. Run the Script

You can run the script using the following command:

`python your_script.py --PHRASE "your search phrase"` 

Replace `your_script.py` with the name of your Python file and `"your search phrase"` with the phrase you want to search for in messages.

## Example

To search for the phrase "hello", you would run:

`python your_script.py --PHRASE "hello"` 

## Notes

-   Ensure that you have permissions to access your Telegram messages through the API.
-   If you have any issues with the script, please check your API credentials and make sure your environment is properly set up.
- Visit https://my.telegram.org/apps for API key