# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['whaler']

package_data = \
{'': ['*'], 'whaler': ['static/*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'humanfriendly>=9.1,<10.0',
 'pathlib>=1.0.1,<2.0.0',
 'rich>=9.5.1,<10.0.0']

entry_points = \
{'console_scripts': ['whaler = whaler.cli:run']}

setup_kwargs = {
    'name': 'whaler',
    'version': '0.0.1',
    'description': '',
    'long_description': '# whaler\n\nA visual disk usage analyser for making docker images smaller\n',
    'author': 'alex-treebeard',
    'author_email': 'alex@treebeard.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/treebeardtech/whaler',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
