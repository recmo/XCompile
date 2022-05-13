#!/usr/bin/python3
import sys

# Assume Compose (i.e. caps lock) is remapped to Ctrl-Opt-Cmd-F8:
# ~ ⌥ Option key
# $ ⇧ Shift key
# ^ ^ Control key
# @ ⌘ Command key
# #   keys on number pad
compose = "^~@\\UF70B"

# https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/TextDefaultsBindings/TextDefaultsBindings.html
# https://developer.apple.com/documentation/appkit/nsstandardkeybindingresponding
# http://xahlee.info/kbd/osx_keybinding_key_syntax.html
# https://github.com/phracker/MacOSX-SDKs/blob/041600eda65c6a668f66cb7d56b7d1da3e8bcc93/MacOSX10.6.sdk/System/Library/Frameworks/AppKit.framework/Versions/C/Headers/NSEvent.h#L395
substitutes = {
	u"↑": "\\UF700",
	u"↓": "\\UF701",
	u"←": "\\UF702",
	u"→": "\\UF703",
    "\\": "\\\\",
    "\"": "\\\"",
    "~": "\\\\~",
    "$": "\\\\$",
    "^": "\\\\^",
    "@": "\\\\@",
    "#": "\\\\#",
}

sequences = {}

for line in sys.stdin.readlines():
    line = line.strip('\n')
    if line.startswith("#") or line == "":
        continue
    (target, sequence) = line.split("\t")
    prev = None
    branch = sequences
    for char in sequence:
        if char in substitutes:
            char = substitutes[char]
        if not char in branch:
            branch[char] = {}
        prev = branch
        branch = branch[char]
    prev[char] = target

sequences = {
    compose: sequences
}

def print_sequence(sequence, indent=4):
    print("{")
    for key in sequence:
        if isinstance(sequence[key], dict):
            print(" " * indent, end="")
            print("\"" + key + "\" = ", end="")
            print_sequence(sequence[key], indent + 4)
            print(";")
        else:
            print(" " * indent, end="")
            # We could add `yank:` or `setMark:, swapWithMark:, deleteToMark:`
            # to delete the selection before inserting the text, but that
            # breaks VSCode. I have not found a way that doesn't break.
            print(
                f'"{key}" = (insertText:, "{sequence[key]}");')
    print(" " * (indent - 4), end="")
    print("}", end="")

print_sequence(sequences)
print()
