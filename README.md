#Installation guide with pipevn
(if you're not able to use pipenv please use requirements.txt for you virtualenv)

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
5. (optional) Execute main.py to demonstrate how to timeit decorator works.
```
    python main.py
```