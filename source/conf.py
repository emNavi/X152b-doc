# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'X152b应用开发指南'
copyright = '2024, hao'
author = 'hao'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'cn'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_sidebars = {
    "**": ["sidebar-nav-bs", "sidebar-ethical-ads"]
}
html_theme_options = {
   "show_nav_level": 0
}

html_theme_options = {
    "logo": {
        "text": "X152b应用开发文档",
        "image_dark": "_static/logo-dark.svg",
    },
    }