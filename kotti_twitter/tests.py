from pyramid.threadlocal import get_current_registry
from kotti.testing import UnitTestBase

from kotti_twitter import render_profile_widget
from kotti_twitter import render_search_widget


def settings():
    return get_current_registry().settings


class TestProfileWidget(UnitTestBase):
    def test_render(self):
        assert u'tweets_background' in render_profile_widget(None, None)

    def test_render_settings(self):
        result = render_profile_widget(None, None)
        assert result['user'] == u'pylons'
        settings()['kotti_twitter.profile_widget.user'] = 'dnouri'
        result = render_profile_widget(None, None)
        assert result['user'] == u'dnouri'

    def test_render_settings_with_name(self):
        result = render_profile_widget(None, None, name='mywidget')
        assert result['user'] == u'pylons'
        settings()['kotti_twitter.profile_widget.mywidget.user'] = 'dnouri'
        result = render_profile_widget(None, None, name='mywidget')
        assert result['user'] == u'dnouri'


class TestSearchWidget(UnitTestBase):

    def test_render_settings_with_name(self):
        result = render_search_widget(None, None, name='mywidget')
        assert result['search'] == u'#pylons #pyramid'
        settings()['kotti_twitter.search_widget.mywidget.search'] = 'dnouri'
        result = render_search_widget(None, None, name='mywidget')
        assert result['search'] == u'dnouri'
