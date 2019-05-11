from behave import step, given, then
from selene import browser
from selene import config
from selene.support.conditions import have

@given(u'Open duckduck page')
def open_page(context):
    config.browser_name = 'chrome'
    browser.open_url('http://duckduckgo.com')
    browser.wait_to(have.title('DuckDuckGo — Privacy, simplified.'))