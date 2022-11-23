import os

from script.result import Legit, Unlegit, Result, CheatProcess
from script.check import check_files




def main(legth, use_cheatprocess):
    legit_files = [os.path.join("Legit", file) for file in os.listdir(os.path.join("Legit")) if ".txt" in file]
    unlegit_files = [os.path.join("Unlegit", file) for file in os.listdir(os.path.join("Unlegit")) if ".txt" in file]
    cheat_files = [os.path.join("CheatProcess", file) for file in os.listdir(os.path.join("CheatProcess")) if ".txt" in file] if use_cheatprocess else []

    check_files(legit_files, unlegit_files, cheat_files)
    
    unlegit_strings = Unlegit(unlegit_files, legth)
    strings = Legit(legit_files, unlegit_strings, legth)

    result = CheatProcess(cheat_files, strings, legth) if use_cheatprocess else strings
    result, number_strings = Result(result)



    with open("Result.txt", "w") as f:
        f.write("\n".join(str(i) for i in result))
    

    input(f"{number_strings} Stringhe Sospette.")


if __name__ == "__main__":
    print("""
    ███████╗████████╗██████╗ ██╗███╗   ██╗ ██████╗     ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
    ██╔════╝╚══██╔══╝██╔══██╗██║████╗  ██║██╔════╝     ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
    ███████╗   ██║   ██████╔╝██║██╔██╗ ██║██║  ███╗    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
    ╚════██║   ██║   ██╔══██╗██║██║╚██╗██║██║   ██║    ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
    ███████║   ██║   ██║  ██║██║██║ ╚████║╚██████╔╝    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                             
    
                                                                        by @Nikappa57
    """)

    length = int(input("Minimum length of strings: "))

    if len(os.listdir(os.path.join("CheatProcess"))) == 1:
        use_cheatprocess = input("Do you want to use the CheatProcess? [y, n] >>")
        use_cheatprocess = True if use_cheatprocess.lower() == "y" else False
    else:
        use_cheatprocess = False

    main(length, use_cheatprocess)