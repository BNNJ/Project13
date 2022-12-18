# Orange County Lettings

OpenClassrooms project 13
[Original doc (in french)](README_oc.md)

## Description

This project is an exercice in continuous integration and continuous deployment.
It uses CircleCi, Dockerhub and Heroku.

Here's a quick recap of the workflow:
- Updates to github's Main/Master branch should trigger the pipeline on CircleCi.
- The CircleCi's pipeline first makes a test build, runs tests and linting
- If both pass, a docker image is produced and pushed to Dockerhub
- The image is then pulled from dockerhub and pushed to Heroku to make the app publicly accessible

## Requirements

* git CLI
* pip
* python 3.6+

## Setup

Clone the project:
```sh
git clone https://github.com/BNNJ/Project13.git {path/to/project}
```
Go to the project directory:
```sh
cd {path/to/project}
``` 
Create a virtual environment:
```sh
python -m venv venv
```
Activate the environment (unix):
```sh
source venv/bin/activate
```
Windows PowerShell:
```sh
.\venv\Scripts\Activate.ps1
```
Install the dependencies:
```sh
pip install -r requirements.txt
```

## Usage

tests:
```sh
python manage.py test
```
linting:
```sh
flake8
```
Start the server:
```sh
python manage.py runserver
```
You can now access the app from `localhost:8000` from your browser
