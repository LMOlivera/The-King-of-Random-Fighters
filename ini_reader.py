import configparser
import os

class ini_reader:
    def __init__(self):
        pass


    def execute(self):
        try:
            config = self.validate_ini_exists()
            return self.get_data_from_config_file(config)
            
        except IniException as e:
            print(f"config.ini file has encountered an error:\n {e}")

        except KeyError as e:
            print(f"config.ini file has encountered an error:\n {e} Key not found")

        except configparser.NoSectionError as e:
            print(f"config.ini file has encountered an error:\n {e}")

        except Exception as e:
            print("General Exception:")
            print(e)
        
        return None
        

    """
    @description: Validate "config.ini" file exists
    """
    def validate_ini_exists(self):
        config = None
        
        # Check config.ini exists
        if os.path.exists('config.ini'):
            configParser = configparser.ConfigParser()
            configParser.read('config.ini')
            config = configParser
        else:
            raise IniException("\"config.ini\" file was not found, it is essential for running this program.")
        
        return config 
    

    """
    @description: Reads data from "config.ini" file and formats it into a Dictionary for ease of processing.
    """
    def get_data_from_config_file(self, config):
        games = {}

        # Check Steam was specified
        games["Steam"] = config["Steam"]["steam_exe"]
        
        # Check [Retroarch Cores] and [ROMs paths] sections
        emulator_dictionary = self.get_emulators_data(config)
        
        # Check [Standalone games] section
        standalone_dictionary = self.get_standalone_data(config)
        

        # Validate there are enough games for a random selection
        possible_roms = self.count_emulator_games(emulator_dictionary)
        
        possible_standalones = len(standalone_dictionary.values())


        if (possible_roms + possible_standalones > 2):
            if (possible_roms > 0):
                games["emulators"] = emulator_dictionary
            
            if (possible_standalones > 0):
                games["standalones"] = standalone_dictionary
            
            print(f"We found {possible_roms + possible_standalones} possible games to play.")

            return games
        
        else:
            print(f"We found {possible_roms + possible_standalones} possible game(s), not enough to use this program.")
                        
        return config


    """
    @description: Formats emulator data into a Dictionary, based on the contents of "config.ini".
    """
    def get_emulators_data(self, config):
        # Check [Retroarch Cores] section
        emulator_core_dictionary = {}
        for emulator_name, emulator_core_path in config.items("Retroarch Cores"):
            if emulator_name != None and emulator_core_path != None:
                emulator_core_dictionary[emulator_name] = emulator_core_path


        # Check [ROMs paths] section
        emulator_roms_dictionary = {}
        for emulator_name, roms_path in config.items("ROMs paths"):
            if emulator_name != None and roms_path != None:
                emulator_roms_dictionary[emulator_name] = roms_path
        

        # Cores and ROMs validations
        emulator_dictionary = {}
        for emulator in emulator_core_dictionary.keys():
            # If Emulator in Cores has a path for Roms...
            if emulator in emulator_roms_dictionary:

                # Validate there is at least 1 file in folder
                current_emulator_roms_path = emulator_roms_dictionary[emulator].replace('"', '')
                if (len(os.listdir(current_emulator_roms_path)) > 0):
                    emulator_dictionary[emulator] = {
                        "core": emulator_core_dictionary[emulator],
                        "roms": emulator_roms_dictionary[emulator]
                    }
        
        return emulator_dictionary


    """
    @description: Formats standalone data into a Dictionary, based on the contents of "config.ini".
    """
    def get_standalone_data(self, config):
        standalone_dictionary = {}
        for standalone_name, standalone_path in config.items("Standalone games"):
            standalone_dictionary[standalone_name] = standalone_path
        
        return standalone_dictionary


    """
    @description: Counts total amount of games (ROMs).
    """
    def count_emulator_games(self, emulator_dictionary):
        counter = 0

        for emulator, data in emulator_dictionary.items():
            counter += len(
                os.listdir(
                    data["roms"].replace('"', '')
                )
            )

        return counter

"""
@description: Custom exception Wrapper Class.
"""
class IniException(Exception):
    pass