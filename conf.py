# Configuration file for the Mohsen documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.mahsen81.ir

# -- Project information -----------------------------------------------------

project = 'پایتون به پارسی'
copyright = '2015, Mohsen Jabbareh Asl'
author = 'Mohsen Jabbareh Asl'

# -- General configuration ---------------------------------------------------

extensions = ["sphinxcontrib.jquery"]

templates_path = ['_templates']
exclude_patterns = []

language = 'fa'

master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_minoo_theme'
html_theme_path = ["_templates"]
html_title = 'کتاب ' + project

html_static_path = ['_static']
