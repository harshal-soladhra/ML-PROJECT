# Import necessary modules
import os
import sys
from src.exception import CustomExpection  # Custom exception handling module
from src.logger import logging             # Custom logger module
import pandas as pd

# Scikit-learn utility to split data into train and test sets
from sklearn.model_selection import train_test_split

# Dataclass to simplify class creation for configs
from dataclasses import dataclass

# Configuration class for data ingestion paths
@dataclass
class DataIngestionConfig:
  # Paths where the processed files will be saved
  train_data_path: str = os.path.join('artifacts', 'train.csv')  # Path for training data
  test_data_path: str = os.path.join('artifacts', 'test.csv')    # Path for test data
  raw_data_path: str = os.path.join('artifacts', 'data.csv')     # Path for raw/original data

# Main DataIngestion class responsible for reading, saving and splitting data
class DataIngestion:
  def __init__(self):
    # Initialize configuration instance
    self.ingestion_config = DataIngestionConfig()

  def initiate_data_ingestion(self):
    # Log the start of the data ingestion process
    logging.info('Enter the data ingestion method or component')
    try:
      # Read the dataset from the given CSV file path (absolute path used here)
      df = pd.read_csv(r"D:\machine-learing-full\24-End To End ML Project With Deployment\notebook\data\stud.csv")
      
      # Log successful read of the dataset
      logging.info('read the dataset as datafreame')

      # Create the directory for train/test/raw data if it doesn't exist
      os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

      # Save the full dataset as raw data for record-keeping
      df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

      # Log the start of train-test splitting
      logging.info("train test split initiated")

      # Split the dataset into 80% training and 20% testing data
      train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

      # Save the training data to CSV
      train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

      # Save the testing data to CSV
      test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

      # Log the successful completion of the ingestion process
      logging.info("ingestion of the data is complited")

      # Return the paths of the train and test data files
      return (
        self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path
      )

    # If any error occurs during the process, raise a custom exception
    except Exception as e:
      raise CustomExpection(e, sys)

# Entry point for the script execution
if __name__ == "__main__":
  obj = DataIngestion()              # Create an instance of the DataIngestion class
  obj.initiate_data_ingestion()      # Call the ingestion method
