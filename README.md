# pycounts

Calculate word counts in a text file!

## Installation

Clone the repository and install using [Poetry](https://python-poetry.org/):

```bash
git clone https://github.com/charlotter1277/pycounts.git
cd pycounts
poetry install
```

## Usage
1. Activate the Poetry shell:
```
poetry shell
```
2. Create a sample text file (e.g., using the Zen of Python):
```
python -c "import this" > zen.txt
```
3. Run pycounts in Python:
```
from pycounts.pycounts import count_words

counts = count_words("zen.txt")
print(counts) 
```
## Usage
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
