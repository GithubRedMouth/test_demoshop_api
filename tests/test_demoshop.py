from selene import have
from utils.base_session import demoshop, LogsOfRequestsInConsole


@LogsOfRequestsInConsole()
def test_login():
    response = demoshop.post('/login', data={'Email': 'test@qa.guru.com', 'Password': '123456'}, allow_redirects=False)
    assert response.status_code == 302


def test_add_cart():
    response = demoshop.post('/addproducttocart/catalog/31/1/1')
    assert response.status_code == 200


def test_delete_cart(register):
    register.open('')
    resource = demoshop.post('/addproducttocart/catalog/31/1/1')
    register.element('.ico-cart').click()
    register.element('.qty-input').clear().send_keys(0).press_enter()
    assert resource.status_code == 200


def test_computers(register):
    register.open('')
    register.element('.search-box-text').type('text').press_enter()
    register.element('.result').should(have.text('No products were found that matched your criteria.'))


def test_logout(register):
    register.open('')
    register.element('.ico-logout').click()
    response = demoshop.get('/logout', allow_redirects=False)
    assert response.status_code == 302
