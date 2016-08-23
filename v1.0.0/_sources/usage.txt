.. _usage:

=====
Usage
=====

This page documents how to get started with the extension.

Installation
============

Install the extension with pip:

.. code:: bash

    pip install sphinxcontrib-imgur

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

.. confval:: imgur_api_cache_ttl

    *Default: 172800 seconds (2 days)*

    Time in seconds before cached Imgur API entries are considered expired. Imgur's API has a request limit (even for
    simple things like getting an image's title) so this extension caches API replies. This lets you keep making
    multiple changes in your documentation without bombarding the API. Does not apply to embedded albums/images.

.. confval:: imgur_api_test_response

    Unless you're developing a Sphinx extension you won't need this.

    If defined, should be a nested dictionary. Keys are Imgur image or album (starting with ``a/``) IDs, values are
    dictionaries whose keys are "title", "description", and other API reply fields and values are what you'd expect. If
    this option is defined, the Imgur API will always be skipped and any missing Imgur IDs will cause ``KeyError`` to be
    raised.

.. confval:: imgur_client_id

    Imgur API Client ID to include in request headers. Required for API calls. More information in the section above.

.. confval:: imgur_hide_post_details

    *Default: False*

    The default value of ``hide_post_details`` in embedded albums/images. Overridden in the directive.
