from selenium import webdriver
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Chrome(executable_path='C://Program Files//chromedriver//chromedriver.exe')
    driver.get('https://larissa.co.id/lkarir/Login')
    driver.implicitly_wait(10)
    driver.minimize_window()
    yield driver
    driver.close()



def test_login_success(setup): #testcase 001
    setup.find_element_by_id('txt_email').send_keys('rxxxxxxxxx2@gmail.com')
    setup.find_element_by_id('txt_password').send_keys('Password123')
    setup.find_element_by_id('btn_login').click()
    Badge = setup.find_element_by_class_name('page-header').text
    assert Badge == 'Halaman Utama'

Accounts = [('rxxxxxxxxx2@gmail.com','salah'),
            ('risky@gmail.com','Password123'),
            ('awin@gmail.com','salah')]

@pytest.mark.parametrize('a,b', Accounts)
def test_login_unsuccess(setup,a,b): #testcase 002,003,004
    setup.find_element_by_id('txt_email').send_keys('a')
    setup.find_element_by_id('txt_password').send_keys('b')
    setup.find_element_by_id('btn_login').click()
    Badge = setup.find_element_by_xpath('//*[@id="loginform"]/div[1]').is_displayed()
    assert Badge == True

    


