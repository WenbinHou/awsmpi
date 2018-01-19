#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='awsmpi',
    version='1.4-alpha',
    author="Wenbin Hou",
    author_email="catchyrime@fastmail.com",
    description="Manage mpi cluster on AWS.",
    long_description="This is for team-wise internal use only.",
    license="AGPLv3",
    keywords="aws mpi",
    url="https://github.com/WenbinHou/awsmpi",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'awsmpi = awsmpi.entrypoint:entrypoint',
        ]
    },
    install_requires=["boto3", "paramiko", "awscli"],
    package_data={
        '': ['*.md'],
        'awsmpi': ['*.sh', '*.py'],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
)
