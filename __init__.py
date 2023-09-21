import subprocess
import os
from ini_reader import ini_reader
from random_number_generator import random_number_generator as random

def run_random_emulator():
    # Random
    emulators = list(games["emulators"].keys())
    random_emulator_number = random.getRandomGameNumber(
        len(
            emulators
        )-1
    )
    selected_emulator_dictionary = games["emulators"][emulators[random_emulator_number]]

    rom_list = os.listdir(selected_emulator_dictionary["roms"].replace("\"", ""))
    random_rom_number = random.getRandomGameNumber(
        len(
            rom_list
        )-1
    )
    rom_for_cmd = selected_emulator_dictionary["roms"].replace("\"", "") + "/" + rom_list[random_rom_number]

    cmd = f'{steam_path} -applaunch 1118310 -L {selected_emulator_dictionary["core"]} "{rom_for_cmd}"'
    print(cmd)
    resultado = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
def run_random_standalone():
    # Random
    standalone_dictionary = games["standalones"]
    print(standalone_dictionary)

    standalone_list = list(games["standalones"].keys())
    random_game_number = random.getRandomGameNumber(
        len(
            standalone_list
        )-1
    )
    standalone_key = standalone_list[random_game_number]
    standalone_path = games["standalones"][standalone_key].replace("\"", "")
    cmd = f'"{standalone_path}"'
    print(cmd)
    resultado = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


print("""

████████╗██╗  ██╗███████╗    ██╗  ██╗██╗███╗   ██╗ ██████╗                 
╚══██╔══╝██║  ██║██╔════╝    ██║ ██╔╝██║████╗  ██║██╔════╝                 
   ██║   ███████║█████╗      █████╔╝ ██║██╔██╗ ██║██║  ███╗                
   ██║   ██╔══██║██╔══╝      ██╔═██╗ ██║██║╚██╗██║██║   ██║                
   ██║   ██║  ██║███████╗    ██║  ██╗██║██║ ╚████║╚██████╔╝                
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝                 
                                                                           
 ██████╗ ███████╗    ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ███╗   ███╗
██╔═══██╗██╔════╝    ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗████╗ ████║
██║   ██║█████╗      ██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██╔████╔██║
██║   ██║██╔══╝      ██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║██║╚██╔╝██║
╚██████╔╝██║         ██║  ██║██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║ ╚═╝ ██║
 ╚═════╝ ╚═╝         ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝
                                                                           
███████╗██╗ ██████╗ ██╗  ██╗████████╗███████╗██████╗ ███████╗              
██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝              
█████╗  ██║██║  ███╗███████║   ██║   █████╗  ██████╔╝███████╗              
██╔══╝  ██║██║   ██║██╔══██║   ██║   ██╔══╝  ██╔══██╗╚════██║              
██║     ██║╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║███████║              
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝              
                                                                           
""")

### Paths
reader = ini_reader()

games = reader.execute()
if games != None:
    steam_path = games["Steam"]
    
    if "emulators" and "standalones" in games:
        if random.getOneOrTwo() == 3:
            print('a1')
            run_random_emulator()
        else:
            print('a2')
            run_random_standalone()

    elif "emulators" in games:
        print('b')
        run_random_emulator()

    elif "standalones" in games:
        print('c')
        run_random_standalone()

    else:
        print('d')
        pass
