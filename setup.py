from setuptools import setup, find_packages

setup(
    name="my_python_app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "flask",
    ],
)
