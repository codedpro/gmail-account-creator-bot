from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import random
import time
import string
import secrets
def generate_strong_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

try:
    fake = Faker()

    driver = webdriver.Safari()

    driver.get("https://www.gmail.com")

    create_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[2]/div/div/div[1]/div/button'))
    )
    create_account_button.click()
    time.sleep(2)
    next_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[2]/div/div/div[2]/div/ul/li[1]'))
    )
    next_element.click()
    time.sleep(2)

    first_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="firstName"]'))
    )
    time.sleep(2)

    fake_name = fake.first_name()
    first_name_field.send_keys(fake_name)

    last_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="lastName"]'))
    )
    fake_last_name = fake.last_name()
    last_name_field.send_keys(fake_last_name)

    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="collectNameNext"]/div/button'))
    )
    time.sleep(2)

    next_button.click()
    month_dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="month"]'))
    )
    time.sleep(2)

    while True:
        try:
            month_options = month_dropdown.find_elements(By.TAG_NAME, 'option')
            while True:
                try:
                    random_month = random.choice(month_options)
                    print("Selecting month:", random_month.text)
                    random_month.click()
                    print("Month selected successfully.")
                    break
                except Exception as e:
                    print("Error occurred while selecting month:", e)
                    print("Selecting another month.")
                    time.sleep(1)

            day_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="day"]'))
            )
            time.sleep(2)

            fake_day = fake.day_of_month()
            day_input.send_keys(fake_day)

            year_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="year"]'))
            )
            fake_year = random.randint(1990, 2005)
            year_input.send_keys(fake_year)
            time.sleep(2)

            gender_dropdown = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="gender"]'))
            )
            gender_options = gender_dropdown.find_elements(By.TAG_NAME, 'option')
            gender_random = random.choice(gender_options)
            gender_random.click()
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="birthdaygenderNext"]/div/button'))
            )
            next_button.click()
          
            break
        except Exception as e:
                print("An errorrrrr:", str(e))

                time.sleep(1)
    print("passed")
    time.sleep(2)

    try:
        next_button2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div[1]/div[1]/div/span/div[3]/div'))
        )
        next_button2.click()
    except Exception as e:
        pass
    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div/div[1]/div/div[1]/input'))
    )

    custom_email = f"{fake_name.lower()}.{fake_last_name.lower()}.dev.{random.randint(100, 999)}"
    email_field.send_keys(custom_email)
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="next"]/div/button'))
    )
    next_button.click()


    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="passwd"]/div[1]/div/div[1]/input'))
    )
    password = generate_strong_password()
    password_field.send_keys(password)
    time.sleep(2)

    confirm_password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input'))
    )
    time.sleep(2)
    confirm_password_field.send_keys(password)
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="createpasswordNext"]/div/button'))
    )
    time.sleep(2)
    next_button.click()
    heading_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="headingText"]/span'))
    )
    heading_text = heading_element.text
    if "robot" in heading_text.lower():
        print("The text contains 'robot'.")
    else:
        print("The text does not contain 'robot'.")
except Exception as e:
    print("An error occurred:", e)
finally:
    time.sleep(20)
    driver.quit()
