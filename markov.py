
import os
def process_file(filename):
	markov_dict = {}
	f = open(filename)
	line = f.readline()
	print line
	f.close()
	# if it's not empty
	# if os.path.getsize(fullpathhere) > 0:
	# 	print filename
	prefix = ()
	suffix = []
	split_line = line.split()
	if len(split_line) < 3:
		pass
		#print markov_dict
	else:
		#tuples just get entered manually, prefix below is a tuple. no need to "append", you can't append tuples
		#you can append lists
		prefix = (split_line[0],split_line[1])
		suffix.append(split_line[2])
		#print prefix
		#print suffix
		#to create a dictionary, give each key the right value
		markov_dict[prefix] = suffix
	#"return" stores the markov_dict value to the process_file function	
	return markov_dict

def main():
	#print is just printing the outcome that was stored of the function run on (filename)
	print process_file("sample2.txt")

if __name__ == "__main__":
	main()

