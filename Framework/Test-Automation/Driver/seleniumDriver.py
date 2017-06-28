# coding: utf-8

import time
import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_web_driver_path(web_driver_path, browser_name):
    _os = platform.system()
    if _os.__contains__("Windows"):
        return "%s/Windows/%sdriver.exe" % (web_driver_path, browser_name)
    elif _os.__contains__("Linux"):
        return "%s/Linux/%sdriver" % (web_driver_path, browser_name)
    elif _os.__contains__("Darwin"):
        return "%s/Darwin/%sdriver" % (web_driver_path, browser_name)
    else:
        raise Exception("No webdriver can be found for os '%s'" % _os)


def open_browser(web_driver_path, browser_name):
    driver = webdriver.Firefox()  # -

    # driver = webdriver.Chrome()  # -

    """
    _exe_path = get_web_driver_path(web_driver_path, browser_name)
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=_exe_path)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=_exe_path)
    elif browser_name == "ie":
        driver = webdriver.Ie(executable_path=_exe_path)
    elif browser_name == "opera":
        driver = webdriver.Opera(executable_path=_exe_path)
    elif browser_name == "safari":
        driver = webdriver.Safari(executable_path=_exe_path)
    else:
        raise Exception("browser '%s' cannot be supported, please select one from [chrome, firefox, ie, opera, safari]" % browser_name)
    """
    driver.maximize_window()
    return driver


def close_browser(driver):
    if driver is not None:
        # driver.close()
        driver.quit()


def wait_element_load(driver, element_id=None, element_xpath=None, timeout=30):
    """
    Wait until specified element is loaded
    """
    _element = ""
    try:
        if element_id is not None:
            _element = element_id
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, element_id)))
        elif element_xpath is not None:
            _element = element_xpath
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
    except:
        raise Exception("element '%s' cannot be loaded" % _element)


def wait_element_unloaded(driver, element_id=None, element_xpath=None, timeout=30):
    """
    Wait until specified element is hidden
    """
    _element = ""
    try:
        if element_id is not None:
            _element = element_id
            WebDriverWait(driver, timeout).until_not(EC.presence_of_element_located((By.ID, element_id)))
        elif element_xpath is not None:
            _element = element_xpath
            WebDriverWait(driver, timeout).until_not(EC.presence_of_element_located((By.XPATH, element_xpath)))
    except:
        raise Exception("element '%s' still displays" % _element)


def load_page(driver, page_url, key_element_id=None, need_refresh=False):
    """
    Open specified url and wait the key element loaded
    """
    _error = ""
    _timeout = 30
    while _timeout > 0:
        try:
            driver.get(page_url)
            if driver.current_url.strip("/") != page_url.strip("/"):
                continue
            if key_element_id is not None:
                wait_element_load(driver, key_element_id, timeout=10)
            return
        except Exception, e:
            if need_refresh:
                driver.refresh()
            _error = e.message
            time.sleep(1)
            _timeout -= 1
    else:
        raise Exception("load page '%s' failed, error message: %s" % (page_url, _error))


def check_required_keys(dict, required_keys):
    """
    Check the required keys for specified dictionary
    """
    _missing_options = []
    for _key in required_keys:
        if dict.has_key(_key) and len(dict[_key]) > 0:
            continue
        else:
            _missing_options.append(_key)
    if len(_missing_options) > 0:
        raise Exception("unable to find the required keys: %s" % ",".join(_missing_options))


def move_mouse_to_element_middle(driver, element):
    """
    Simulate mouse moving to the middle position of some element.
    :param element:
    :return:
    """
    ActionChains(driver).move_to_element(element).perform()
