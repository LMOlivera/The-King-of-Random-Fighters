import subprocess
import os
from ini_reader import ini_reader
from random_number_generator import random_number_generator as random

def run_random_emulator():
    emulators = list(games["emulators"].keys())
    
    random_emulator_number = random.getRandomNumberFromZero(
        len(
            emulators
        )-1
    )
    selected_emulator_dictionary = games["emulators"][emulators[random_emulator_number]]

    rom_list = os.listdir(selected_emulator_dictionary["roms"].replace("\"", ""))
    random_rom_number = random.getRandomNumberFromZero(
        len(
            rom_list
        )-1
    )
    rom_for_cmd = selected_emulator_dictionary["roms"].replace("\"", "") + "/" + rom_list[random_rom_number]

    print("Game Type: Emulator")
    print("Chosen emulator: " + str(emulators[random_emulator_number] + "\n"))
    print("You will fight in: " + str(rom_list[random_rom_number] + "\n"))

    cmd = f'{steam_path} -applaunch 1118310 -L {selected_emulator_dictionary["core"]} "{rom_for_cmd}"'

    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    
def run_random_standalone():
    standalone_list = list(games["standalones"].keys())
    random_game_number = random.getRandomNumberFromZero(
        len(
            standalone_list
        )-1
    )
    standalone_key = standalone_list[random_game_number]

    standalone_path = games["standalones"][standalone_key].replace("\"", "")
    print(standalone_path)
    print("Game Type: Standalone")
    print("You will fight in: " + standalone_key + "\n")
    cmd = f'"{standalone_path}"'
    
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def run_random_steam_game():
    

    # Random
    steam_games_list = list(games["steam_games"].keys())
    random_game_number = random.getRandomNumberFromZero(
        len(
            steam_games_list
        )-1
    )
    standalone_key = games["steam_games"][steam_games_list[random_game_number]].replace("\"", "")

    print("Game Type: Steam Game \n")
    print("You will fight in: " + str(steam_games_list[random_game_number]) + "\n")

    cmd = f'{steam_path} -applaunch {standalone_key}'
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


# Program starts here
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


reader = ini_reader()

games = reader.execute()

if games != None:
    steam_path = games["Steam"]

    game_type = []
    for type in list(games):
        if (type != "Steam"):
            game_type.append(type)
    
    random_type = random.getRandomNumberFromZero(len(game_type)-1)

    cmd_operation_result = None
    if game_type[random_type] == "emulators":
        cmd_operation_result = run_random_emulator()
    elif game_type[random_type] == "standalones":
        cmd_operation_result = run_random_standalone()
    elif game_type[random_type] == "steam_games":
        cmd_operation_result = run_random_steam_game()

    if cmd_operation_result.returncode == 0:
        print("GET READY!!! \n")
    else:
        print("It seems there was a problem while trying to run the game. Here is some data that may be useful to find out what happened: \n")
        print(cmd_operation_result)