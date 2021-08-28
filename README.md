# PRP-Connector

![GitHub](https://img.shields.io/github/license/manuelbieri/PRP-APIConnect?label=License)
![GitHub repo size](https://img.shields.io/github/repo-size/manuelbieri/PRP-APIConnect)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/manuelbieri/PRP-APIConnect)
![Lines of code](https://img.shields.io/tokei/lines/github/manuelbieri/PRP-APIConnect)
![GitHub last commit](https://img.shields.io/github/last-commit/manuelbieri/PRP-APIConnect)
![CI - Tests](https://github.com/manuelbieri/PRP-APIConnect/actions/workflows/ci.yml/badge.svg)
![GitHub Release Date](https://img.shields.io/github/release-date/manuelbieri/PRP-APIConnect)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/manuelbieri/PRP-APIConnect)
![PyPi](https://github.com/manuelbieri/PRP-APIConnect/actions/workflows/pypi.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/PRPConnector)
![GitHub deployments](https://img.shields.io/github/deployments/manuelbieri/PRP-APIConnect/github-pages?label=docs)

### Installation
Install the current release over [PyPI](https://pypi.org/project/PRPConnector/):

  ```
  $ pip install PRPConnector
  ```
  
Clone the whole [repository](https://github.com/manuelbieri/PRP-APIConnect) for the latest version:

  ```
  $ git clone https://github.com/manuelbieri/PRP-APIConnect.git
  ```

### Documentation

The code documentation is hosted on [github.io/PRP-APIConnect](https://manuelbieri.github.io/PRP-APIConnect/).

### Example
[ToDo Connector](PRPConnector/Connector.py)
```
import PRPConnector.ToDoConnector as Connector

connection: Connector.ToDoConnector = Connector.ToDoConnector('username', 'password', 'domain_url')
connection.get_all_todo()
```


[Basic Connector](PRPConnector/Connector.py)
```
import PRPConnector.Connector as Connector

connection: Connector.PRPConnector = Connector.PRPConnector('username', 'password', 'domain_url')
connection.get_all('todo')
```
See the [documentation](https://manuelbieri.github.io/PRP-APIConnect/) for further methods.
