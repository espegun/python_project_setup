# How to tox

## The purpose
tox aims to automate and standardize testing in Python. It creates virtual environments with the python versions and packages your require and runs the test in those environments. It may also serve as a frontend toward CI tools.

## How does it work?
Create a `tox.ini` file in the same (base) folder as `setup.py` (which is required). `tox.ini` defines the Python versions and dependencies (of what..?)

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

`$ pip install tox`<br/>
`$ tox`

## Useful commands
`...`  .... <br/>
`...`  .... <br/>
`rm -rf .tox .build_venv` Simen's triks for å rydde opp i gammelt ræl. Funker overraskende ofte ved `InvocationError`.<br />


## Useful links
[Readthedocs - tox with simple example **WIP**](https://tox.readthedocs.io/en/latest/)<br/>
https://pypi.org/project/tox/<br/>


