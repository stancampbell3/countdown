from setuptools import setup, find_packages

setup(
    name='countdown-letters',
    version='0.1.0',
    description='A package for playing the letters round of Countdown',
    author='Stan Campbell',
    author_email='stan.campbell@seashellanalytics.com',
    url='https://CHANGEME',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'unittest',
        'Flask'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)