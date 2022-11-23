import re

reString = "(0x.+) (\([0-9]*\)): (.*)"

def read_files(file, legth):
    strings = set()

    with open(file, "r") as f:
        lines = f.read().splitlines()

    for line in lines:
        line = adapter_line(line)
        if len(line) >= legth:
            strings.add(line)
            
    return strings


def adapter_line(line):
    match = re.search(reString, line)

    if match:
        line = match.group(3)

    return str(line)


def adapter_legit_unlegit(legit, unlegit):
    return set(unlegit) - set(legit)


def adapter_unlegit(a, b):
    return set(a).intersection(b) if len(b) else a

