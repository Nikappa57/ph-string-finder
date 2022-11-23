import os
import time

def check_files(legit_files, unlegit_files, cheat_files):
    directory = [f for f in os.listdir()]
    
    if "Legit" not in directory:
        os.makedirs("Legit")
    
    if "Unlegit" not in directory:
        os.makedirs("Unlegit")

    if "CheatProcess" not in directory:
        os.makedirs("CheatProcess")

    if len(legit_files) < 1:
        print("No Legit Files Found.")

        time.sleep(5)

        exit()

    elif len(unlegit_files) < 1:
        print("No Unlegit files found.")

        time.sleep(5)

        exit()
    
    elif len(cheat_files) > 1:
        print("You can only use one CheatProcess log.")

        time.sleep(5)

        exit()