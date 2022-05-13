# XCompile

Simply create compose key instructions for Linux and Mac.

The compose sequences are specified by a Unicode characters, a tab and then the key sequence (using → ← ↑ ↓ for the arrow keys).

```
❤  <3
⇆   ←→
```

Now you can enter cool unicode characters such as ❤ and ⇆ and with the keystrokes `CapsLock` `<` `3` and `CapsLock` `left` `right`!

## How to use

### Linux

```sh
cat Diacritics Math Other | ./XCompile.py > ~/.XCompose && setxkbmap
```

Specify the `CapsLock` key as your compose key.

### Mac OS

```sh
cat Math Diacritics Other | ./KeyBindings.py > ~/Library/KeyBindings/DefaultKeyBinding.Dict
```

Mac doesn't have a concenpt of a compose key, so instead `Ctrl-Opt-Cmd-F8` is used. You can use [Karabiner Elements](https://karabiner-elements.pqrs.org/) to remap `CapsLock` to `Ctrl-Opt-Cmd-F8`. After installation, copy the rule file:

```sh
cp ./karabiner-compose.json ~/.config/karabiner/assets/complex_modifications/
```

And enable the new rule in Karabiner preferences (Complex Modifications -> Rules -> Add Rule).

[Karabiner JSON doc](https://karabiner-elements.pqrs.org/docs/json/)

