from selene.support.jquery_style_selectors import s, ss
from selene.bys import *
from selene.conditions import exact_text, visible, exact_texts, enabled
from selene.support.conditions import be
from selene.support.conditions import have

def result_page_contains(text):
    ss(by('.result__title .result__a > b')).filtered_by(be.visible).should(have.texts(text))