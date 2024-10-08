# py-utils

Uses a src layout, vs a flat layout

## Setting Up:
create virtual environment and install requirements.txt
install the folder py_utils as a package, with pip install -e . by either configuring the setup.cfg + pyproject.toml files OR setup.py file, for scripts inside scripts folder to import properly. Refer to this tutorial: https://medium.com/mlearning-ai/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95
*If your main entry points are ouside in the root folder, no need to do this step, simply import py-utils as a normal package.

## Useful pip commands
- python3 -m venv .venv -> create a venv
- source ./venv/scripts/activate -> activate the venv
- pip freeze file.txt -> dumps out latest installed packages to a file
- python3 -m pip install --upgrade pip setuptools wheel
- python3 -m pip install -r requirements.txt --upgrade
- pytest -> run the tests

## GitHub Workflow
Based on https://github.com/actions/starter-workflows/blob/main/ci/python-package-conda.yml

## Building 
https://packaging.python.org/en/latest/tutorials/packaging-projects/
- py -m pip install --upgrade build
- py -m build
  - This builds into dist - tar ball (src) + wheel (built distribution)
- https://test.pypi.org/
  - Setu twine (py -m pip install --upgrade twine)
- py -m twine upload --repository testpypi dist/*
- Uploads to https://test.pypi.org/project/py-utils-knaier/0.0.1/
- Can be imported via pip install -i https://test.pypi.org/simple/ py-utils-knaiera==0.0.1