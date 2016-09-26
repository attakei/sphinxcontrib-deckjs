# -*- coding: utf-8 -*-
"""sphinxcontrib.deckjs
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :author: attakei <attakei@gmail.com>
    :copyright: attakei. All Rights Reserved.
"""
from sphinx.builders.html import StandaloneHTMLBuilder


__version__ = '0.0.1'


class DeckjsBuilder(StandaloneHTMLBuilder):
    name = 'deckjs'


def setup(app):
    """entry-point for sphinx directive."""
    app.add_builder(DeckjsBuilder)
