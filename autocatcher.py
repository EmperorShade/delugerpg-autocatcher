import time
import random
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from winotify import Notification
from datetime import datetime
from credentials import id, passwd
from files_and_assets.maps import maps
from files_and_assets.movement_keys import *
from files_and_assets.pokemon_list import *
from files_and_assets.variables import *
from files_and_assets.notifications import ico_path


options = webdriver.ChromeOptions() 
options.add_argument("--start-maximized")


def zoom_out():
    # driver.execute_script("document.body.style.zoom = '60%'")
    action.key_down(Keys.LEFT_CONTROL).send_keys(Keys.SUBTRACT).key_up(Keys.LEFT_CONTROL).perform()
    time.sleep(.4)
    action.key_down(Keys.LEFT_CONTROL).send_keys(Keys.SUBTRACT).key_up(Keys.LEFT_CONTROL).perform()
    time.sleep(.4)
    action.key_down(Keys.LEFT_CONTROL).send_keys(Keys.SUBTRACT).key_up(Keys.LEFT_CONTROL).perform()
    time.sleep(.4)
    action.key_down(Keys.LEFT_CONTROL).send_keys(Keys.SUBTRACT).key_up(Keys.LEFT_CONTROL).perform()
    time.sleep(.4)
    action.key_down(Keys.LEFT_CONTROL).send_keys(Keys.SUBTRACT).key_up(Keys.LEFT_CONTROL).perform()
    time.sleep(.4)
    action.key_down(Keys.LEFT_CONTROL).send_keys(Keys.SUBTRACT).key_up(Keys.LEFT_CONTROL).perform()
    time.sleep(.4)


def ball_check():
    try:
        balls = driver.find_element(By.CLASS_NAME, "cardif")
        balls_data = (balls.text)

        for b in balls_test:
            if b in balls_data:
                pokemart_btn = driver.find_element(By.LINK_TEXT, "Visit Pokemart")
                time.sleep(.25)
                pokemart_btn.click()
                time.sleep(3)
                masterball_box = driver.find_element(By.NAME, "itembuy[masterball]")
                time.sleep(.25)
                masterball_box.click()
                time.sleep(2)
                action.send_keys("5").perform()
                time.sleep(2)
                action.send_keys(Keys.RETURN).perform()
                print("Purchased Masterball")
                now = datetime.now()
                dt_string = now.strftime("%H:%M:%S")
                with open(".\logs.txt", 'a') as f:
                    f.write("\n")
                    f.write(dt_string + " -- Purchased Masterballs")
                time.sleep(3)
                driver.get(rand_map)
            elif b not in balls_data:
                pass
            else:
                pass
    except:
        pass


def login():
    
    try:
        global usrn_box
        global pass_box
        usrn_box = driver.find_element(By.NAME, 'username')
        pass_box = driver.find_element(By.NAME, 'password')
        action.click(on_element=usrn_box)
        time.sleep(1)
        usrn_box.send_keys(id)
        print("Entering username...")
        time.sleep(1)
        action.click(on_element=pass_box)
        time.sleep(1)
        pass_box.send_keys(passwd)
        print("Decrypting passcode...")
        time.sleep(3)
        pass_box.send_keys(Keys.RETURN)
        print("Logging in...")
        time.sleep(1)
        print("Logged in successfully.")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open(".\logs.txt", 'a') as f:
            f.write("\n")
            f.write(dt_string + " -- Logged in")
    except NoSuchElementException:
        print("unable to login")
        login()


def startmap():
    global rand_map
    rand_map = random.choice(maps)
    driver.get(rand_map)
    time.sleep(2)
    time.sleep(5)
    return rand_map


def search():
    global streak

    counter = 0
    counter_limit = random.randint(60, 80)
    while counter < counter_limit:
        try:
            counter += 1
            ball_check()
            time.sleep(.25)
            to_move = random.choice(movement_keys)
            to_move_element = driver.find_element(By.ID, str(to_move))
            to_move_element.click()
            time.sleep(.75)

            poke_box = driver.find_element(By.ID, "showpoke")
            poke_text = (poke_box.text)

            t = 0

            if  t < 1:

                for p in found_or_not:

                    if p in poke_text and p == "Appeared!":
                        print("Pokemon Appeared")    


                        for i in pokemonlist:
                                            
                            if i in poke_text and t < 1:

                                print(i)
                                time.sleep(.25)
                                print("Found a " + i + "!")
                                streak += 1

                                title_noti = ("Autocatcher found " + i + "!")
                                msg_noti = ("This is the " + str(streak) + "th legendary caught this session")
                                
                                notify = Notification(app_id="Auto-catcher",
                                        title=title_noti,
                                        msg=msg_noti,
                                        icon=ico_path,
                                        duration="short")
                                notify.show()

                                catch_btn = poke_box.find_element(By.CLASS_NAME, "btn-catch-action")
                                time.sleep(.25)
                                catch_btn.click()
                                time.sleep(3)
                                battle_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/form/div[4]/input[1]")
                                time.sleep(.25)
                                battle_btn.click()
                                time.sleep(3.5)
                                master_ball = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/form/div[1]/div[4]/div[3]")
                                time.sleep(.25)     
                                master_ball.click()
                                time.sleep(2)
                                throw_poke = driver.find_element(By.CSS_SELECTOR, "#itemwrap > div:nth-child(1) > form > div.buttoncenter.clear > input:nth-child(2)")
                                time.sleep(.25)
                                throw_poke.click()
                                now = datetime.now()
                                dt_string = now.strftime("%H:%M:%S")
                                with open(".\logs.txt", 'a') as f:
                                    f.write('\n')
                                    f.write(dt_string + " -- found " + str(i))


                                time.sleep(3)
                                return_to_map = driver.find_element(By.LINK_TEXT, " Return to Map ")
                                time.sleep(.25)
                                return_to_map.click()
                                time.sleep(2)
                                t += 1
                                

                            elif i not in poke_text and t < 1:
                                pass
                            elif t >= 1:
                                pass


                    elif p in poke_text and p == "anything":
                        print("No Pokemon")
                        pass
                    else:
                        pass



            else:
                pass



        except ElementClickInterceptedException:
            print("elementnotclickable")
            pass
        except ElementNotInteractableException:
            print("elementnotinteractable")
            pass
        except NoSuchElementException:
            print("elementnotfound")
            pass
        except StaleElementReferenceException:
            print("StaleElementReferenceException")
            pass


    print("Loading new map...")
    startmap()


if __name__ == '__main__':
    driver = uc.Chrome(options=options)
    action = ActionChains(driver)
    driver.get("https://www.delugerpg.com/login")

    zoom_out()
    time.sleep(2)
    login()
    startmap()
    while True:
        search()
 
