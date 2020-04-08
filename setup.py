from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="stark",
    version="0.1.0",
    author="Iheb Haboubi",
    author_email="iheb.haboubi56@gmail.com",
    description="stark generates random and strong passwords",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Iheb-Haboubi/stark",
    download_url="https://github.com/Iheb-Haboubi/stark/tarball/0.0.1",
    packages=find_packages(exclude=["tests"]),
    entry_points={"console_scripts": ["stark=stark.cli:main"],},
    license="MIT",
    keywords=["password", "random", "generator"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3.6"
        "Programming Language :: Python :: 3.7"
        "Programming Language :: Python :: 3.8"
        "Operating System :: OS Independent",
    ],
)
