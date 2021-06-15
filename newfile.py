string_var="abcde"
print(string_var)
print("after replacing G in string", string_var.replace("c","G"))


print(string_var)
print("after replacing G in string", string_var[:2]+'G'+string_var[3:])

import re
print(string_var)
string_var=re.sub("c","G",string_var)
print("after replacing G in string",string_var )