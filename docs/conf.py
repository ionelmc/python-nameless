extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
source_suffix = ".rst"
master_doc = "index"
project = "Nameless"
year = "2024"
author = "Ionel Cristian Maries"
copyright = f"{year}, {author}"
version = release = "0.0.0"

pygments_style = "trac"
templates_path = ["."]
extlinks = {
    "issue": ("https://github.com/ionelmc/python-nameless/issues/%s", "#%s"),
    "pr": ("https://github.com/ionelmc/python-nameless/pull/%s", "PR #%s"),
}

html_theme = "furo"
html_theme_options = {
    "source_repository": "https://github.com/ionelmc/python-nameless/",
    "source_branch": "main",
    "source_directory": "docs/",
    "footer_icons": [
        {
            "url": "https://github.com/ionelmc/python-nameless/",
            "html": "github.com/ionelmc/python-nameless",
        },
    ],
}

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_short_title = f"{project}-{version}"

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
