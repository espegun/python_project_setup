# python_project_setup
How to set up a repo and file structure for automatic build, test, documentation and deployment.

## The most simple approach (__init__.py only, no setup.py)
Adding a `__init__.py` file to a directory, turns it into a package. Files in that directory can then be imported using a statement like the below.
`from dirname.pymodule import function_name`. Make sure the folder doesn't have the same name as an existing package, e.g. `code`.  
Note that this notation should also be used when importing module is the same directory/package. If not, it won't be found when running tests.

This also works from parallell/sibling directories, like a `tests` directory.
Run `pytest`in the `simple_packages` directory to test this.

See this [article](https://codeburst.io/creating-local-python-packages-with-init-py-aa19f1e9e80f).  

## The setup.py

**TBD: setup-fila, hva gjør packages=(...) og name()**
https://github.com/espegun/good-dev-practice/tree/master/how_to_setuptools


Since we are using `tox`, it is recommended to use the [src layout](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure).  


`__init__.py` files in all **(?)** folders under the top folder.  
`from folder.folder.module import function1, function2` To import from a project sibling folder. Within a folder, just `from .module ...`  

[Python projects](https://docs.python-guide.org/writing/structure/) Good link, use it!  
[General Python project structure](https://github.com/yngvem/python-project-structure)  
[Setup from pytest perspective](https://docs.pytest.org/en/stable/goodpractices.html)  
