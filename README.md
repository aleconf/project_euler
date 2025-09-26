# Description

Solutions for [Project Euler](https://projecteuler.net/).

The focus is to write a Python project according to all best practices:
* creating a correct repository structure;
* writing all the needed tests and using TDD;
* writing clean code, with docstring and signature for all functions;
* writing efficient code, fast and with small memory footprint;
* using a linter and a formatter.

# Prerequisites

  * [Python](https://www.python.org/)
  * [uv](https://github.com/astral-sh/uv)

On a Windows machine, a solution for running a Makefile is also needed.

# Installation

To install it, run

```
make setup
```

# Usage

To simply use the application, run
```
make run
```

### Tests, linter, and formatter

* To run all **tests**, run `make tests`
* To use a **linter**, run `make linter`
* To **format**, the code run `make format`
* To run a **static type checker**, run `make typecheck`
