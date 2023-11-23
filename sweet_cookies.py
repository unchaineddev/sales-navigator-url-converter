import pickle

def save_cookie(driver):
    with open("cookies.pkl", 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)


def load_cookie(driver):
     with open("cookies.pkl", 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             print(cookie)
             driver.add_cookie(cookie)