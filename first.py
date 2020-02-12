number = 5
number += 20

# No apparent difference in outcome between the two. I assume conversion is done automatically.
print(f"The number is {str(number)}")
print(f'The number is {number}')


# challenge 2
oranges = 3333
people = 4

# to_charity = oranges % people
# to_each = (oranges - to_charity) / people

# or

to_each = oranges//people
to_charity = oranges % people

print(to_charity)
print(to_each)


# challenge 3
sentence = "This is a string"
is_sentence = isinstance(sentence, str)
print(is_sentence)
