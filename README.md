# Python_0

A collection of my experiences and test experiments with Python (Pytest)

## Commands used

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
