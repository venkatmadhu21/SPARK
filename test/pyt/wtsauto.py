from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path to your ChromeDriver
driver_path = "path/to/chromedriver"
driver = webdriver.Chrome(driver_path)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for the user to scan the QR code
print("Scan the QR code, then press Enter.")
input()

# Function to send a message
def send_whatsapp_message(contact_name, message):
    try:
        # Search for the contact
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.send_keys(contact_name)
        time.sleep(2)  # Wait for the contact list to update

        # Select the contact
        contact = driver.find_element(By.XPATH, f'//span[@title="{contact_name}"]')
        contact.click()

        # Type and send the message
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')
        message_box.click()
        message_box.send_keys(message)
        message_box.send_keys('\n')  # Press Enter to send

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
send_whatsapp_message("Contact Name", "Hello from automation!")

# Close the driver after a delay
time.sleep(5)
driver.quit()
