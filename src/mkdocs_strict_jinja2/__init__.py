"""mkdocs-strict-jinja2."""
from __future__ import annotations

import jinja2
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files


class StrictJinja2Plugin(BasePlugin):
    """Set jinja2 environment to StrictUndefined"""

    def on_env(
        self, env: jinja2.Environment, *, config: MkDocsConfig, files: Files
    ) -> jinja2.Environment | None:
        env.undefined = jinja2.StrictUndefined
        return env
