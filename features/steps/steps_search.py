from behave import step, given, then
from selene import browser
from selene import config
from selene.support.conditions import have
from pages import main_page
from pages import result_page

@given(u'Open duckduck page')
def open_page(context):
    config.browser_name = 'chrome'
    browser.open_url('http://duckduckgo.com')
    browser.wait_to(have.title('DuckDuckGo — Privacy, simplified.'))

@when(u'Search text {text}')
def search_text_from_main_page(context, text):
    main_page.search_text(text)

@then(u'first link contains {text}')
def first_link_contains_text(context, text):
    result_page.result_page_contains(text)