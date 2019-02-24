from setuptools import find_packages, setup

setup(
    name="onn_sanic",
    version="0.0.1",
    author="Stephen Onnen",
    author_email="stephen.onnen@gmail.com",
    description="Project site for Stephen Onnen",
    license="MIT",
    url="https://github.com/onnenon/onn_sanic",
    install_requires=["sanic"],
    packages=find_packages(),
)
