# Python Programming

Learning and documenting my knowledge about Python programming language

## Installing Dependencies

    pip install -r requirements.txt

## Generating Dependencies Using `pipdeptree`

    pipdeptree -f --warn silence | grep -P '^[\w0-9\-=.]+' >> requirements.txt

## Topics

1. Language Basics and Data Model
2. Object Oriented Programming
3. Functional Programming
4. Concurrenct Programming
5. Design Patterns
6. Data Structures
7. Algorithms
8. Interview Questions

## Configure pylint into git hook

1. Install git-pylint-commit-hook using `pip install git-pylint-commit-hook`
2. TODO
