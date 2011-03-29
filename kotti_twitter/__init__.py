from pyramid.renderers import render

from kotti.util import extract_from_settings
from kotti.views.slots import register
from kotti.views.slots import RenderRightSlot
from kotti.views.slots import RenderLeftSlot

PROFILE_WIDGET_DEFAULTS = {
    'user': 'pylons',
    'loop': 'false',
    'live': 'false',
    'height': '300',
    'width': 'auto',
    'shell_background': '#fff',
    'shell_color': '#000',
    'tweets_background': '#fff',
    'tweets_color': '#000',
    'tweets_links': '#0000ff',
    }

SEARCH_WIDGET_DEFAULTS = PROFILE_WIDGET_DEFAULTS.copy()
SEARCH_WIDGET_DEFAULTS.update({
    'search': '#pylons #pyramid',
    'interval': '6000',
    'title': 'Pylons Project news',
    'subject': '',
    'loop': 'true',
    'live': 'true',
    })

def render_profile_widget(context, request, name=''):
    prefix = 'kotti_twitter.profile_widget.'
    if name:
        prefix += name + '.'
    variables = PROFILE_WIDGET_DEFAULTS.copy()
    variables.update(extract_from_settings(prefix))
    return render('templates/profile_widget.pt', variables)

def render_search_widget(context, request, name=''):
    prefix = 'kotti_twitter.search_widget.'
    if name:
        prefix += name + '.'
    variables = SEARCH_WIDGET_DEFAULTS.copy()
    variables.update(extract_from_settings(prefix))
    return render('templates/search_widget.pt', variables)

def include_profile_widget(config, where=RenderRightSlot): # pragma: no cover
    register(where, None, render_profile_widget)

def include_profile_widget_left(config): # pragma: no cover
    include_profile_widget(config, RenderLeftSlot)

def include_search_widget(config, where=RenderRightSlot): # pragma: no cover
    register(where, None, render_search_widget)

def include_search_widget_left(config): # pragma: no cover
    include_search_widget(config, RenderLeftSlot)
