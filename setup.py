# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['whaler']

package_data = \
{'': ['*'], 'whaler': ['static/html.tgz']}

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
    'long_description': "# whaler\n\n[![PyPI versions](https://img.shields.io/pypi/pyversions/whaler?logo=python&logoColor=white)](https://pypi.org/project/whaler)\n[![PyPI versions](https://img.shields.io/pypi/v/whaler?logo=python&logoColor=white)](https://pypi.org/project/whaler)\n\n**What?** A command-line tool for visually investigating the disk usage of docker images\n\n**Why?** Large images are slow to move and expensive to store. They cost developer productivity by lengthening devops tasks and often contain unnecessary data\n\n**Who is this for?** Primarily for engineers working with images containing Python packages.\n\n## User Stories\n\nThis tool should allow you to answer questions such as:\n1. Which file types are occupying the most disk space?\n2. Which are my largest Python packages?\n3. What are my unknown causes of high disk usage?\n\n## Quick start\n\n```bash\npip install whaler\n```\n\n### Run against a local directory\n```\n➜ whaler .venv\nRunning bash -c cd .venv && du -a -k\nDone. Serving output at http://localhost:8000 (ctrl+c to exit)\nRunning python3 -m http.server 8000 --directory=_whaler/html\n```\n\n### Run against a docker image\n\nThe tool will pull the image first if it is not present.\n```\nwhaler --image='hl:latest' /\nRunning docker run --rm --entrypoint=du --workdir=/ hl:latest -a -k\nIgnoring what seems to be non-fatal error(s):\ndu: cannot access './proc/1/task/1/fd/4': No such file or directory\ndu: cannot access './proc/1/task/1/fdinfo/4': No such file or directory\ndu: cannot access './proc/1/fd/3': No such file or directory\ndu: cannot access './proc/1/fdinfo/3': No such file or directory\n\n\nDone. Serving output at http://localhost:8000 (ctrl+c to exit)\nRunning python3 -m http.server 8000 --directory=_whaler/html\n```\n\nDone. Serving output at http://localhost:8000 (ctrl+c to exit)\nRunning python3 -m http.server 8000 --directory=_whaler/html\n\n![HTML Report](docs/screen.png)\n\n\n## Limitations\n\n1. Platform: whaler uses `du` to gather disk usage data. It must be present in your docker image\n2. Scale: I have tested the web UI with up to 500,000 file system nodes with `du` output of up to ~100MB.\n\n## Alternatives/Complements to this tool:\n\n1. Whaler can tell you what is taking up space in the final layer of your Docker image, but you may have intermediate layers which are contributing to the image size. For diving through the layers, use [dive](https://github.com/wagoodman/dive)\n    * **Related**: read up on [multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/) to understand how to mitigate the problem of intermediate layers bloating your image.\n1. For investigating disk usage in non-docker directories, [Disk Inventory X](http://www.derlien.com/) is a great tool on OS X which I have based whaler on.",
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
