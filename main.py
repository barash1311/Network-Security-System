from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys
if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        dataIngestion=DataIngestion(dataingestionconfig)
        logging.info("initiate the data ingestion")
        artifact=dataIngestion.inititate_data_ingestion()
        print(artifact)
        
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)