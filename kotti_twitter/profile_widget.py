from pyramid.renderers import render

from kotti.util import extract_from_settings
from kotti.views.slots import register
from kotti.views.slots import RenderRightSlot
from kotti.views.slots import RenderLeftSlot

PROFILE_WIDGET_DEFAULTS = {
    'user': 'pylons',
    'height': '300',
    'width': 'auto',
    'shell_background': '#fff',
    'shell_color': '#000',
    'tweets_background': '#fff',
    'tweets_color': '#000',
    'tweets_links': '#0000ff',
    }

def render_profile_widget(context, request, name=''):
    prefix = 'kotti_twitter.profile_widget.'
    if name:
        prefix += name + '.'
    variables = PROFILE_WIDGET_DEFAULTS.copy()
    variables.update(extract_from_settings(prefix))
    return render('templates/profile_widget.pt', variables)

def includeme(config, where=RenderRightSlot): # pragma: no cover
    register(where, None, render_profile_widget)
    
def include_left(config): # pragma: no cover
    includeme(config, RenderLeftSlot)
