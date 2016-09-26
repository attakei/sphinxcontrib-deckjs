from os import path
from sphinx_testing import with_app


here = path.join(path.dirname(__file__))
src_dir = path.join(here, 'sources')


def test_builder():
    @with_app(buildername='deckjs', srcdir=src_dir, copy_srcdir_to_tmpdir=True)
    def _test_builder(app, status, warning):
        app.build()

    _test_builder()
