1. Install pipenv:
```
    pip install pipenv
```
2. Activate virtualenv:
```
    pipenv shell
```
3. Ensure that libs are installed:
```
    pipenv sync
```
4. Execute tests:
```
    python -m pytest -v --color=yes tests/
```