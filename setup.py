from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except:
        pass

setup(
    name='iterapi',
    version='1.2.1', 
    description='Python API to student portal of ITER',

    long_description=readme(),  
    long_description_content_type='text/markdown', 

    url='https://github.com/SubhrajitPrusty/iterapi',  
    author='Subhrajit Prusty',  
    author_email='subhrajit1997@gmail.com',

    setup_requires=['setuptools>=38.6.0'],
    
    classifiers=[  
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='api ITER development', 
    license = 'MIT',
    packages=['iterapi'], 
    install_requires=['requests'], 
)
