# Python - Pytest

A collection of my experiences and test experiments with Python (Pytest):  
- [my_test.py](https://github.com/fiszym/Pytest_Automated_Testing/blob/ec38a689568d518c8f200f19fa589b38f1aa1e04/my_test.py) - set of tests regarding CSV file verification
- [basic_code_example.py](https://github.com/fiszym/Pytest_Automated_Testing/blob/fa02f8a587083143b7503e6ea3ae92cce3970b0c/basic_code_example.py) - example of code demonstration

## Commands used in project

### Virtual environment

- make v. environment
  `python -m venv venv`
- activatee v.environment
  `venv\Scripts\activate.bat`
- requirements installation
  `pip install -r ./requirements/requirements.txt`
- formatter 'Black' installation
  `pip install black`

### Pytest

- running tests
  `python -m pytest`
- test with extended report 'verbose'
  `python -m pytest -v`

### Black

- running black manually
  `black . `

- modify lines in settings.json

```
{
"editor.formatOnSave": true,
"python.formatting.provider": "black"
}
```

- edit project settings in pyproject.toml

```
[tool.black]
line-length = 119
```
