import os.path

from script.adapter import adapter_unlegit, adapter_legit_unlegit, read_files


def Unlegit(files, legth):
    unlegit_strings = set()

    for file in files:
        print(file)
        strings = read_files(file, legth)
        unlegit_strings = adapter_unlegit(strings, unlegit_strings)

    return unlegit_strings


def Legit(files, unlegit_strings, legth):
    for file in files:
        print(file)
        strings = read_files(file, legth)
        unlegit_strings = adapter_legit_unlegit(strings, unlegit_strings)

    return unlegit_strings

    
def CheatProcess(file, result_strings, legth):
    print(file[0])
    strings = read_files(file[0], legth)

    return adapter_unlegit(result_strings, strings)


def Result(strings):
    result = set()
    number_strings = 0

    file_url = os.path.join("script", "Exception", "Exception.txt")
    with open(file_url, "r") as f:
        except_strings = f.read().splitlines()

    for string in strings:
        add = True

        for except_string in except_strings:
            if except_string in string:
                add = False

        if add:
            result.add(string)
            number_strings += 1

    
    return result, number_strings
