import io
import time
import requests
from PIL import ImageGrab, Image
import pyperclip
import os
import signal
import sys
from tkinter import Tk, messagebox
import winsound

# Configuration variables
ASK_BEFORE_UPLOAD = "true"  # Set to "false" to disable pop-up prompt
ACCESS_TOKEN = "YOUR_API_KEY_HERE"  # Set your Gyazo access token here

# You can get your Gyazo API key from: https://gyazo.com/98fa7e6f6d0c1ba204e8be35502238e9

def normalize_boolean(value):
    """Normalize a string to a boolean."""
    return str(value).strip().lower() in ['true', '1', 't', 'yes', 'y']

def upload_image(image, file_extension):
    url = "https://upload.gyazo.com/api/upload"
    params = {
        "access_token": ACCESS_TOKEN
    }
    files = {'imagedata': image}
    response = requests.post(url, params=params, files=files)
    response.raise_for_status()
    return response.json().get("permalink_url"), file_extension  # Get the permalink URL and file extension of the uploaded image

def signal_handler(sig, frame):
    print('Exiting program.')
    sys.exit(0)

def handle_image_upload(image, file_extension):
    if ASK_BEFORE_UPLOAD:
        root = Tk()
        root.withdraw()  # Hide the root window

        # Play a "ding" sound
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

        # Focus the pop-up window
        root.deiconify()
        root.lift()
        root.focus_force()

        # Create a dialog to ask the user for confirmation
        user_response = messagebox.askyesno("Upload Image", "Do you want to upload the image?")
        root.destroy()

        if not user_response:
            print("Image upload canceled by user.")
            return

    # Save the image to a BytesIO object
    image_bytes = io.BytesIO()
    image.save(image_bytes, format=file_extension.upper())
    image_bytes.seek(0)

    # Upload the image
    try:
        direct_link, file_extension = upload_image(image_bytes, file_extension)
        if direct_link:
            # Append the correct file extension to the link and copy it to the clipboard
            direct_link_with_extension = f"{direct_link}.{file_extension}"
            pyperclip.copy(direct_link_with_extension)
            print("Image uploaded successfully. Direct link copied to clipboard.")
        else:
            print("Failed to retrieve the direct link.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to upload the image: {e}")

def main():
    global ASK_BEFORE_UPLOAD
    ASK_BEFORE_UPLOAD = normalize_boolean(ASK_BEFORE_UPLOAD)

    ascii_art = """
.______    _______ .___________. _______ .______          _______.                       
|   _  \  |   ____||           ||   ____||   _  \        /       |                       
|  |_)  | |  |__   `---|  |----`|  |__   |  |_)  |      |   (----`                       
|   ___/  |   __|      |  |     |   __|  |      /        \   \                           
|  |      |  |____     |  |     |  |____ |  |\  \----.----)   |                          
| _|      |_______|    |__|     |_______|| _| `._____|_______/                           
                                                                                         
     _______.     _______.   .___________.  ______       __       __  .__   __.  __  ___ 
    /       |    /       |   |           | /  __  \     |  |     |  | |  \ |  | |  |/  / 
   |   (----`   |   (----`   `---|  |----`|  |  |  |    |  |     |  | |   \|  | |  '  /  
    \   \        \   \           |  |     |  |  |  |    |  |     |  | |  . `  | |    <   
.----)   |   .----)   |          |  |     |  `--'  |    |  `----.|  | |  |\   | |  .  \  
|_______/    |_______/           |__|      \______/     |_______||__| |__| \__| |__|\__\ 
                                                                                         
    """
    print(ascii_art)

    if not ACCESS_TOKEN:
        print("Error: Gyazo access token not found. Please set the ACCESS_TOKEN variable.")
        sys.exit(1)

    print("Monitoring clipboard for images... Press Ctrl+C to exit.")
    signal.signal(signal.SIGINT, signal_handler)
    recent_image_hash = None

    while True:
        try:
            # Capture the image from the clipboard
            image = ImageGrab.grabclipboard()
            if image and hasattr(image, 'tobytes'):
                image_hash = hash(image.tobytes())
                if image_hash != recent_image_hash:
                    recent_image_hash = image_hash
                    print("Image detected in clipboard, uploading...")

                    file_extension = image.format.lower()  # Get the image format
                    handle_image_upload(image, file_extension)
        except Exception as e:
            print(f"Error capturing or processing the clipboard image: {e}")

        time.sleep(1)  # Check every second

if __name__ == "__main__":
    main()
