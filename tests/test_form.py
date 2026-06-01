from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_form_submission():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("http://127.0.0.1:8000/index.html")  # локально
        
        # Тест 1: Проверка заголовка
        assert "Тестовая Форма" in driver.title
        
        # Тест 2: Заполнение формы
        driver.find_element(By.ID, "name").send_keys("Иван Иванов")
        driver.find_element(By.ID, "email").send_keys("ivan@test.com")
        driver.find_element(By.TAG_NAME, "button").click()
        
        time.sleep(1)
        
        # Тест 3: Проверка сообщения об успехе
        result = driver.find_element(By.ID, "result").text
        assert "Спасибо, Иван Иванов!" in result
        
        print("Все тесты прошли успешно!")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_form_submission()
