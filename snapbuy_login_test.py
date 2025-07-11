from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup the ChromeDriver service
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://snapbuy-ecommerce-oqbb.onrender.com/account/my-login")

    # Wait up to 30 seconds for username field to appear
    wait = WebDriverWait(driver, 30)
    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password = driver.find_element(By.NAME, "password")

    username.send_keys("Faizan")
    password.send_keys("leotest@69")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Wait for possible redirect to dashboard
    wait.until(lambda driver: "dashboard" in driver.current_url)

    if "dashboard" in driver.current_url:
        print("Login Test Passed: Dashboard loaded.")
    else:
        print("Login Test Failed: Dashboard not loaded.")

finally:
    driver.quit()
