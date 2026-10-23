from __future__ import annotations

from pathlib import Path


class Stack:
    """A basic stack implementation for expression evaluation."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack."""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._items[-1]

    def is_empty(self):
        """Check whether the stack contains any items."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)


def is_number(token: str) -> bool:
    """Return True if the token can be interpreted as a number."""
    try:
        float(token)
        return True
    except ValueError:
        return False


def precedence(operator: str) -> int:
    """Return the precedence value for a supported operator."""
    if operator in ("+", "-"):
        return 1
    if operator in ("*", "/"):
        return 2
    return 0


def tokenise(expression: str):
    """Split the expression into tokens while ignoring whitespace."""
    tokens = []
    index = 0

    while index < len(expression):
        character = expression[index]

        if character.isspace():
            index += 1
            continue

        if character.isdigit() or character == ".":
            start = index
            dot_seen = character == "."
            index += 1

            while index < len(expression):
                current = expression[index]
                if current.isdigit():
                    index += 1
                    continue
                if current == ".":
                    if dot_seen:
                        raise ValueError(f"Malformed number: {expression[start:index + 1]}")
                    dot_seen = True
                    index += 1
                    continue
                break

            number = expression[start:index]
            if number == ".":
                raise ValueError(f"Malformed number: {number}")
            tokens.append(number)
            continue

        if character in "+-*/()":
            tokens.append(character)
            index += 1
            continue

        raise ValueError(f"Unsupported character: '{character}'")

    return tokens


def infix_to_postfix(tokens):
    """Convert infix tokens to postfix using the shunting-yard algorithm."""
    output = []
    operators = Stack()

    for token in tokens:
        if is_number(token):
            output.append(token)
        elif token == "(":
            operators.push(token)
        elif token == ")":
            while not operators.is_empty() and operators.peek() != "(":
                output.append(operators.pop())
            if operators.is_empty():
                raise ValueError("Mismatched parentheses")
            operators.pop()  # remove the opening parenthesis
        elif token in "+-*/":
            while (
                not operators.is_empty()
                and operators.peek() != "("
                and precedence(operators.peek()) >= precedence(token)
            ):
                output.append(operators.pop())
            operators.push(token)
        else:
            raise ValueError(f"Invalid token: {token}")

    while not operators.is_empty():
        operator = operators.pop()
        if operator == "(":
            raise ValueError("Mismatched parentheses")
        output.append(operator)

    return output


def evaluate_postfix(postfix_tokens):
    """Evaluate a postfix expression using a stack."""
    stack = Stack()

    for token in postfix_tokens:
        if is_number(token):
            stack.push(float(token))
        else:
            if stack.size() < 2:
                raise ValueError("Malformed expression")

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                result = left / right
            else:
                raise ValueError(f"Unsupported operator: {token}")

            stack.push(result)

    if stack.size() != 1:
        raise ValueError("Malformed expression")

    return stack.pop()


def format_number(value):
    """Format a numeric result cleanly for output."""
    if isinstance(value, float):
        if abs(value - round(value)) < 1e-10:
            return str(int(round(value)))
        return format(value, ".10g")
    return str(value)


def evaluate_expression(expression: str) -> str:
    """Parse and evaluate one expression, returning a readable string result."""
    trimmed = expression.strip()
    if not trimmed:
        return "Error: empty expression"

    try:
        tokens = tokenise(trimmed)
        if not tokens:
            return "Error: empty expression"
        postfix = infix_to_postfix(tokens)
        result = evaluate_postfix(postfix)
        return format_number(result)
    except ZeroDivisionError:
        return "Error: division by zero"
    except ValueError as exc:
        message = str(exc)
        if message.startswith("Mismatched"):
            return "Error: mismatched parentheses"
        if message.startswith("Malformed") or message.startswith("Unsupported"):
            return "Error: malformed expression"
        return f"Error: {message}"


def build_output_line(expression: str) -> str:
    """Return a readable line with the original expression and its computed result."""
    result = evaluate_expression(expression)
    return f"{expression.strip()} = {result}"


def read_expressions(input_path: Path):
    """Read the input file and split it into expressions, ignoring separators and blanks."""
    expressions = []
    current_expression = []

    with input_path.open("r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()

            if line == "-----":
                if current_expression:
                    expressions.append(" ".join(current_expression))
                    current_expression = []
                continue

            if not line:
                continue

            current_expression.append(line)

    if current_expression:
        expressions.append(" ".join(current_expression))

    return expressions


def process_input_file(input_path: Path, output_path: Path):
    """Read the input file, evaluate each expression, and write the results to the output file."""
    expressions = read_expressions(input_path)
    lines = []

    for expression in expressions:
        lines.append(build_output_line(expression))

    if not lines:
        output_path.write_text("", encoding="utf-8")
        return

    output_content = "\n-----\n".join(lines)
    output_path.write_text(output_content + "\n", encoding="utf-8")


def main():
    """Entry point for the stack-based expression evaluator."""
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / "input.txt"
    output_path = base_dir / "output.txt"

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    expressions = read_expressions(input_path)
    for expression in expressions:
        print(build_output_line(expression))

    process_input_file(input_path, output_path)
    print(f"\nProcessed expressions and saved results to {output_path}")


if __name__ == "__main__":
    main()
