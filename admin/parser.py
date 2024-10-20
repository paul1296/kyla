from pyparsing import Word, alphas, nums, oneOf, infixNotation, opAssoc, Combine, quotedString, Suppress, ZeroOrMore, Group

# Define the basic elements of grammar
allowed_identifiers = oneOf("Price delivery_time weight")

# Define number (for numeric values)
number = Word(nums)

# Define date using (YYYY-MM-DD format)
date = Combine(Word(nums, exact=4) + "-" + Word(nums, exact=2) + "-" + Word(nums, exact=2))

# Define string (enclosed in quotes)
string = quotedString.setParseAction(lambda t: t[0][1:-1])

# Define comparison operators
comparison_op = oneOf("< > =")

# Logical operators
logical_op = oneOf("AND OR")

# Define a general "value" which can be a number, date, or string
value = number | date | string

# Define comment rule
comment = Suppress("---") + ZeroOrMore(Word(alphas + nums + " "))

# Define the expression grammar, ignoring comments
expr = ZeroOrMore(comment) + Group(infixNotation(
    allowed_identifiers + comparison_op + value,
    [
        (logical_op, 2, opAssoc.LEFT),
    ]
))

# Example input string with comments
input_string = """
Price < 100 --- This is a comment
delivery_time = 5 --- Ignore this too
--- Another comment
weight > 10
"""

# Parse the input string
parsed_results = expr.searchString(input_string)

# Output the parsed results
for result in parsed_results:
    print(result[0])  # Access the group of parsed expressions
