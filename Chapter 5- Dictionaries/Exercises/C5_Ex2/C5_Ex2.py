# This piece of code defines a dictionary called 'glossary' that contains programming terms and their meanings, specifically related to variables, lists, and if statements.

glossary = {
    "Variable": "A container that holds data, which can be changed during the execution of a program.",
    "Data Type": "A classification that specifies which type of value a variable can hold, such as int, float, or str.",
    "List": "A data structure that stores a collection of elements in an ordered sequence.",
    "Dictionary": "A data structure that stores key-value pairs, allowing efficient retrieval of values based on keys.",
    "Control Flow": "The order in which statements and instructions are executed in a program, typically controlled by conditional statements and loops.",
}

for word, meaning in glossary.items(): # Print each word and its meaning with a blank line between them
    print(word + ": " + meaning + "\n")