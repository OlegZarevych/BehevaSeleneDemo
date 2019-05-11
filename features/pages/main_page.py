from selene.support.jquery_style_selectors import s, ss
from selene.bys import *
from selene.conditions import exact_text, visible, exact_texts, enabled
from selene.support.conditions import be

def search_text(text):
    s(by_css('#search_form_input_homepage')).should(be.enabled).set_value(text)
    s(by_css('#search_button_homepage')).should(be.enabled).click()