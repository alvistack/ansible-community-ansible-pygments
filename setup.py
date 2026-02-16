# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ansible_pygments']

package_data = \
{'': ['*']}

install_requires = \
['pygments>=2.4.0']

entry_points = \
{'pygments.lexers': ['Ansible-output = '
                     'ansible_pygments.lexers:AnsibleOutputLexer',
                     'ansible-output = '
                     'ansible_pygments.lexers:AnsibleOutputLexer'],
 'pygments.styles': ['Ansible = ansible_pygments.styles:AnsibleStyle',
                     'ansible = ansible_pygments.styles:AnsibleStyle']}

setup_kwargs = {
    'name': 'ansible-pygments',
    'version': '0.1.2',
    'description': 'Tools for building the Ansible Distribution',
    'author': 'Felix Fontein',
    'author_email': 'felix@fontein.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ansible-community/ansible-pygments',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.0',
}


setup(**setup_kwargs)
