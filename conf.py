# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "TJ Physics Olympiad"
copyright = "%Y, TJ Physics Team Officers"
author = "TJ Physics Team Officers"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    ".venv",
    ".git",
    ".github",
    "Thumbs.db",
    ".DS_Store",
    "README.md",
    "LICENSE.md",
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "dollarmath",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = project
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

html_favicon = "_static/favicon.png"
html_show_sourcelink = False

html_theme_options = {
    # Uncomment once date is finalized
    # "announcement": "The TJ Physics Team Olympiad ends on ...",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/tjphysicsteam/tjpho",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Instagram",
            "url": "https://www.instagram.com/tjpho/",
            "icon": "fa-brands fa-instagram",
        },
        {
            "name": "Facebook",
            "url": "https://www.facebook.com/groups/tjphysicsteam/",
            "icon": "fa-brands fa-facebook-f",
        },
    ],
    "footer_start": ["copyright"],
    "footer_end": [],
}

html_sidebars = {
    "**": ["description.html"],
    # don't use description.html for the main page
    "index": [],
}

html_css_files = ["custom.css"]
