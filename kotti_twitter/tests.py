from kotti.tests import UnitTestBase

from kotti import get_settings
from kotti_twitter import render_profile_widget
from kotti_twitter import render_search_widget

class TestProfileWidget(UnitTestBase):
    def test_render(self):
        self.assert_(render_profile_widget(None, None).startswith('<script'))

    def test_render_settings(self):
        html = render_profile_widget(None, None)
        self.assert_(u'dnouri' not in html)
        get_settings()['kotti_twitter.profile_widget.user'] = 'dnouri'
        html = render_profile_widget(None, None)
        self.assert_(u'dnouri' in html)

    def test_render_settings_with_name(self):
        html = render_profile_widget(None, None, name='mywidget')
        self.assert_(u'dnouri' not in html)
        get_settings()['kotti_twitter.profile_widget.mywidget.user'] = 'dnouri' 
        html = render_profile_widget(None, None, name='mywidget')
        self.assert_(u'dnouri' in html)

class TestSearchWidget(UnitTestBase):
    def test_render(self):
        self.assert_(render_search_widget(None, None).startswith('<script'))

    def test_render_settings_with_name(self):
        html = render_search_widget(None, None, name='mywidget')
        self.assert_(u'dnouri' not in html)
        get_settings()['kotti_twitter.search_widget.mywidget.search'] = 'dnouri' 
        html = render_search_widget(None, None, name='mywidget')
        self.assert_(u'dnouri' in html)
