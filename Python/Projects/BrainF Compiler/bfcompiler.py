"""
This contains a compiler for the language brainf into python.
To use, put the raw brainf file inside this folder (so that the import works)

Then run the_compiler(path/to/raw/brainf)
An output file a.out.py should be seen.
(Make sure there are no other a.out.py files)
To run the code, run $python a.out.py

Presently, an example of brainf addition is in a.out.py
"""

def lexer(bf_file):
    ret = []
    afile = open(bf_file, "r")
    content = afile.read().replace(" ","").replace("\n", "").replace("\t", "")
    #for now assuming no letters and just bf symbols and whitespace
    afile.close()
    index = 1
    previous_char = content[0]
    char_count = 0
    for char in content:
        if char == "[" or char == "]":
			ret.append((char, 1))
			continue
        if index == len(content):
            if previous_char == char:
				char_count += 1
				ret.append((previous_char, char_count))
            else:	
				ret.append((previous_char, char_count))
				ret.append((char, 1))
        else:
	        if previous_char == char:       
	             char_count += 1 
	        else:
	            ret.append((previous_char, char_count))
	            previous_char = char
	            char_count = 1
        index += 1
    return ret

def compiler(lexed, prefix = "", First_time = False):
	#lexed is a list of tuples ("char", int) like 
	#("+", 3)
	out = open("a.out.py", "a+")
	if First_time:
		out.write("from inflist import *\n")
		out.write("a = InfiniteList()\n")
	index = 0
	for token in lexed:
		typ = token[0]
		amt = str(token[1])
		if typ == ">":
			out.write(prefix +"a.move_right(" + amt + ")\n")
		elif typ == "<":
			out.write(prefix +"a.move_left(" + amt + ")\n")
		elif typ == "+":
			out.write(prefix +"a.increment(" + amt + ")\n")
		elif typ == "-":
			out.write(prefix +"a.decrement(" + amt + ")\n")
		elif typ == ".":
			out.write(prefix +"print(a.get())\n")
		elif typ == ",":
			out.write(prefix +"inp = input() #must be an integer\na.assign(int(inp))\n")
		elif typ == "[":
			out.write(prefix + "while a.get() != 0:\n")
			prefix += "\t"
		elif typ == "]":
			prefix = prefix[:-1]
		index += 1
	out.close()
	return None
	
def the_compiler(path):
	compiler(lexer(path), First_time = True)
	return None

