from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

# Correct path
service = Service("C:\\WebDriver\\geckodriver.exe")
driver = webdriver.Firefox(service=service)

# Base URL
base_url = "http://127.0.0.1:5000/login"


# Helper function for login test
def test_login(username, password, expected_result):
    driver.get(base_url)
    time.sleep(1)

    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.ID, "loginBtn")

    username_field.clear()
    password_field.clear()

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    time.sleep(2)
    current_url = driver.current_url

    if expected_result == "success" and "feedback" in current_url:
        print(f"✅ Test Passed: Valid login with ({username}, {password})")
    elif expected_result == "failure" and "login" in current_url:
        print(f"✅ Test Passed: Login failed as expected for ({username}, {password})")
    else:
        print(f"❌ Test Failed for ({username}, {password}) — Unexpected result")


# Test cases
print("Running Login Test Cases...\n")

# 1⃣ Valid credentials
test_login("student1", "12345", "success")

# 2️ Invalid username
test_login("invalidUser", "12345", "failure")

# 3️ Invalid password
test_login("student1", "wrongpass", "failure")

# 4️ Empty username
test_login("", "12345", "failure")

# 5️ Empty password
test_login("student1", "", "failure")

# 6️ Both fields empty
test_login("", "", "failure")

# 7️ SQL Injection attempt
test_login("' OR '1'='1", "' OR '1'='1", "failure")

# 8️ Case sensitivity check
test_login("Student1", "12345", "failure")

# 9️ Whitespace in username
test_login(" student1 ", "12345", "failure")

# 10️ Special characters in username
test_login("student@123", "12345", "failure")

print("\nAll tests executed.")

driver.quit()
