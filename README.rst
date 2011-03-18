=============
kotti_twitter
=============

This is an extension to the Kotti CMS that allows you to add Twitter
widgets to your Kotti site.

`Find out more about Kotti`_

Setting up a profile widget
===========================

To set up the profile widget to display on every page in Kotti on the
right hand side, add ``kotti_twitter.profile_widget`` to the
``kotti.includes`` setting in your Paste Deploy config::

  kotti.includes = kotti_twitter.profile_widget

To set the name of the profile for which the widget is shown, set the
``kotti_twitter.profile_widget.user`` variable.  An example with some
other variables::

  kotti.includes = kotti_twitter.profile_widget
  kotti_twitter.profile_widget.user = dnouri
  kotti_twitter.profile_widget.tweets_links = #00ff00


.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
