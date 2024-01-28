import os
import time
from selene import browser, be, have, by

def test_positive_form_registration():

    browser.open('automation-practice-form')

    browser.driver.execute_script("document.querySelector('#fixedban').remove();")
    browser.driver.execute_script("document.querySelector('footer').remove();")

    browser.element('#firstName').type('Alex')
    browser.element('#lastName').should(be.blank).type('Yanin')
    browser.element('#userEmail').should(be.blank).type('test@test.ru')
    browser.element("[for='gender-radio-1']").click()
    browser.element('#userNumber').should(be.blank).type('7916896581')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(".react-datepicker__year-select").click().element(
        by.text("1982")
    ).click()
    browser.element(".react-datepicker__month-select").click().element(
        by.text("April")
    ).click()
    browser.element(".react-datepicker__day--010").click()

    browser.element('#subjectsInput').should(be.blank).type('Computer Science')\
        .press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture.form-control-file').send_keys(os.path.abspath('photo.jpg'))

    browser.element('#currentAddress').should(be.blank).type('random residential address')

    browser.element("#state").should(be.clickable).click()
    browser.element(by.text('NCR')).should(be.clickable).click()
    browser.element("#city").should(be.clickable).click()
    browser.element(by.text('Delhi')).should(be.clickable).click()

    browser.element('#submit').should(be.clickable).click()

    browser.element('.table').all('td').even.should(
        have.texts('Alex Yanin',
                   'test@test.ru',
                   'Male',
                   '7916896581',
                   '10 April,1982',
                   'Computer Science',
                   'Sports, Reading, Music',
                   'photo.jpg',
                   'random residential address',
                   'NCR Delhi'))
