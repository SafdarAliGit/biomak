from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in biomak/__init__.py
from biomak import __version__ as version

setup(
	name="biomak",
	version=version,
	description="This is biomak",
	author="TechVentures",
	author_email="safdar211@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
