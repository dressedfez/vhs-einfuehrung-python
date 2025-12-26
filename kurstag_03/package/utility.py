"""
Utility functions for the kurstag_04 project.
"""

import os


def ensure_directory_exists(directory_path):
    """
    Ensure that the specified directory exists. If it does not exist, create it.

    Args:
        directory_path (str): The path of the directory to check or create.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    elif not os.path.isdir(directory_path):
        raise NotADirectoryError(
            f"The path {directory_path} exists but is not a directory."
        )
    # If the directory exists and is a directory, do nothing.
    return directory_path
