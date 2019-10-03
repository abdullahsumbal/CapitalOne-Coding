import sys
import json
import argparse
from helper import *
from CLanguage import CLanguage
from JavaLanguage import JavaLanguage
from PythonLanguage import PythonLanguage
from LanguageInformation import LanguageInformation

# args parser
parser = argparse.ArgumentParser(description='Count Comments')
parser.add_argument(
    '-c',
    '--config_path',
    type=str,
    default="template-config.json",
    help='provide an config file (default: template-config.json)'
)

if __name__ == "__main__":
    # main logic to file.

    # get config file path from args or use default
    config_file = parser.parse_args().config_path

    # load json file
    try:
        with open(config_file, "r") as read_file:
            config = json.load(read_file)
    except FileNotFoundError:
        print(f'{config_file} does not exist')
        sys.exit()

    # data from config file
    source_directory = config["source_directory"]
    languages = config["languages"]

    # filter files with extension defined in the config file
    source_files = get_files_in_directory(source_directory)
    map_ext_to_lang = get_acceptable_ext_and_lang(languages)
    acceptance_files_and_lang = get_acceptance_source_files(source_files, map_ext_to_lang)

    # initialize languageInformation class and reuse object
    info = LanguageInformation()
    # call language classes
    for file_path, language_name in acceptance_files_and_lang:
        if language_name == "python":
            info.language = PythonLanguage(file_path)
        elif language_name == "java":
            info.language = JavaLanguage(file_path)
        elif language_name in ["c", "cplus", "csharp", "js"]:
            info.language = CLanguage(file_path)

        info.get_comment_info()
        print(f"File Name: {file_path}")
        print(info.language)

