import os.path

from setuptools import setup, find_packages

HOME=os.path.expanduser('~')

setup(
    name='popup',
    version='0.1.0',
    author='Jay Edwards',
    author_email='jay@meangrape.com',
    packages=['PopupServer', 'PopupServer.test'],
    package_data={'PopupServer': ['playbooks/*/*.yaml']},
    data_files=[('%s/.popup/config/ssh_configs' % HOME, []),
    ('%s/.popup/config/ssh_control' % HOME, []), ('%s/.popup/keys' % HOME, []),
    ('%s/.popup/manifests' % HOME, [])],
    url="http://pypi.python.org/pypi/popup",
    license='BSD',
    description='Quickly setup an EC2 server running OpenVPN and other network tools',
    long_description=open('README.txt').read(),
    install_requires=[
       "ansible == 0.9",
       "boto >= 2.7.0",
       ],
    setup_requires=[
       "github-distutils >= 0.1.0",
       ],
    entry_points = {
        'console_scripts': [
            'popup = PopupServer.popup:main',
        ]
    }
)    