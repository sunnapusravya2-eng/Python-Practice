'''
collectings of characters
'''
a='operations'
b="python"
c='''java'''
print(type(a),type(b),type(c))

'''
lower
upper
ends with 
starts with
replace
Strip
Rstrip
Lstrip
find
index
remove prefix
remove suffix
split
'''
#examples UPPERCASE()
Sravya="job searching"
print(Sravya.upper())

#LOWER CASE()
python="PROGRAMMING"
print(python.lower())

#endsWith()
java="high level"
print(java.endswith("level"))

#startsWith()
java="high level"
print(java.startswith("high"))

#replace with()
genai="Artificial intelligence"
print(genai.replace("Artificial","human"))

#index
java="high level"
print(java.index("level"))

#find
genai="human intelligence"
print(genai.find("human"))

#count
sql="tables coloumns"
print(sql.count("s"))

#remove prefix
AI="chatgpt"
print(AI.removeprefix("chat"))

#remove suffix
input="output"
print(input.removesuffix("put"))

#split (it will change in list format)
genai="HUMAN INTELLIGENCE"
print(genai.split())

#strip
sql="   tables   coloumns"
print(len(sql))
database="   tables   coloumns"
print(database.lstrip())
print(len(database))



