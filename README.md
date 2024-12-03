# DigiPOD ExecutionEngine Addons

This repository contains additional components for the [CELIDA Execution Engine][EE] that are specific to
the [DigiPOD project][DigiPOD].


## Usage
Run execute_digipod.py.


[DigiPOD]: https://github.com/DigiPOD
[EE]: https://github.com/CODEX-CELIDA/execution-engine


# Testing

Follow these steps to set up and run tests for the project:

### 1. Clone Submodules

First, ensure that you have cloned the submodules to get the necessary test data:

```bash
git submodule update --init --recursive
```

### 2. Start PostgreSQL Container

Ensure a PostgreSQL container is running. You can do this manually

```bash
docker run \
  --name postgres-pytest-digipod \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5434:5432 \
  -d postgres
```

### 3. Install Development Requirements

Install the necessary packages for testing from requirements-dev.txt:

```bash
pip install -r requirements-dev.txt
```

### 4. Run Pytest

Finally, run pytest with the necessary parameters:

```bash
pytest \
  --postgresql-host=localhost \
  --postgresql-port=5434 \
  --postgresql-user=postgres \
  --postgresql-password=mysecretpassword \
  --color=yes
```

This will execute the tests with the specified PostgreSQL configuration and additional options for the test run.
