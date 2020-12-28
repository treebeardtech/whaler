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
    'version': '0.1',
    'description': '',
    'long_description': '# whaler\n[![codecov](https://codecov.io/gh/treebeardtech/whaler/branch/main/graph/badge.svg?token=9GuDM35FuO)](https://codecov.io/gh/treebeardtech/whaler)\n[![PyPI versions](https://img.shields.io/pypi/pyversions/whaler?logo=python&logoColor=white)](https://pypi.org/project/whaler)\n[![PyPI versions](https://img.shields.io/pypi/v/whaler?logo=python&logoColor=white)](https://pypi.org/project/whaler) [![Slack](https://img.shields.io/static/v1?label=slack&message=join&color=green&logo=slack)](https://join.slack.com/t/treebeard-entmoot/shared_invite/zt-jyvuqted-xBjnbvlfcu5P2ltBvn1~mg)\n\n**What?** Pytest plugin for testing and releasing notebook documentation\n\n**Why?** To raise the quality of scientific material through better automation\n\n**Who is this for?** Research/Machine Learning Software Engineers who maintain packages/teaching materials with documentation written in notebooks.\n\n## Functionality\n\n1. Executes notebooks using pytest and nbclient, allowing parallel notebook testing\n2. Optionally writes back to the repo, allowing faster building of [nbsphinx](https://github.com/spatialaudio/nbsphinx) or [jupyter book](https://github.com/executablebooks/jupyter-book) docs\n3. Optionally builds an HTML report using [jupyter-book](https://github.com/executablebooks/jupyter-book) of the test run which can be uploaded to hosting providers such as Netlify.\n\n**See [docs](https://treebeardtech.github.io/whaler) to get started.**\n<br/>\n<br/>\n\n## See Also\n\n* [whaler-action](https://github.com/treebeardtech/whaler-action)\n\n### HTML Report Example\n\n![HTML Report](docs/screen.png)\n\n\n## Developing\n\n### Install local package\n```\npoetry install -E html\n```\n\n### Activate shell\n```\npoetry shell\n```\n\n### Run static checks\n```\npre-commit run --all-files\npre-commit install\n```\n\n### Run tests\n```\npytest\n```\n\n',
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
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
