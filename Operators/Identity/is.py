# is symbol : is

# it used when both indentifer object same into result return true

# example human eyes

female_body = ["eyes","ears","legs"]
male_body = ["eyes","ears","legs"]

animal = male_body
bird = female_body

# it's return true becuase female_body object are same of bird object 
print(bird is female_body)

# it's return false becuse female and male are diffrent body
print(female_body is male_body)

