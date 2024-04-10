
from setuptools import setup, find_packages

# Define library metadata
NAME = "FlutterwaveDjango"
VERSION = "1.1.0"
AUTHOR = "Oladejo Sodiq Opeyemi"
AUTHOR_EMAIL = "devsurdma@gmail.com"
DESCRIPTION = "FlutterwaveDjango - A Django Integration Library for Flutterwave Payment"
URL = "https://github.com/surdma/FlutterwaveDjango"  
LICENSE = "MIT"  # Replace with your chosen license


INSTALL_REQUIRES = [ "djangorestframework","decouple","rave_python","python-dotenv"]


PACKAGES = find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"])

# Setup configuration
setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url=URL,
    license=LICENSE,
    install_requires=INSTALL_REQUIRES,
    packages=PACKAGES,
)
