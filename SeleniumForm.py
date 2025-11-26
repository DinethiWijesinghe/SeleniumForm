from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
import time
import os


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

wait = WebDriverWait(driver, 10)
print("Opened web form ")

# ID
text_box = wait.until(EC.presence_of_element_located((By.ID, "my-text-id")))
text_box.send_keys("Hello, Text ID!")
print("Entered text using ID.")
time.sleep(30)

password_box = driver.find_element(By.NAME, "my-password")
password_box.send_keys("Password123")
print("Entered password using NAME.")
time.sleep(30)

textarea = driver.find_element(By.TAG_NAME, "textarea")
textarea.send_keys("This is a textarea")
print("Filled textarea using TAG NAME.")
time.sleep(30)

dropdown = driver.find_element(By.CSS_SELECTOR, "select.form-select")
for option in dropdown.find_elements(By.TAG_NAME, "option"):
    if option.text == "Option 2":
        option.click()
        print("Selected 'Option 2' using CSS SELECTOR.")
        break
time.sleep(30)

# (file upload)
file_input = driver.find_element(By.CLASS_NAME, "form-control")
file_path = os.path.abspath(__file__)  # current script file
file_input.send_keys(file_path)
print("Uploaded file using CLASS NAME.")
time.sleep(30)

# Interact using XPATH (checkbox)
checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
checkbox.click()
print("Clicked checkbox using XPATH.")
time.sleep(30)

#  Interact using Relative Locator: to_right_of
radio_label = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='my-radio-1']")))
driver.execute_script("arguments[0].scrollIntoView(true);", radio_label)
radio_button = driver.find_element(locate_with(By.TAG_NAME, "input").to_right_of(radio_label))
radio_button.click()
print("Selected radio button using Relative Locator: to_right_of.")
time.sleep(30)


# Relative Locator: below (color picker below textarea)
color_input = driver.find_element(locate_with(By.TAG_NAME, "input").below(textarea))
color_input.send_keys("#ff5733")
print("Selected color using Relative Locator: below.")
time.sleep(30)

# Relative Locator: near (date picker near color input)
date_input = driver.find_element(locate_with(By.TAG_NAME, "input").near(color_input))
date_input.send_keys("2025-10-20")
print("Entered date using Relative Locator: near.")
time.sleep(30)

# Relative Locator: above (find element above Submit button)
submit_button = driver.find_element(By.CSS_SELECTOR, "button")
element_above_submit = driver.find_element(locate_with(By.TAG_NAME, "input").above(submit_button))
print("Found element above submit button using Relative Locator: above ->", element_above_submit.get_attribute("name"))
time.sleep(30)

# Relative Locator: to_left_of (find label left of dropdown)
left_label = driver.find_element(locate_with(By.TAG_NAME, "label").to_left_of(dropdown))
print("Found label to the left of dropdown using Relative Locator: to_left_of ->", left_label.text)
time.sleep(30)

# Submit form
submit_button.click()
print("Form submitted successfully using Selenium!")

# Wait and quit browser
time.sleep(5)
driver.quit()
