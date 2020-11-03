# python_project_setup
How to set up a repo and file structure for automatic build, test, documentation and deployment.



**TBD: setup-fila, hva gjør packages=(...) og name()**<br>


Since we are using `tox`, it is recommended to use the [src layout](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure).<br/>


`__init__.py` files in all**(?)** folders under the top folder.<br/>
`from folder.folder.module import function1, function2` How to import from sibling folders in a project. From same folder, just `from .module` ...<br/> 


[General Python project structure](https://github.com/yngvem/python-project-structure)<br/>
[Setup from pytest perspective](https://docs.pytest.org/en/stable/goodpractices.html)<br/>
