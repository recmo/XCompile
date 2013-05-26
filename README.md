XCompile
========

Specify XCompose sequences in a simple language and compile them to .XCompose files

The compose sequences are specified by a Unicode characters, a tab and then the key sequence (using → ← ↑ ↓ for the arrow keys).

    ǿ	`/o
    ≠	/=

Gets translated to

    <Multi_key> <apostrophe> <slash> <o> : "ǿ"
    <Multi_key> <slash> <equal> : "≠"

Store this in your `~/.XCompose` file, specify the `CapsLock` key as your compose key. Now you can enter cool unicode characters such as ❤ and ⇆ and with the keystrokes `CapsLock` `<` `3` and `CapsLock` `left` `right`!

How to use
----------

The program `XCompile` translates between 

    cat Diacritics Math Other | ./XCompile > ~/.XCompose && setxkbmap





