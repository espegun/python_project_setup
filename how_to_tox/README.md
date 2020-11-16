# How to tox

## The purpose
tox aims to automate and standardize testing in Python, standardize as in control all the process input variables to create a reproducable and precise testing and build process. It creates virtual environments with the python versions and packages your require and runs the test in those environments. It may also serve as a frontend toward CI tools.

## How does it work?
1. Creates a lot of virtual environments.
2. Install dependencies of each of the environments.
3. Run setup commands.
4. Returns the results from each environment to the user.
This is all defined in `tox.ini`, which should be created in the same (base) folder as `setup.py` (which is a required file). All the magic happens in the `.tox` folder.

As written [here](https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/), you may think of this as the following.
- `virtualenv .tox/my_env`
- `source .tox/my_env/activate`  
- `(my_env) pip install some dependencies`
- `(my_env) .tox/my_env/prepare_something.sh`
- `(my_env) pytest .tox/my_env/tests_dir`

**HERE WE ARE.**


`tox.ini` defines the Python versions and dependencies **(of what..?)**. Does all packages used needs to be defined in `deps` - what about using `requirements.txt`?

`commands` can include any command(?), not just test related. 


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
`$ pip install tox` Install tox.<br/>
`$ python3 -m pip install --upgrade tox` Keep it updated.<br/>
`$ tox --version` Check version. <br/>
`$ tox` Run the commands defined in `tox.ini`.<br/>
`$ rm -rf .tox .build_venv` Simens triks for å rydde opp i gammelt ræl med test og bygg. Funker overraskende ofte.<br/>

## Useful links
[Readthedocs - tox with simple example](https://tox.readthedocs.io/en/latest/)  
https://pypi.org/project/tox/  
[Tox tutorial with explanations](https://christophergs.com/python/2020/04/12/python-tox-why-use-it-and-tutorial/) Really intuitive explanation. Use this.  
[Comprehensive tutorial](https://www.seanh.cc/2018/09/01/tox-tutorial/)  
