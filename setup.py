import os
from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='django-h2-push',
    version='0.1a1',
    description="A django app that assists with generating HTTP/2 Server Push "
                "headers for reverse proxies, such as h2o and apache",
    long_description=read('README.md'),
    author="Anthony King",
    author_email="anthony.king@fundingoptions.com",
    license="GPLv3",
    url="https://github.com/FundingOptions/django-h2-push",
    packages=['django_h2_push'],
    install_requires=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5"
    ]
)
