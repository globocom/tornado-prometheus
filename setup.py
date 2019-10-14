# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

tests_require = [
    'nose',
    'coverage',
    'flake8',
]

setup(
    name='tornado-prometheus',
    version='0.1.0',
    description="HTTP metrics for a tornado application",
    long_description=open('README.rst').read(),
    keywords='prometheus tornado',
    author=u'Globo.com',
    author_email='backstage@corp.globo.com',
    url='https://github.com/globocom/tornado-prometheus',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(
        exclude=(
            'tests',
        ),
    ),
    include_package_data=True,
    install_requires=[
        'tornado>=4.0',
        'prometheus-client==0.7.1',
    ],
    extras_require={
        'tests': tests_require,
    },
)
