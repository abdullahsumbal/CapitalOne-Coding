import os
import glob


def get_files_in_directory(source_directory):
    """
    get all file in directory recursively
    :param source_directory: name/path of the directory to look in
    :return: list of files found in the directory
    """
    return glob.glob(source_directory + "/*")


def get_acceptable_ext_and_lang(languages):
    """
    Get acceptable extension specified in config file
    :param languages: dictionary of programing language
    :return: dictionary of acceptable extensions (key)
            and languages (value)
    """
    map_ext_to_lang = {}
    for language, language_info in languages.items():
        extension = language_info["ext"]
        map_ext_to_lang[extension] = language
    return map_ext_to_lang


def get_acceptance_source_files(file_paths, map_ext_to_lang):
    """
    Get acceptable source files with extension specified in the config file
    :param file_paths: list of files to validate based on extension
    :param map_ext_to_lang: dictionary of acceptable extensions (key)
            and languages (value)
    :return: list of tuple of acceptable files based on extension in the map_ext_to_lang
    """
    acceptance_files_and_lang = []
    for file_path in file_paths:
        _, file_extension = os.path.splitext(file_path)
        if file_extension in map_ext_to_lang:
            acceptance_files_and_lang.append((file_path, map_ext_to_lang[file_extension]))
    return acceptance_files_and_lang