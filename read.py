#!/usr/bin/env python

''' Simple script to auto-generate the README.md file for the project.
'''
from __future__ import print_function
import os
import json


HEADER = '''# awesome-dev.to <img src="https://d2fltix0v2e0sb.cloudfront.net/dev-badge.svg" alt="DEV Community" height="30" width="30">
> A collection of awesome blog series on [DEV.to](https://dev.to/)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/Bhupesh-V/awesome-dev.to/blob/master/LICENSEs)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/topics/awesome)

---
'''

FOOTER = '''---

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE) file for details.

## Contributing

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
		for key in sorted(data_dict["series"]):
			file_.write('| [{0}]({1}) |{2}|\n'.format(key["Series-Title"],key["link"],key["author"]))
		file_.write('\n' + FOOTER)


if __name__ == '__main__':
    data = read_data()
    update_readme(data)
    #os.system('git add README.md')