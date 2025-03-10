# SPDX-License-Identifier: BSD-2-Clause

import datetime
from pathlib import Path

from torii_usb import __version__ as torii_usb_version

ROOT_DIR = (Path(__file__).parent).parent

project   = 'Torii-USB'
version   = torii_usb_version
release   = version.split('+')[0]
copyright = f'{datetime.date.today().year}, Shrine Maiden Heavy Industries'
language  = 'en'

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.doctest',
	'sphinx.ext.githubpages',
	'sphinx.ext.graphviz',
	'sphinx.ext.intersphinx',
	'sphinx.ext.napoleon',
	'sphinx.ext.todo',
	'sphinxcontrib.mermaid',
	'myst_parser',
	'sphinx_inline_tabs',
	'sphinxext.opengraph',
]


source_suffix = {
	'.rst': 'restructuredtext',
	'.md': 'markdown',
}

pygments_style              = 'monokai'
autodoc_member_order        = 'bysource'
autodoc_docstring_signature = False
graphviz_output_format      = 'svg'
todo_include_todos          = True

intersphinx_mapping = {
	'python': ('https://docs.python.org/3', None),
	'torii': ('https://torii.shmdn.link/', None),
	'usb_construct': ('https://usb-construct.shmdn.link/', None)
}

napoleon_google_docstring              = True
napoleon_numpy_docstring               = True
napoleon_use_ivar                      = True
napoleon_use_admonition_for_notes      = True
napoleon_use_admonition_for_examples   = True
napoleon_use_admonition_for_references = True

myst_heading_anchors = 3

html_baseurl     = 'https://torii-usb.shmdn.link'
html_theme       = 'furo'
html_copy_source = False

html_theme_options = {
	'top_of_page_buttons': [],
}

html_static_path = [
	'_static'
]

html_css_files = [
	'css/styles.css'
]

# OpenGraph config bits
ogp_site_url = html_baseurl
ogp_image    = f'{html_baseurl}/_images/og-image.png'

autosectionlabel_prefix_document = True
