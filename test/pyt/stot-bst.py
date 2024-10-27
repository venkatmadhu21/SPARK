import os
import time
from playwright.sync_api import sync_playwright


def listen():
    url = 'https://aquamarine-llama-e17401.netlify.app/'

    with sync_playwright() as p:
        # Launch the browser in headless mode
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        # Ensure the data directory exists
        if not os.path.exists('data'):
            os.makedirs('data')

        # Wait for the textbox to be available
        page.wait_for_selector("#textbox", timeout=10000)  # Wait for up to 10 seconds

        last_txt = ""

        while True:
            # Get the current value of the textbox
            current_txt = page.query_selector("#textbox").input_value()

            if current_txt != last_txt:
                # Write the current text to input_cmd.txt if it has changed
                with open(r'data\input_cmd.txt', 'w') as file:
                    file.write(current_txt)
                print(f"Updated input_cmd.txt with: '{current_txt}'")  # Debug print
                last_txt = current_txt

            time.sleep(0.5)  # Polling interval


if __name__ == "__main__":
    listen()
