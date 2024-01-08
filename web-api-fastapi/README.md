# RECOMMENDATION ENGINE
This repository supports calls to decomposition and recommendation feature in distribution feature of DCE.

## Python
In order to run the pipelines,` python 3.10` is required. All the python libraries essential to this repo are included in `requirements.txt`.

It is recommended to use an environment manager such as [conda](https://docs.conda.io/en/latest) in order to control the python environment and use a minimal setup.

## Local Dev Environment
In order to set up local dev environment run `pip3 install -r requirements.dev.txt`

Further, specific environment variables would be setup in config `.<env>` file. A draft version of the file is available in the same location for reference

## Pre-commit
We have set up pre-commit configuration to ensure that code is formatted properly and passes flake8 (lint), mypy and other standard checks. To learn more refer [Pre-commit Introduction](https://pre-commit.com/#intro).

## Running Tests, Coverage Report and Code Quality
Following libraries would be required to run tests, coverage, quality checks. They can be included in `requirements.dev.txt`

* pytest
* coverage
* code-quality
* flake8
* black

Integration tests must be included for every function/module while submitting merge requests.

* To run tests you can call pytest from script directory `python3 -m pytest`
* To run tests coverage report run `coverage run -m pytest` and then to view the report run `coverage report -m`. Final coverage percentage must be included in the merge request
* We use `black` for code linting. Black could be setup on choice of IDE following [Editor integration](https://black.readthedocs.io/en/stable/integrations/editors.html)
* Code quality report numbers must also be submitted with every merge request. We use light weight `code-quality` library for this. Report can be generated using `python -m code_quality -d src/`

Setting files for `pre-commit`, `coverage`, `linting` are included in the base location of the repo and should not be changed.

## Docker

We use [docker](https://docs.docker.com/get-docker/) for deploying the repository. Docker keeps the code isolated and scalable.

Install docker locally in order to be able to build and run the Dockerfile and container.

Once docker is installed, build image by running `docker build -t <repository-name> . --build-arg BRANCH=<env>`. This would build a docker image on the local machine.

To run the image after building run `docker run -it <repository-name>`.

Contribution to the Project
Contribution must be done via merge requests on `dev` branch. Every merge request must be approved by repository owner.

Commit messages must follow the [conventional_commit_message_format](https://www.conventionalcommits.org/en/v1.0.0/)
