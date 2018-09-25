from distutils.core import setup
from setuptools import find_packages


app_id = "common"
app_name = "blueking-common"
app_description = "Blueking common package."
app_version = __import__(app_id).__version__
app_requires = [
]


setup(name=app_name,
      description=app_description,
      version=app_version,
      url="http://git.dev.cnicg.cn/blueking/"+app_name,
      packages=find_packages(exclude=["tests"]),
      install_requires=app_requires)
