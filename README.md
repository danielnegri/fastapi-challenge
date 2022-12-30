<p align="center" style="text-align:center;">
  <a href="./docs/greystone_labs-code-challenge.pdf">
    <img alt="Greystone Labs Logo" src="https://www.greystone.com/wp-content/themes/greystone/assets/images/logo_grey.svg" width="500" />
  </a>
</p>

This challenge demonstrates a REST API for a Loan Amortization app using the Python miniframework [FastAPI](https://fastapi.tiangolo.com/).

It provides sereral key features:
* **Create a user**
 
* **Create a loan**

* **Fetch loan schedule**
 
* **Fetch loan summary for a specific month**

Quick Start
---

#### Requirements

* Python >= 3.8.1
* [Poetry](https://python-poetry.org/docs/)
* Database migrations
* Docker

```bash
# Clone repository
$ git clone https://github.com/danielnegri/greyco-challenge.git 

# Install dependencies
$ pip3 install poetry
$ poetry use env 3.8
$ poetry shell 
$ poetry install
```

**Database Migrations:**

```bash
$ export PYTHONPATH=$PWD

# Create database
$ alembic upgrade heads 

# Seed database, create superuser
$ python app/pre_start.py # Create admin user
```

#### Running the live server

See [Fast API: First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/) for instructions on setting up a local 
development environment.

```bash
$ uvicorn app.main:app --reload
```

#### Running the live server with Docker

```bash
$ docker build --rm --progress=plain -t greyco-challenge .
$ docker run -it --rm -p 8000:80 greyco-challenge
$ open http://localhost:8000/docs
```

## How-To

For a more complete example including how to create users, loans and schedules, see the 
[Tutorial - User Guide](docs/tutorial.md). 

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for details on submitting patches and the contribution workflow.

### License

This repository is under the AGPL 3.0 license. See the [LICENSE](LICENSE) file for details.