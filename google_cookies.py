def reject_cookies(driver):
    """reject cookies that appear in google search"""
    try:
        reject = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.QS5gu.sy4vM')))
        reject.click()
    except:
        pass