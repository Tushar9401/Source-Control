from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in source_control/__init__.py
from source_control import __version__ as version

setup(
	name="source_control",
	version=version,
	description="t",
	author="t",
	author_email="tusharthakkar1996@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
