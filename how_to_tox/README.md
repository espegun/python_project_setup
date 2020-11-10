# How to tox

## The purpose
tox aims to automate and standardize testing in Python. It creates virtual environments with the python versions and packages your require and runs the test in those environments. It may also serve as a frontend toward CI tools.

## How does it work?
Create a `tox.ini` file in the same (base) folder as `setup.py` (which is a required file). 

`tox.ini` defines the Python versions and dependencies (of what..?). Does all packages used needs to be defined in `deps` - what about using `requirements.txt`?




**TBD: MASSE BRA GREIER I opening_hours tox.ini og pyprojcet.toml.**


```
[tox]
envlist = py27,py37

[testenv]
# install pytest in the virtualenv where commands will be executed
deps = pytest
commands =
    # NOTE: you can run any command line tool here - not just tests
    pytest
```
Python-versions (and packages??) needs to be installed globally or it will fail.

## Useful commands
`$ pip install tox` Install.<br/>
`$ python3 -m pip install --upgrade tox` Remember, your need an updated tox  .... <br/>

`$ tox`
`tox --version`  .... <br/>
`rm -rf .tox .build_venv` Simen's triks for å rydde opp i gammelt ræl. Funker overraskende ofte ved `InvocationError`.<br />


## Useful links
[Readthedocs - tox with simple example **WIP**](https://tox.readthedocs.io/en/latest/)<br/>
https://pypi.org/project/tox/<br/>


