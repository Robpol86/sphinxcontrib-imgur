.. _examples:

========
Examples
========

This page shows several example use cases for the extension.

Inline Roles
============

Include text entries inline in your paragraphs. These work with images and albums.

Titles and Descriptions
-----------------------

.. code-block:: rst

    * Imgur title of the album below: :imgur-title:`a/hWyW0`
    * And the description of the animated image below: :imgur-description:`7WTPx0v`

* Imgur title of the album below: :imgur-title:`a/hWyW0`
* And the description of the animated image below: :imgur-description:`7WTPx0v`

Embedded Directives
===================

Embed Imgur albums or images using their JavaScript option. This is the same as the "Embed album" link when you view
an album on imgur.com.

Album With Details
------------------

.. code-block:: rst

    .. imgur-embed:: a/hWyW0

.. imgur-embed:: a/hWyW0

Album Without Details
---------------------

.. code-block:: rst

    .. imgur-embed:: a/9YZHA
        :hide_post_details: True

.. imgur-embed:: a/9YZHA
    :hide_post_details: True

Image With Details
------------------

.. code-block:: rst

    .. imgur-embed:: 7WTPx0v

.. imgur-embed:: 7WTPx0v

Image Without Details
---------------------

.. code-block:: rst

    .. imgur-embed:: Srt4owo
        :hide_post_details: True

.. imgur-embed:: Srt4owo
    :hide_post_details: True
