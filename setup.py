#!/usr/bin/env python
import os
import sys

from setuptools import setup


if sys.version_info < (3, 6, 3):
    print('Error: dbt-mysql-adapter does not support this version of Python.')
    print('Please upgrade to Python 3.6.3 or higher.')
    sys.exit(1)


this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()


package_name = "dbt-mysql-adapter"
package_version = "0.19.0"
description = """The MySQL adapter plugin for dbt (data build tool)"""


setup(
    name=package_name,
    version=package_version,

    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',

    author="Juliano Benvenuto Piovezan",
    author_email="piovezan.juliano@gmail.com",
    url="https://github.com/julianopiovezan/dbt-mysql-adapter",
    packages=[
        'dbt.adapters.mysql',
        'dbt.include.mysql',
        'dbt.adapters.mysql5',
        'dbt.include.mysql5',
    ],
    package_data={
        'dbt.include.mysql': [
            'macros/*.sql',
            'macros/materializations/**/*.sql',
            'dbt_project.yml',
            'sample_profiles.yml',
        ],
        'dbt.include.mysql5': [
            'macros/*.sql',
            'macros/materializations/**/*.sql',
            'dbt_project.yml',
            'sample_profiles.yml',
        ],
    },
    install_requires=[
        "dbt-core==0.19.0",
        "mysql-connector-python~=8.0.22",
        "wrapt==1.13.3",
    ],
    extras_require={
        "dev": [
            "black==21.7b0",
            "bleach>=3.3.0",
            "bump2version",
            "flake8==4.0.1",
            "pytest>=6.0.0",
            "pytest-dbt-adapter>=0.4.0",
            "rope==0.22.0",
            "tox>=3.2.0",
            "twine",
            "wemake-python-styleguide==0.0.1"
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: Apache Software License',

        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires=">=3.6.3",
)
