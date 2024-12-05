# simPLe Compiler

A compiler implementation for the simPLe programming language, developed for the Compiler Techniques course at FCUL (Faculty of Sciences - University of Lisbon), lectured by [Alcides Fonseca](https://github.com/alcides).

## Student Information

- **Name:** Guilherme Lopes
- **Student Number:** fc52761
- **Final Grade:** 16.5/20

## Project Overview

simPLe is a minimalistic programming language designed for new programmers, featuring C-like syntax with static typing and LLVM code generation. The current implementation has limited support for arrays.

## Setup & Usage

Install dependencies:

```bash
./setup.sh
```

Run compiler:

```bash
python simple.py <file>        # Compile single file
python simple.py ok_tests      # Run working tests
python simple.py failed_tests  # Run error tests
./run.sh                       # Run complex example
```

## Language Features

- Function declarations and definitions
- Control flow (if/else, while)
- Variables and assignments
- Binary operators with C-like precedence
- Arrays and index access (limited implementation)
- Comments using (\* ... \*)
- Integer, Float, Boolean, and String literals
- Static type checking and inference
- Error detection (syntax, semantics, types)

## Examples

```bash
max:Int (a:Int, b:Int) {
    if a > b {
        return a;
    }
    return b;
}

main:Int () {
    return max(5, 3);
}
```

## Implementation Details

- Lexical analysis using Lex
- Parsing with Yacc
- LLVM code generation

Developed and tested in Ubuntu.
