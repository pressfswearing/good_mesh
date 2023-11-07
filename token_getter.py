import time

def get_token(login, password):
    start_time = time()
    driver.get("https://school.mos.ru")
    sleep(3)
    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/main/section/div/div[1]/div[3]/div/div[1]/div[2]/div')
    login_button.click()
    sleep(5)
    login_input = driver.find_element(By.ID, "login")
    login_input.send_keys(login)
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    submit_button = driver.find_element(By.ID, "bind")
    submit_button.click()
    while "/?token" not in driver.current_url:
        pass
    try:
        callback_code = parse_url(driver.current_url).query[6:-17]
    except TypeError:
        driver.close()
        return "Возникла ошибка"

    driver.close()

    return callback_code

get_token()