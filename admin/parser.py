from pyparsing import Word, alphas, nums, oneOf, infixNotation, opAssoc, ParseResults, Combine, quotedString


# Define the basic elements of grammar
allowed_identifiers = oneOf("Price delivery_time weight")

# Define number (for numeric values)
number = Word(nums)

# Define date using (YYYY-MM-DD format)
date = Combine(Word(nums, exact=4) + "-" + Word(nums, exact = 2)) + "-" + Word(nums, exact=2)

# Define string (enclosed in quotes)
string = quotedString.setParseAction(lambda t: t[0][1:-1])

# Define comparison operators
comparison_op = oneOf("< > =")

# Logical operators
logical_op = oneOf("AND OR")

# Define a general "value" which can be a number, date, or string
value = number | date | string

# Define the expression grammar
expr = infixNotation(
    allowed_identifiers + comparison_op + value,
    [
        (logical_op, 2, opAssoc.LEFT),
    ]
)

# Expand evaluation logic later