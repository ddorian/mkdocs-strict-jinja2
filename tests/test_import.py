"""Test mkdocs-strict-jinja2."""

import mkdocs_strict_jinja2


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(mkdocs_strict_jinja2.__name__, str)
