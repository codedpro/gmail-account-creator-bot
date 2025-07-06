from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time

# Set up the Edge WebDriver options
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("--inprivate")
driver = webdriver.Edge(options=edge_options)

fake = Faker()

def get_phone_number():
    return "+989353591020"

def generate_user_data():
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = f"{first_name.lower()}dev{last_name.lower()}"
    birthday = "02 3 1999"
    password = fake.password()
    gender = str(fake.random_int(min=1, max=2))
    return first_name, last_name, username, birthday, gender, password

def fill_form(driver, first_name, last_name, username, birthday, gender, password):
    try:
        wait = WebDriverWait(driver, 20)
        time.sleep(5)
        first_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        last_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))

        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field.clear()
        last_name_field.send_keys(last_name)

        next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
        next_button.click()
        time.sleep(3)
        birthday_elements = birthday.split()

        month_dropdown = wait.until(EC.visibility_of_element_located((By.ID, "month")))
        Select(month_dropdown).select_by_value(birthday_elements[1])

        day_field = wait.until(EC.visibility_of_element_located((By.ID, "day")))
        day_field.clear()
        day_field.send_keys(birthday_elements[0])

        year_field = wait.until(EC.visibility_of_element_located((By.ID, "year")))
        year_field.clear()
        year_field.send_keys(birthday_elements[2])

        gender_dropdown = wait.until(EC.visibility_of_element_located((By.ID, "gender")))
        Select(gender_dropdown).select_by_value(gender)

        next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
        next_button.click()

        try:
            create_own_option = wait.until(EC.element_to_be_clickable((By.ID, "selectionc2")))
            create_own_option.click()
        except:
            username_field = wait.until(EC.visibility_of_element_located((By.NAME, "Username")))
            username_field.clear()
            username_field.send_keys(username)

        next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
        next_button.click()

        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        password_field.clear()
        password_field.send_keys(password)

        password_confirmation_field = wait.until(EC.visibility_of_element_located((By.NAME, "PasswdAgain")))
        password_confirmation_field.clear()
        password_confirmation_field.send_keys(password)

        next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
        next_button.click()

        return wait

    except Exception as e:
        print(f"Error filling form: {e}")
        return None

def main():
    global driver
    while True:
        try:
            driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
            first_name, last_name, username, birthday, gender, password = generate_user_data()
            wait = fill_form(driver, first_name, last_name, username, birthday, gender, password)
            
            if not wait:
                raise Exception("Form filling failed, retrying...")

            time.sleep(5)  # Allow some time for any error messages to appear

            error_message_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div'
            retry_button_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div/div/button/span'
            try:
                error_message = driver.find_element(By.XPATH, error_message_xpath)
                if error_message.is_displayed():
                    retry_button = wait.until(EC.element_to_be_clickable((By.XPATH, retry_button_xpath)))
                    retry_button.click()
                    first_name, last_name, username, birthday, gender, password = generate_user_data()
                    wait = fill_form(driver, first_name, last_name, username, birthday, gender, password)
                    if not wait:
                        raise Exception("Form filling failed after retry, retrying from the beginning...")
                    continue
            except:
                pass

            # Assuming we have now reached the phone number input stage
            number = get_phone_number()
            phone = wait.until(EC.visibility_of_element_located((By.NAME, "Phone")))
            phone.clear()
            phone.send_keys(number)

            next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
            next_button.click()

            # Complete the rest of the steps if any
            agree_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
            agree_button.click()

            driver.quit()

            print(f"Your Gmail successfully created:\n{{\ngmail: {username}@gmail.com\npassword: {password}\n}}")
            break

        except Exception as e:
            print(f"An error occurred: {e}")
            try:
                driver.quit()
            except:
                pass
            driver = webdriver.Edge(options=edge_options)

if __name__ == "__main__":
    main()
