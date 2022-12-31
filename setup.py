from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in impact_trades_bd_ltd/__init__.py
from impact_trades_bd_ltd import __version__ as version

setup(
	name="impact_trades_bd_ltd",
	version=version,
	description="Customization for IMPACT TRADES BD LTD.",
	author="Mainul Islam",
	author_email="mainulkhan94@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
