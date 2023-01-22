from selenium import webdriver



nav = webdriver.Chrome()
nav.get('https://blaze.com/pt')

clicaremlogin = nav.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div[1]/a').click()

username = nav.find_element_by_id(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[2]/div/input')
password = nav.find_element_by_id(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[3]/div/input')
username.send_keys("luanmax.contato10@gmail.com")
password.send_keys("147852@Luan")

login_button = driver.find_element_by_id("//*[@id="header"]/div/div[2]/div/div/div[1]/a")
login_button.click()