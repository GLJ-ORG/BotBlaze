from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


nav = webdriver.Chrome()
nav.get('https://blaze.com/pt')


esp = sleep(15)
clicaremlogin = nav.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div[1]/a').click()
esp1 = sleep(8)
colocaremail = nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[1]/div/input').send_keys('lucasv17.lv29@gmail.com')
esp2 = sleep(5)
colocarsenha = nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[2]/div/input').send_keys('147852@Lucas')
esp3 = sleep(5)
clicarem_entrar = nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[4]/button').click()
esp4 = sleep(20)
nav.get('https://blaze.com/pt/games/double')
esp5 = sleep(10)

colocar_valor = nav.find_element(By.XPATH, '//*[@id="roulette-controller"]/div[1]/div[2]/div[1]/div/div[1]/input').send_keys('1.25')
esp6 = sleep(2)
colocar_valor = nav.find_element(By.XPATH, '//*[@id="roulette-controller"]/div[1]/div[2]/div[2]/div/div[2]/div').click()

#Variaveis globais









esp40 = sleep(30)






