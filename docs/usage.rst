.. _usage:

=====
Usage
=====

This page documents how to get started with the extension.

Make sure that you've already :ref:`installed <install>` it.

Configuration
=============

If you're just trying to `embed <http://imgur.com/blog/2015/04/07/embed-your-post-anywhere/>`_ albums or images in your
Sphinx documents you don't need to add anything extra to your ``conf.py``. Just include ``sphinxcontrib.imgur`` in
``extensions``.

If you'd like to use other features in this extension then you'll need to generate a "Client ID" by going to the
`Register an Application <https://api.imgur.com/oauth2/addclient>`_ page on Imgur. You'll just need the very basics. As
of this writing you put in something in Application Name (e.g. your project name or title of your documentation), set
Authorization Type to "Anonymous usage without user authorization" and whatever for your email and description.

Here is a sample file with the two things you need to do for advanced features:

.. code-block:: python

    # General configuration.
    author = 'Your Name Here'
    copyright = '2015, Your Name Here'
    exclude_patterns = ['_build']
    extensions = ['sphinxcontrib.imgur']  # Add to this list.
    master_doc = 'index'
    project = 'my-cool-project'
    release = '1.0'
    version = '1.0'

    # Options for extensions.
    imgur_client_id = 'abc123def456789'  # Add this line to conf.py.

All Config Options
==================

.. attribute:: imgur_api_cache_ttl

    *Default: 172800 seconds (2 days)*

    Time in seconds before cached Imgur API entries are considered expired. Imgur's API has a request limit (even for
    simple things like getting an image's title) so this extension caches API replies. This lets you keep making
    multiple changes in your documentation without bombarding the API. Does not apply to embedded albums/images.

.. attribute:: imgur_client_id

    Imgur API Client ID to include in request headers. Required for API calls. More information in the section above.

.. attribute:: imgur_hide_post_details

    *Default: False*

    The default value of ``hide_post_details`` in embedded albums/images. Overridden in the directive.

Roles and Directives
====================

These are the available Sphinx/RST roles and `directives <http://www.sphinx-doc.org/en/stable/rest.html#directives>`_.
To see them in action visit the :ref:`Examples` section.

.. rst:role:: imgur-title

    Display an Imgur image or album's title inline.

.. rst:role:: imgur-description

    Display an Imgur image or album's description text inline.

.. rst:directive:: imgur-embed

    Embed an Imgur image or album using Imgur's fancy javascript.

    .. attribute:: hide_post_details

        Overrides :attr:`imgur_hide_post_details` for this specific embed.