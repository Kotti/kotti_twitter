from kotti.util import extract_from_settings
from kotti.views.slots import assign_slot

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
    return variables


def render_search_widget(context, request, name=''):
    prefix = 'kotti_twitter.search_widget.'
    if name:
        prefix += name + '.'
    variables = SEARCH_WIDGET_DEFAULTS.copy()
    variables.update(extract_from_settings(prefix))
    return variables


def include_profile_widget(config, where='right'):  # pragma: no cover
    config.add_view(render_profile_widget,
                    name='twitter-profile',
                    renderer='templates/profile_widget.pt')
    assign_slot('twitter-profile', where)


def include_profile_widget_left(config):  # pragma: no cover
    include_profile_widget(config, 'left')


def include_search_widget(config, where='right'):  # pragma: no cover
    config.add_view(render_search_widget,
                    name='twitter-search',
                    renderer='templates/search_widget.pt')
    assign_slot('twitter-search', where)


def include_search_widget_left(config):  # pragma: no cover
    include_search_widget(config, 'left')
