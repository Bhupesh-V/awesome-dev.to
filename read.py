#!/usr/bin/env python3

''' Simple script to auto-generate the README.md file for the project.
'''
from __future__ import print_function
import os
import json


HEADER = '''
<h1 align="center">awesome-dev.to <img src="https://d2fltix0v2e0sb.cloudfront.net/dev-badge.svg" alt="DEV Community" height="30" width="30"></h1>

---

<p align="center">
  
  <a href="https://github.com/topics/awesome">
    <img alt="awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" target="_blank" />
  </a>
  <a href="http://makeapullrequest.com">
    <img alt="License: MIT" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" target="_blank" />
  </a>
  <a href="https://github.com/Bhupesh-V/awesome-dev.to/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/apm/l/atomic-design-ui.svg?" target="_blank" />
  </a>
  <a href="https://twitter.com/bhupeshimself">
    <img alt="Twitter: bhupeshimself" src="https://img.shields.io/twitter/follow/bhupeshimself.svg?style=social" target="_blank" />
  </a>
</p>

> A collection of awesome blog series on [DEV.to](https://dev.to/).
'''

FOOTER = '''---

## :memo: License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE) file for details.

## Author

:bust_in_silhouette: **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- Github: [@Bhupesh-V](https://github.com/Bhupesh-V)
- DEV: [@bhupesh](https://dev.to/bhupesh)

## :wave: Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) for the process for submitting pull requests to us.

'''

def read_data():
	with open('series.json') as json_file:  
		data = json.load(json_file)
	return data


def update_readme(data_dict):
	with open('README.md', 'w') as file_:
		file_.write(HEADER)
		file_.write('\n')
		file_.write('| Series | Author |\n')
		file_.write('|--------|--------|\n')
		for key in data_dict["series"]:
			file_.write('| [{0}]({1}) |{2}|\n'.format(key["Series-Title"],key["link"],key["author"]))
		file_.write('\n' + FOOTER)


if __name__ == '__main__':
    data = read_data()
    update_readme(data)
    #os.system('git add README.md')