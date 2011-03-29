=============
kotti_twitter
=============

This is an extension to the Kotti CMS that allows you to add Twitter
widgets to your Kotti site.

`Find out more about Kotti`_

Setting up a profile widget
===========================

To set up the profile widget to display on every page in Kotti on the
right hand side, add ``kotti_twitter.include_profile_widget`` to the
``kotti.includes`` setting in your Paste Deploy config::

  kotti.includes = kotti_twitter.include_profile_widget

To set the name of the user for which the widget is shown, set the
``kotti_twitter.profile_widget.user`` variable.  An example with some
other variables::

  kotti.includes = kotti_twitter.include_profile_widget
  kotti_twitter.profile_widget.user = dnouri
  kotti_twitter.profile_widget.loop = true
  kotti_twitter.profile_widget.tweets_links = #00ff00

Setting up a search widget
==========================

The search widget is very similar to the profile widget, but instead
of a ``user``, it expects a ``search``.  An example configuration::

  kotti.includes = kotti_twitter.include_search_widget
  kotti_twitter.search_widget.search = #pylons #pyramid
  kotti_twitter.search_widget.title = Pylons Project news


.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
