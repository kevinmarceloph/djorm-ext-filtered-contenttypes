from setuptools import setup, find_packages

description="""
GenericForeignKey with filtering capabilities for Django ORM + PostgreSQL
"""

setup(
    name = "djorm-ext-filtered-contenttypes",
    version = '0.1.1',
    url = 'https://github.com/mpasternak/djorm-ext-filtered-contenttypes',
    license = 'MIT',
    platforms = ['OS Independent'],
    description = description.strip(),
    author = 'Michal Pasternak',
    author_email = 'michal.dtz@gmail.com',
    maintainer = 'Michal Pasternak',
    maintainer_email = 'michal.dtz@gmail.com',
    packages = find_packages(),
    include_package_data = False,
    install_requires = [],
    zip_safe = False,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ]
)