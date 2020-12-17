from setuptools import setup, find_packages

from repo_bitcoin import __version__


setup(
    name="repo-bitcoin",
    description="A classification challenge that aims at building investment strategies on cryptocurrencies",
    long_description=open("README.md").read(),
    version=__version__,
    author="Yassine DOUFANI & Hajar IBRARHI",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
    license="Appache-2.0",
