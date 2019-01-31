from setuptools import setup, find_packages
import io
import os

VERSION = "0.1"


def get_long_description():
    with io.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="dbf-to-sqlite",
    description="CLCLI tool for converting DBF files (dBase, FoxPro etc) to SQLite",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    version=VERSION,
    license="Apache License, Version 2.0",
    packages=find_packages(),
    install_requires=["dbf==0.97.11", "click", "sqlite_utils"],
    entry_points="""
        [console_scripts]
        dbf-to-sqlite=dbf_to_sqlite.cli:cli
    """,
    url="https://github.com/simonw/dbf-to-sqlite",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Database",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
