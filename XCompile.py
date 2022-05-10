#!/usr/bin/python2
# coding=utf-8
import sys

# To find out:
# xmodmap -pke

XComposeNames = {
	"~": "asciitilde",
	"=": "equal",
	"-": "minus",
	"_": "underscore",
	"+": "plus",
	">": "greater",
	"<": "less",
	"|": "bar",
	"/": "slash",
	"\\": "backslash",
	".": "period",
	"!": "exclam",
	":": "colon",
	"^": "asciicircum",
	"?": "question",
	"(": "parenleft",
	")": "parenright",
	"[": "bracketleft",
	"]": "bracketright",
	"`": "grave",
	"'": "apostrophe",
	"\"": "quotedbl",
	" ": "space",
	",": "comma",
	"@": "at",
	"#": "numbersign",
	"$": "dollar",
	"%": "percent",
	"*": "asterisk",
	u"←": "Left",
	u"↑": "Up",
	u"→": "Right",
	u"↓": "Down",
}

def XComposeSequence(s, target):
	seq = "<Multi_key> "
	for c in s:
		if c in XComposeNames:
			seq += "<" + XComposeNames[c] + "> "
		else:
			seq += "<" + c + "> "
	seq += ": \"" + target + "\""
	return seq

sequences = {}
while True:
	try: line = raw_input().decode("utf-8");
	except EOFError: break
	if line == "" or line[0] == "#":
		print line.encode("utf-8")
		continue
	target, sequence = line.split("\t", 2)
	for s in sequences.iterkeys():
		if s.startswith(sequence) or sequence.startswith(s):
			sys.stderr.write(("WARNING: sequence \"" + sequence + "\" for \"" + target + "\" clashes with previous sequence \"" + s + "\" for \"" + sequences[s]+"\"\n").encode("utf-8"))
	sequences[sequence] = target
	print XComposeSequence(sequence, target).encode("utf-8")
