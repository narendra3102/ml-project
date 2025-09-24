import os
import sys
import dill #
import numpy as np #
import pandas as pd #

from src.pipeline.exception import CustomException #

def save_object(file_path, obj):
    """
    Saves a Python object to a file using dill.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Opens the file path in write-byte mode and saves the object
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys) #