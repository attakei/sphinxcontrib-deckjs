from os import path
from sphinx_testing import with_app


here = path.join(path.dirname(__file__))
src_dir = path.join(here, 'sources')


def test_builder():
    @with_app(buildername='deckjs', srcdir=src_dir, copy_srcdir_to_tmpdir=True)
    def _test_builder(app, status, warning):
        app.build()
        html = (app.outdir / 'contents.html').read_text()
        assert 'Slide title' in html
        assert path.exists(app.outdir / '_sources') is False
        assert 'class="headerlink"' not in html
        assert 'class="reference internal"' not in html

    _test_builder()
