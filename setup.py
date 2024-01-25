from setuptools import setup

with open ("Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


AUTHOR_NAME = "Chee KaiSin"
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['STREAMLIT']


setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = "kaisin1993@hotmail.com",
    description = "A small example package for movies recommendation",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    python_requires = '>= 3.7',
    install_requires = LIST_OF_REQUIREMENTS
)