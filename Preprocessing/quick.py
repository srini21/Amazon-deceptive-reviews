import sys

f = open(sys.argv[1], "r")
g = open(sys.argv[2], "w")

sentences = [line.strip() for line in f]
sentences = sentences[0:4000]

for sent in sentences:
	g.write(sent+"\n")


