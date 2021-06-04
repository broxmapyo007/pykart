from setuptools import setup

with open("README.md","r") as f:
    README=f.read()
setup(
    name = "pykart",
    version = '0.0.1',
    description = "pykart is module which help to fetch product-data from ecommerce website [flipkart]",
    long_description=README,
    long_description_content_type="text/markdown",
    py_modules = ["pykart"],
    package_dir = {'':'src'},
    url=""
    author="Adesh Dangi",
    author_email="adeshdangi104@gmail.com",
    classifiers = [
        "Programming Language :: Python ::3",
        "Programming Language :: Python ::3.6",
        "Programming Language :: Python ::3.7",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],

    install_requires=["requests","bs4","prettytable"],
    extras_requir={
        "dev":[
            "pytest>=3.7",
        ]
    }

)
