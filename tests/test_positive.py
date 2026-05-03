import pytest
import time
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("Username,Password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
])
def test_login(get_driver, Username, Password):
    driver = get_driver
    driver.get("https://www.saucedemo.com/")

    # Check page loaded
    assert "Swag Labs" in driver.title

    # Enter credentials
    driver.find_element(By.ID, "user-name").send_keys(Username)
    driver.find_element(By.ID, "password").send_keys(Password)
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    #  Handle expected outcomes properly
    if Username == "locked_out_user":
        error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        assert "locked out" in error.text.lower()
    else:
        assert "inventory" in driver.current_url




