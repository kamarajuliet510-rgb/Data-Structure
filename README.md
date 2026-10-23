# DCOMP320 – Data Structures and Algorithms

## How to run the program

- Python version: Python 3.10 or later
- Command to execute:

```bash
python stack_evaluator.py
```

The program reads `input.txt`, evaluates each expression using a stack-based expression evaluator, and writes the results to `output.txt` in the same separator format used by the input file.

## Structure of `input.txt` and `output.txt`

### `input.txt`

- Each expression appears on its own line.
- Expressions are separated by a line containing only dashes: `-----`.
- Blank lines are ignored.
- A trailing separator is tolerated without crashing.

Example:

```text
3 + 5 * 2
-----
(8 / 4) + 7 * 2
-----
10 - (2 + 3) * 4
```

### `output.txt`

- Each line shows the original expression and its result in the form: `expression = result`.
- The same separator line is used between results.
- Invalid expressions produce a clear error message in the same format, for example: `5 / 0 = Error: division by zero`.

Example:

```text
3 + 5 * 2 = 13
-----
(8 / 4) + 7 * 2 = 16
-----
10 - (2 + 3) * 4 = -10
```

## Assumptions and limitations

- Supported operators: `+`, `-`, `*`, `/`, and parentheses.
- Operator precedence follows normal arithmetic rules: multiplication and division are evaluated before addition and subtraction.
- Operators with the same precedence are evaluated left-to-right.
- The implementation uses the shunting-yard algorithm to convert infix expressions to postfix notation, then evaluates the postfix form with a stack.
- Integer and decimal numbers are accepted.
- Division follows standard Python division semantics. Whole-number results are printed without a trailing `.0`.
- Unary minus is not implemented; expressions such as `-5` are treated as invalid unless your input format is adjusted.
- Invalid input, mismatched parentheses, malformed tokens, and division by zero are reported as error messages rather than crashing the program.

## Report outline for the printed assignment

### Title page
- Title: Stack-Based Expression Evaluation Using a Stack Data Structure
- Student Name: [Student Name]
- Course Name: DCOMP320 – Data Structures and Algorithms
- Submission Date: [DD/MM/YYYY]

### Introduction
- Explain the purpose of the assignment.
- Describe the role of expression evaluation in computing.
- Mention why stack-based methods are important in building interpreters, calculators, and compilers.

### Data Structures Used
- Describe the stack data structure and its key operations: push, pop, and peek.
- Explain how the program stores operators and values during evaluation.
- Discuss why stack-based processing is efficient for expression parsing and evaluation.
- Emphasize the importance of stacks in computing, especially for managing nested structures such as parentheses and operator precedence.

### Program Design
- Provide a high-level overview of the architecture of the solution.
- Describe the main parts of the program:
  - `Stack` class
  - tokenization of expressions
  - shunting-yard conversion to postfix
  - postfix evaluation using a stack
  - reading and writing files
- Include pseudocode or a simple flowchart showing the evaluation process.

### Testing and Results
- Explain how the program was tested using valid and invalid expressions.
- Describe the sample cases in `input.txt` and the resulting `output.txt`.
- Discuss how the program handles errors such as division by zero and mismatched parentheses.
- Explain how blank lines and a trailing separator were handled.

### Conclusion
- Summarize the success of the stack-based solution.
- Mention that the code was uploaded to GitHub and the lecturer was added as a collaborator.
- State how the assignment demonstrates the practical use of stacks in problem solving.

### References
- Sedgewick, R., & Wayne, K. (2011). Algorithms. Addison-Wesley.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms. MIT Press.
- Python Software Foundation. Python documentation: `https://docs.python.org/3/`

### Formatting requirements for the report

- Font: Tahoma
- Size: 10
- Line spacing: 1.15
- Alignment: Justified

### Grading criteria targeted

- Stack operations (15)
- Input handling (30)
- Output (30)
- Testing and results (15)
- Documentation and GitHub (10)

---

This project demonstrates a complete stack-based expression evaluator implemented in Python and saved as a ready-to-use assignment solution.
