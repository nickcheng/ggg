# ggg

Personal Git/GitHub/Gist Helper

- [ggg](#ggg)
  - [How to Install](#how-to-install)
  - [How to Use](#how-to-use)
    - [Commands](#commands)
  - [How to Develop](#how-to-develop)
    - [Try run it](#try-run-it)
    - [For supporting in VS Code](#for-supporting-in-vs-code)
    - [Using jupyter with poetry](#using-jupyter-with-poetry)
    - [Packaging](#packaging)
      - [Convert TOML project file to setup.py](#convert-toml-project-file-to-setuppy)
      - [entry_points](#entry_points)


## How to Install

Python 3 required.

1. Clone the repo

2. `python setup.py install`

3. Configuration

Under your HOME directory (`~/`), create `.ggg` file.

```bash
touch ~/.ggg
```

I have a sample configuration file `sample.ggg`. Feel free to modify it and put it into correct place(`~/`) with correct file name(`.ggg`).

## How to Use
### Commands

- [x] `ggg c`: Enter interactive commit mode.
- [x] `ggg rb`: Checkout recent branches interactively.
- [ ] `ggg pr`: Send pull request easier.

## How to Develop

### Try run it

```bash
python -m ggg
```

### For supporting in VS Code

```bash
poetry shell
code .
```

### Using jupyter with poetry

Ref: https://blog.jayway.com/2019/12/28/pyenv-poetry-saviours-in-the-python-chaos/

jupyter works with kernels, and will not work out of the box with your virtual environment that poetry created for you. If you wish to work in a jupyter notebook based on your virtual environment, you need to create a kernel for that virtual environment. The code below explains how. The prerequisite is that you have added both jupyter and ipykernel as dependencies in your poetry project.

```shell
# Make sure to run the command within your virtual environment. The 'poetry run' command ensures this
# Best practice is to use the same name for your kernel as the project.
poetry run ipython kernel install --user --name=ggg
```

### Packaging

1. Convert toml file to `setup.py`
2. Add `entry_points` into `setup.py`
3. run `python setup.py install`

#### Convert TOML project file to setup.py

```bash
dephell deps convert --from=pyproject.toml --to=setup.py
```

Ref: https://dephell.org

#### entry_points

```python
entry_points={
    'console_scripts': ['ggg=ggg.app:cli'],
},
```
