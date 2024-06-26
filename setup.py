from setuptools import setup, find_packages

setup(
    name='datavalidator',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='SkyShineTH',
    author_email='_',
    description='A simple data validation library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SkyShineTH/pyEazyValidationD',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)