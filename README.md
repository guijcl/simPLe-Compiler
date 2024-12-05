# simPLe Compiler

This project was developed for the Compiler Techniques course at FCUL (Faculty of Sciences - University of Lisbon), lectured by [Alcides Fonseca](https://github.com/alcides).

## Student Information

- **Name:** Guilherme Lopes
- **Student Number:** fc52761

## Setup

Before running the compiler, install all dependencies:

```bash
./setup.sh
```

## Usage

The compiler can be run in three different ways:

1. Run with a specific test file:

```bash
python simple.py <file>
```

Replace `<file>` with any file from the `tests` folder.

2. Run all working tests:

```bash
python simple.py ok_tests
```

This executes all tests that demonstrate working features without errors.

3. Run all error test cases:

```bash
python simple.py failed_tests
```

This executes tests containing intentionally incorrect simPLe programs to verify error detection.

Alternatively, you can use the provided script to run the most complex example:

```bash
./run.sh
```

## Environment

Compiler developed and tested in Ubuntu
