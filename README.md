# python_project_setup
How to set up a repo and file structure for automatic build, test, documentation and deployment.

**TBD: setup-fila, hva gjør packages=(...) og name()**
https://github.com/espegun/good-dev-practice/tree/master/how_to_setuptools


Since we are using `tox`, it is recommended to use the [src layout](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure).  


`__init__.py` files in all **(?)** folders under the top folder.  
`from folder.folder.module import function1, function2` To import from a project sibling folder. Within a folder, just `from .module ...`  

[Python projects](https://docs.python-guide.org/writing/structure/) Good link, use it!  
[General Python project structure](https://github.com/yngvem/python-project-structure)  
[Setup from pytest perspective](https://docs.pytest.org/en/stable/goodpractices.html)  
