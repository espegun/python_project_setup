# How to GitHub Actions

## The purpose
Automated testing, building and deployment which mean those processes are all done easier, quicker and more repeatable.
There are templates for doing Python build, building and deploying Docker images to services such as EC2.

## How does it work?
[**Events**](https://help.github.com/en/actions/reference/events-that-trigger-workflows) like commit, opening or closing a pull requests may trigger the start of a workflow.<br/>
**Jobs** are actions like running tests, building containers or deploying those to the production environment.<br/>
**Workflows** are composed on a number of jobs.<br/>

GitHub looks for .yaml files in the `.github/workflows` directory.


## Useful commands
`$ ...` Some comment<br/>

## Useful links
[Tutorial](https://github.com/padok-team/github-actions-tutorial)<br/>
[Learn Github Actions](https://docs.github.com/en/free-pro-team@latest/actions/learn-github-actions)<br/>
[GitHub: GitHub Actions quickstart](https://docs.github.com/en/free-pro-team@latest/actions/quickstart)<br/>
[GitHub: Bulding and testing Python](https://docs.github.com/en/free-pro-team@latest/actions/guides/building-and-testing-python) - has a good [template](https://github.com/actions/starter-workflows/blob/main/ci/python-package.yml) for Python projects.<br/>
There are also lots of good examples under **Actions** --> **Get started with GitHub Actions** inside the GitHub GUI.<br/>
