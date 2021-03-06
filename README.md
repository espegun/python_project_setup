# python_project_setup
How to set up a repo and file structure for automatic build, test, documentation and deployment.

# Modules, packages and importing

https://www.programiz.com/python-programming/modules
https://www.programiz.com/python-programming/package


## The most simple approach (\_\_init\_\_.py only, no setup.py)
See the example files in `simple_packages/`. Run `pytest`from that directory and also run `my_package/script.py` separately. Everything should work.  

Adding a `__init__.py` file to a directory, turns it into a package. Files in that directory can then be imported from *outside the package* (e.g. a sibling `test` directory) using a statement like:  
`from my_package.my_module import my_function`. 
*Within* the package, only use from `from my_module import my_function`.  
Make sure the folder doesn't have the same name as an existing package, e.g. `code`.  

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
[How to make Python packages](https://link.medium.com/NvGP2II99eb)  
https://python-packaging.readthedocs.io/en/latest/index.html  
