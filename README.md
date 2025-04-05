# pycounts

Calculate word counts in a text file!

## Installation

You can either clone the repository and install with [Poetry](https://python-poetry.org/):

```bash
git clone https://github.com/charlotter1277/pycounts.git
cd pycounts
poetry install
```

Or install the package from TestPyPI:
```bash
pip install -i https://test.pypi.org/simple/ pycounts-charlotter1277
```


## Usage
### Option 1: From the Poetry shell (recommended for development) 

```
poetry shell
```

Create a sample text file (e.g., using the Zen of Python):

```
python -c "import this" > zen.txt
```

Run pycounts in Python:

```
from pycounts.pycounts import count_words

counts = count_words("zen.txt")
print(counts) 
```
### Option 2: From anywhere (if installed via pip from TestPyPI)
```
python
>>> from pycounts.pycounts import count_words
>>> count_words("zen.txt")
```

## Tests
Tests are written using pytest. To run them:
```
poetry run pytest
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pycounts` was created by Charlotte Ren. It is licensed under the terms of the MIT license.

## Credits

`pycounts` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
