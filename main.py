from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def get_driver():
    """
    Summary:
    Function to get a WebDriver instance for Edge browser with specific options and navigate to Google's homepage.

    Explanation:
    This function sets up custom options for the Edge browser, creates a WebDriver instance, navigates to Google's homepage, and returns the driver.

    Args:
    Returns:
        WebDriver: A WebDriver instance for the Edge browser.

    Examples:
        driver = get_driver()
    """

    options = webdriver.EdgeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-extensions")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Edge(options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver


def clean_text(text: str):
    """
    Summary:
    Function to clean and extract text after a colon in a string.

    Explanation:
    This function takes a string as input, splits it by colon, extracts and returns the text after the colon.

    Args:
        text (str): The input text containing a colon.

    Returns:
        str: The cleaned text after the colon.

    """

    return text.split(":")[1].strip()


def main():
    """
    Summary:
    Main function to automate a series of actions on a web page using a WebDriver instance.

    Explanation:
    This function automates a series of actions on a web page, including entering text, clicking elements, extracting and printing output, and finally quitting the WebDriver.

    Args:
    Returns:
        None
    """
    d = get_driver()
    d.find_element(By.ID, "id_username").send_keys("automated")
    time.sleep(1)
    d.find_element(By.ID, "id_password").send_keys(f"automatedautomated{Keys.RETURN}")
    time.sleep(2)
    d.find_element(By.XPATH, "/html/body/nav/div/a").click()
    time.sleep(3)
    t = d.find_element(By.CLASS_NAME, "text-success")
    output = int(clean_text(t.text))
    print(output)
    # print(el)

    d.quit()


if __name__ == "__main__":
    main()
