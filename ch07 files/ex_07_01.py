txt = input('Text file: ')
def python_shout(txt):
    file = open(txt)
    inp = file.read()
    print(inp.upper())

python_shout(txt)