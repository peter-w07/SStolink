# SS to Link

SS to Link is a Python script that monitors your clipboard for images, asks for confirmation before uploading (with a "ding" sound and focused window if enabled), and then uploads the image to Gyazo, copying the link to your clipboard. The script runs continuously, ensuring you never miss an opportunity to share your screenshots.

## Features

- Monitors clipboard for images.
- Optional confirmation pop-up before uploading.
- Plays a "ding" sound and focuses the pop-up window.
- Automatically uploads the image to Gyazo.
- Copies the direct link to your clipboard.

## Prerequisites

- Python 3.x
- Gyazo API key (You can get your API key [here](https://gyazo.com/98fa7e6f6d0c1ba204e8be35502238e9))

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/peter-w07/SStolink.git
    cd SStolink
    ```

2. **Install required packages:**

    ```bash
    pip install pillow requests pyperclip tk
    ```

3. **Set your Gyazo API key:**

    Open `sstolink.py` and set your Gyazo API key:

    ```python
    ACCESS_TOKEN = "your_gyazo_access_token"  # Set your Gyazo access token here
    ```

## Usage

1. **Run the script:**

    ```bash
    python sstolink.py
    ```

    When the script starts, it will display ASCII art and begin monitoring your clipboard for images.

2. **Configuration:**

    - To enable or disable the confirmation pop-up, set `ASK_BEFORE_UPLOAD` to `true` or `false` in `sstolink.py`:

    ```python
    ASK_BEFORE_UPLOAD = "true"  # Set to "false" to disable pop-up prompt
    ```

    The script will always run in a loop, ensuring continuous monitoring of your clipboard.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

## Adding to Startup on Windows (Optional)

To run `sstolink.py` automatically when Windows starts:

1. **Create a Batch File:**

    Create a new file named `start_sstolink.bat` and add the following lines:

    ```batch
    @echo off
    cd C:\path\to\SStolink
    python sstolink.py
    ```

    Replace `C:\path\to\SStolink` with the actual path to your `SStolink` directory.

2. **Add to Startup Folder:**

    - Press `Win + R`, type `shell:startup`, and press Enter.
    - Copy the `start_sstolink.bat` file to the Startup folder.

Now, `sstolink.py` will run automatically whenever you start Windows.

