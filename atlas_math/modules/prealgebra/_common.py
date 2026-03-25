from __future__ import annotations

import random
from fractions import Fraction

DIFFICULTY_TO_LEVEL = {
    "level_1": 1,
    "level_2": 2,
    "level_3": 3,
    "level_4": 4,
    "level_5": 5,
}
DIFFICULTY_MAP = dict(DIFFICULTY_TO_LEVEL)

NAMES = [
    "Ava", "Noah", "Liam", "Emma", "Olivia", "Mason", "Sophia", "Lucas",
    "Mia", "Ethan", "Isabella", "Amelia", "James", "Charlotte", "Benjamin", "Harper",
]
ITEMS = [
    ("book", "books"), ("notebook", "notebooks"), ("apple", "apples"), ("pencil", "pencils"),
    ("ticket", "tickets"), ("sticker", "stickers"), ("balloon", "balloons"), ("plant", "plants"),
]
CONTAINERS = ["box", "bag", "crate", "basket", "jar", "folder"]

SOLVE_TEMPLATES = [
    "Solve:", "Solve for x:", "Find x:", "Determine the value of x:", "Work out the solution:",
    "Find the solution:", "Compute x:", "Solve the equation:", "Determine x:", "Find the unknown:",
    "Set up and solve:", "Calculate the value of x:",
]
SIMPLIFY_TEMPLATES = [
    "Simplify:", "Reduce the expression:", "Combine like terms:", "Rewrite in simplest form:",
    "Simplify the expression:", "Work out the simplified form:", "Find the simplified result:",
    "Expand and simplify:", "Determine the simplified expression:", "Compute the simplified form:",
]
EVALUATE_TEMPLATES = [
    "Evaluate:", "Compute:", "Find the value of:", "Calculate:", "Work out:", "Determine the result:",
    "Evaluate the expression:", "Compute the expression:", "Find the result of:", "Solve:",
]
SLOPE_TEMPLATES = [
    "Find the slope:", "Compute the slope:", "Determine the slope:", "What is the slope?",
    "Calculate the slope of the line:", "Find the rate of change:", "Solve for the slope:",
]
LINE_TEMPLATES = [
    "Find the equation of the line:", "Determine the line in slope-intercept form:",
    "Write the line equation:", "Find y = mx + b:", "Identify the equation of the line:",
]
SYSTEM_TEMPLATES = [
    "Solve the system:", "Find the solution to the system:", "Determine the ordered pair:",
    "Solve for x and y:", "Compute the solution to the system:", "Find the intersection point:",
]

def difficulty_level(difficulty: str) -> int:
    return DIFFICULTY_TO_LEVEL.get(difficulty, 1)

def choose_instruction(rng: random.Random, *args: object) -> str:
    if len(args) == 1:
        return str(args[0])
    if len(args) == 2:
        instructions, problem = args
        choices = list(instructions) if isinstance(instructions, (list, tuple)) else []
        if not choices:
            return str(problem)
        opener = rng.choice(choices)
        return f"{opener} {problem}" if opener else str(problem)
    raise TypeError("choose_instruction() expects (rng, problem) or (rng, instructions, problem)")

def choose_template(rng: random.Random, templates: list[str] | tuple[str, ...], problem: str | None = None) -> str:
    template = rng.choice(list(templates))
    return f"{template} {problem}" if problem else template

def signed_int(rng: random.Random, low: int, high: int, exclude_zero: bool = False) -> int:
    value = 0
    while True:
        value = rng.randint(low, high)
        if not (exclude_zero and value == 0):
            return value

def int_words(n: int) -> str:
    small = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
        12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    }
    tens = {20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
    if n < 0:
        return "minus " + int_words(-n)
    if n < 20:
        return small[n]
    if n < 100:
        return tens[n] if n in tens else f"{tens[n // 10 * 10]}-{small[n % 10]}"
    if n < 1000:
        return f"{small[n // 100]} hundred" if n % 100 == 0 else f"{small[n // 100]} hundred {int_words(n % 100)}"
    return str(n)

number_to_words = int_words

def number_words(value: int | Fraction) -> str:
    if isinstance(value, Fraction):
        return fraction_to_words(value)
    return int_words(value)

def fraction_to_str(value: Fraction) -> str:
    value = Fraction(value.numerator, value.denominator)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"

to_fraction_str = fraction_to_str

def fraction_to_words(value: Fraction) -> str:
    value = Fraction(value.numerator, value.denominator)
    if value.denominator == 1:
        return int_words(value.numerator)
    denom_names = {2:"halves",3:"thirds",4:"fourths",5:"fifths",6:"sixths",7:"sevenths",8:"eighths",9:"ninths",10:"tenths",12:"twelfths"}
    denom = denom_names.get(value.denominator, f"{int_words(value.denominator)}ths")
    prefix = "minus " if value.numerator < 0 else ""
    n = abs(value.numerator)
    if n == 1:
        singular = denom[:-1] if denom.endswith("s") else denom
        return f"{prefix}one {singular}"
    return f"{prefix}{int_words(n)} {denom}"

fraction_words = fraction_to_words

def money_str(cents: int) -> str:
    dollars, rem = divmod(cents, 100)
    return f"${dollars}.{rem:02d}"

def money_words(cents: int) -> str:
    dollars, rem = divmod(cents, 100)
    if rem == 0:
        unit = "dollar" if dollars == 1 else "dollars"
        return f"{int_words(dollars)} {unit}"
    return f"{int_words(dollars)} dollars and {int_words(rem)} cents"

def format_coeff(value: int | Fraction, variable: str = "x", power: int = 1) -> str:
    if isinstance(value, Fraction):
        coeff = fraction_to_str(value)
        zero = value == 0
        is_one = value == 1
        is_neg_one = value == -1
    else:
        coeff = str(value)
        zero = value == 0
        is_one = value == 1
        is_neg_one = value == -1
    if zero:
        return "0" if power == 0 else f"0{variable}"
    if power == 0:
        return coeff
    base = variable if power == 1 else f"{variable}^{power}"
    if is_one:
        return base
    if is_neg_one:
        return f"-{base}"
    return f"{coeff}{base}"

def join_terms(parts: list[str]) -> str:
    cleaned = [p.strip() for p in parts if p and p.strip() and p.strip() != "0x"]
    if not cleaned:
        return "0"
    out = cleaned[0]
    for term in cleaned[1:]:
        if term.startswith("-"):
            out += f" - {term[1:]}"
        else:
            out += f" + {term}"
    return out

def expression_words(text: str) -> str:
    out = str(text)
    replacements = [
        ("<=", " less than or equal to "),
        (">=", " greater than or equal to "),
        ("!=", " not equal to "),
        ("^", " to the power of "),
        ("+", " plus "),
        ("-", " minus "),
        ("=", " equals "),
        ("(", " open parenthesis "),
        (")", " close parenthesis "),
        ("/", " over "),
        (",", " comma "),
    ]
    for a, b in replacements:
        out = out.replace(a, b)
    return " ".join(out.split()).lower()

def answer_line(answer: str) -> str:
    return answer

def answer_words_line(answer_words: str) -> str:
    return answer_words
