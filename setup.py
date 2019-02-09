import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# https://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files
# URL above is for setup config tutorial.

setup(
        name = 'user-mgnt',
        version= '0.1',
        packages = find_packages(),
        license = 'MIT', 
        description = 'A simple Admin Management for User Registrations,Logins,Logouts,etc.',
        long_description = README,
        url='http://jojosiao.com',
        author='Jojo Siao',
        author_email = 'joubertsiao@gmail.com',
        classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Framework :: Django :: X.Y',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'OPerating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.7',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    )




