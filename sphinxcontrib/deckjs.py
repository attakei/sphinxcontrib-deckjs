# -*- coding: utf-8 -*-
"""sphinxcontrib.deckjs
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :author: attakei <attakei@gmail.com>
    :copyright: attakei. All Rights Reserved.
"""
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.writers.html import HTMLTranslator


__version__ = '0.0.1'


class DeckjsBuilder(StandaloneHTMLBuilder):
    name = 'deckjs'
    copysource = False
    add_permalinks = False

    def init_translator_class(self):
        if self.translator_class is not None:
            pass
        else:
            self.translator_class = DeckjsTranslator


class DeckjsTranslator(HTMLTranslator):
    def visit_section(self, node):
        if self.section_level != 0:
            self.body.append('</section>\n')
        self.section_level += 1
        self.body.append(
            self.starttag(node, 'section', CLASS='slide'))

    def depart_section(self, node):
        self.section_level -= 1
        if self.section_level == 0:
            self.body.append('</section>\n')


def setup(app):
    """entry-point for sphinx directive."""
    app.add_builder(DeckjsBuilder)
