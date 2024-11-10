# cookie-py-template

This package is based on [cookiecutter](https://github.com/cookiecutter/cookiecutter) to create a python package skeleton. The project uses a src, tests, docs layout to structure the relevant parts of a python project. With this template you are able to create a python package with the pyproject.toml covering everything you need for
* packaging
* testing
* linting
* formatting
* documentation

## Usage
The easiest way to use this template is with [cruft](https://github.com/cruft/cruft#installation) (`pip3 install cruft`).
    
```bash
cruft create https://github.com/42nick/cookie-py-template 
```
or
```bash
python3 -m cruft create https://github.com/42nick/cookie-py-template
```

You can also checkout the version of this repository that is handled with poetry via
```bash
python3 -m cruft create https://github.com/42nick/cookie-py-template -c feat/poetry
```

If you have this repository already locally you can use the following command to update the template:
```bash
cruft create /path/to/your/local/cookie-py-template
```


You will be guided through a set of questions to create your project. If you just one want to try it out you can leave everything as default (without the fear of having a washing machine bought :grin:).

## Features

### Packaging
Installation of the project with the following command will install all the dependencies for the project and the development environment.
```bash
pip install -e .[dev]
``` 

### Testing
Tox is used to manage the testing environment and ensuring usibility across different python versions. To run the tests you can use the following command:
```bash
tox
```

To run tests for your current version simply run pytest. You will find a report folder in the root of the project with the coverage report visualizing all lines of code that are covered by the tests (see reports/html/index.html).

### Documentation
The docs can be generated with the following command:
```bash
sphinx-build -b html docs/source docs/build
```
You will find the generated documentation in the docs/build folder and you can open the index.html to view the documentation.