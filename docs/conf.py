# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from pathlib import Path

# from sphinx_gallery import scrapers
from sphinx_gallery.sorting import ExampleTitleSortKey

from napari_animation._version import version as napari_animation_version

release = napari_animation_version
if "dev" in release:
    version = "dev"
else:
    version = release

# -- Project information -----------------------------------------------------

project = "napari-animation"
copyright = "2024, The napari team"
author = "The napari team"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx_external_toc",
    "myst_nb",
    "sphinx.ext.viewcode",
    "sphinx_favicon",
    "sphinx_copybutton",
    "sphinx_gallery.gen_gallery",
]

external_toc_path = "_toc.yml"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "napari_sphinx_theme"

# # Define the json_url for our version switcher.
# json_url = "https://napari.org/dev/_static/version_switcher.json"

# if version == "dev":
#     version_match = "latest"
# else:
#     version_match = release

html_theme_options = {
    "external_links": [{"name": "napari", "url": "https://napari.org"}],
    "github_url": "https://github.com/napari/napari-animation",
    "navbar_start": ["navbar-logo", "navbar-project"],
    "navbar_end": ["navbar-icon-links"],
    # "switcher": {
    #     "json_url": json_url,
    #     "version_match": version_match,
    # },
    "navbar_persistent": [],
    "header_links_before_dropdown": 6,
    "secondary_sidebar_items": ["page-toc"],
    "pygment_light_style": "napari",
    "pygment_dark_style": "napari",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_logo = "images/logo.png"
html_sourcelink_suffix = ""
html_title = "napari animation"

favicons = [
    {
        # the SVG is the "best" and contains code to detect OS light/dark mode
        "static-file": "favicon/logo-silhouette-dark-light.svg",
        "type": "image/svg+xml",
    },
    {
        # Safari in Oct. 2022 does not support SVG
        # an ICO would work as well, but PNG should be just as good
        # setting sizes="any" is needed for Chrome to prefer the SVG
        "sizes": "any",
        "static-file": "favicon/logo-silhouette-192.png",
    },
    {
        # this is used on iPad/iPhone for "Save to Home Screen"
        # apparently some other apps use it as well
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "static-file": "favicon/logo-noborder-180.png",
    },
]

html_css_files = [
    "custom.css",
]

intersphinx_mapping = {
    "python": ["https://docs.python.org/3", None],
    "numpy": ["https://numpy.org/doc/stable/", None],
    "napari_plugin_engine": [
        "https://napari-plugin-engine.readthedocs.io/en/latest/",
        "https://napari-plugin-engine.readthedocs.io/en/latest/objects.inv",
    ],
    "napari": [
        "https://napari.org/dev",
        "https://napari.org/dev/objects.inv",
    ],
}

myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "substitution",
    "tasklist",
]

myst_heading_anchors = 4
suppress_warnings = ["etoc.toctree"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".jupyter_cache",
    "jupyter_execute",
]

# def reset_napari(gallery_conf, fname):
#     from napari.settings import get_settings
#     from qtpy.QtWidgets import QApplication

#     settings = get_settings()
#     settings.appearance.theme = 'dark'

#     # Disabling `QApplication.exec_` means example scripts can call `exec_`
#     # (scripts work when run normally) without blocking example execution by
#     # sphinx-gallery. (from qtgallery)
#     QApplication.exec_ = lambda _: None


# def napari_scraper(block, block_vars, gallery_conf):
#     """Basic napari window scraper.

#     Looks for any QtMainWindow instances and takes a screenshot of them.

#     `app.processEvents()` allows Qt events to propagateo and prevents hanging.
#     """
#     imgpath_iter = block_vars['image_path_iterator']

#     if app := napari.qt.get_app():
#         app.processEvents()
#     else:
#         return ""

#     img_paths = []
#     for win, img_path in zip(
#         reversed(napari._qt.qt_main_window._QtMainWindow._instances),
#         imgpath_iter,
#     ):
#         img_paths.append(img_path)
#         win._window.screenshot(img_path, canvas_only=False)

#     napari.Viewer.close_all()
#     app.processEvents()

#     return scrapers.figure_rst(img_paths, gallery_conf['src_dir'])


sphinx_gallery_conf = {
    # path to your example scripts
    "examples_dirs": "../examples",
    "gallery_dirs": "gallery",  # path to where to save gallery generated output
    "filename_pattern": "/*.py",
    "ignore_pattern": "README.rst|/*_.py",
    "default_thumb_file": Path(__file__).parent / "images" / "logo.png",
    "plot_gallery": "'True'",  # https://github.com/sphinx-gallery/sphinx-gallery/pull/304/files
    "download_all_examples": False,
    "only_warn_on_example_error": False,
    "abort_on_example_error": True,
    #'image_scrapers': ("matplotlib", napari_scraper,),
    #'reset_modules': (reset_napari,),
    "reference_url": {"napari": None},
    "within_subsection_order": ExampleTitleSortKey,
}


def setup(app):
    """Set up docs build.

    * Ignores .ipynb files to prevent sphinx from complaining about multiple
      files found for document when generating the gallery
    * Rewrites github anchors to be comparable
    * Adds google calendar api key to meetings schedule page

    """
    app.registry.source_suffix.pop(".ipynb", None)


# linkcheck_anchors_ignore = [r'^!', r'L\d+-L\d+', r'r\d+', r'issuecomment-\d+']

# linkcheck_ignore = [
#     'https://napari.zulipchat.com/',
#     '../_tags',
#     'https://en.wikipedia.org/wiki/Napari#/media/File:Tabuaeran_Kiribati.jpg',
# ]


# def rewrite_github_anchor(app, uri: str):
#     """Rewrite anchor name of the hyperlink to github.com

#     The hyperlink anchors in github.com are dynamically generated.  This rewrites
#     them before checking and makes them comparable.
#     """
#     parsed = urlparse(uri)
#     if parsed.hostname == "github.com" and parsed.fragment:
#         for text in [
#             "L",
#             "readme",
#             "pullrequestreview",
#             "issuecomment",
#             "issue",
#         ]:
#             if parsed.fragment.startswith(text):
#                 return None
#         if re.match(r'r\d+', parsed.fragment):
#             return None
#         prefixed = parsed.fragment.startswith('user-content-')
#         if not prefixed:
#             fragment = f'user-content-{parsed.fragment}'
#             return urlunparse(parsed._replace(fragment=fragment))
#     return None
