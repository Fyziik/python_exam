#!python
import is_even as i
import shuffled
from checkdigit import isbn

print(i.is_even(2))
print(i.is_even(1))

random_list = shuffled.Shuffled(10)
print(list(random_list))

checkdigit_response = isbn.validate("1-56619-909-3")
print(checkdigit_response)

