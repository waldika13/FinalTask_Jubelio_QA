from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "https://app.jubelio.com/login"

driver.get(url)
driver.maximize_window()
driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(3)

# Navigasi ke halaman "Barang" > "Persediaan" pada sidebar
menu_barang = driver.find_element(By.XPATH, "//span[text()='Barang']")
menu_persediaan = driver.find_element(By.XPATH, "//span[text()='Persediaan']")

# Klik menu "Barang"
menu_barang.click()
time.sleep(1)

# Klik menu "Persediaan" yang ada di dalam menu "Barang"
menu_persediaan.click()
time.sleep(1)

# click button Penyusaian Persediaan
penyesuaian_stock = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]")
penyesuaian_stock.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Penyesuaian Persediaan')]")))

# input product
scan_barang = driver.find_element(By.XPATH, "//input[@placeholder='Scan']")
product = "ROG-3000"
scan_barang.send_keys(product, Keys.ENTER)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'ASUS ROG')]")))

# Click button Simpan
simpan_button = driver.find_element(By.XPATH, "//button[contains(@class, 'ladda-button') and .//span[contains(text(),'Simpan')]]")
simpan_button.click()

print('Successfully')
time.sleep(3)
driver.quit()