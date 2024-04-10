from setuptools import setup, find_packages


with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()
    
with open("LICENSE.txt", "r", encoding = "utf-8") as fh:
    license = fh.read()
       
NAME = "FlutterwaveDjango"
VERSION = "1.1.2"
AUTHOR = "Oladejo Sodiq Opeyemi"
AUTHOR_EMAIL = "devsurdma@gmail.com"
DESCRIPTION = "FlutterwaveDjango - A Django Integration Library for Flutterwave Payment"
URL = "https://github.com/surdma/FlutterwaveDjango"  
LICENSE = license


INSTALL_REQUIRES = [ "rave_python"]


PACKAGES = find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"])

# Setup configuration
setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url=URL,
    license=LICENSE,
    install_requires=INSTALL_REQUIRES,
    packages=PACKAGES,
)
