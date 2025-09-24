
import os
import sys
import pandas as pd
from dataclasses import dataclass

from src.pipeline.exception import CustomException
from src.pipeline.logger import logging
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion paths.
    This dataclass will hold the paths for raw, train, and test data files.
    """
    train_data_path: str = os.path.join('artifacts', "train.csv") #
    test_data_path: str = os.path.join('artifacts', "test.csv")  #
    raw_data_path: str = os.path.join('artifacts', "data.csv")   #

class DataIngestion:
    def __init__(self):
        """
        Initialises the DataIngestion class with the configuration.
        """
        self.ingestion_config = DataIngestionConfig() #

    def initiate_data_ingestion(self):
        """
        This method reads data from a source, splits it into training and testing sets,
        and saves them to the artifact directory.
        """
        logging.info("Entered the data ingestion method or component") #
        try:
            # Read the dataset into a pandas DataFrame
            # In a real-world scenario, this could be from a database or an API
            df = pd.read_csv('notebook/data/stud.csv') #
            logging.info('Read the dataset as dataframe') #

            # Create the 'artifacts' directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) #

            # Save the raw data to the specified path
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) #

            # Initiate the train-test split
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42) #

            # Save the training data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            # Save the testing data
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed") #

            # Return the paths of the train and test data for the next component (data transformation)
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # Raise a custom exception if any error occurs
            raise CustomException(e, sys)

# This block allows the script to be run directly for testing purposes
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()