# GlassClassification

===================================================================================

Guessing type of glass based on given input from website

===================================================================================

## What is in inside?

- [Start](#Start)
- [Folder Structure](#Structure)
- [Status](#Status)
- [Features](#Features)
- [How to execute](#Execute)

===================================================================================

## Start

- [From this link download repo](https://github.com/ErenEroglu61/GlassClassification)

- Clone repo with 
  - git clone 'https://github.com/ErenEroglu61/GlassClassification.git'

===================================================================================

## Structure

<details>
<summary> Structure </summary>

```app/
├── api/
│   ├── __init__.py
│   ├── routes.py
│   └── schemas.py
├── ml/
│   ├── __init__.py
│   └── model.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── predict.html
│   └── results.html
├── __init__.py
├── config.py
└── main.py

config/
├── __init__.py
└── config.yaml

datasets/
├── models/
│   ├── classifier.pkl
│   ├── label_encoder.pkl
│   └── scaler.pkl
├── raw/
│   └── glass.csv
└── README.md

notebooks/
├── glass.csv
└── GlassClassification.ipynb

.gitignore
README.md
requirements.txt
run.py
```
</details>

===================================================================================

## Status

As long as no bug found not thinking about upgrading

===================================================================================


## Features

Check [Requirements](requirements.txt) for features versions

===================================================================================

## Execute

- Download code in [here](#Start)
- Select notebooks folders 
- Execute [GlassClassification.ipynb](notebooks/GlassClassification.ipynb)
- Check [Models](datasets/models)
  - if any problem occurs ask ANY AI TOOLS 
  - if no problem I am cool and chilling
- Now you can execute run.py by (from now on you can use terminal for execute file)
  - python [run.py](run.py)
- By default, http://127.0.0.1:8000 will open as long as you didn't give any parameters while executing
  - python [run.py](run.py) --port 8080 
  - python [run.py](run.py) --host 0.0.0.0
- For debug
  - python [run.py](run.py) --debug
- While upgrading use reload because any changes will be change website
  - python [run.py](run.py) --reload
- If you have done with website you can go terminal and press CTRL + C for keyboard interrupt

