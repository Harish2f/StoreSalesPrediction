import pandas as pd
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
ll=LabelEncoder()
from get_data import read_params
import argparse

def TrainEncoding(config_path):
    '''Meathod for encoding the 
        train data
        input: None
        output: return encoded train_data as pandas DataFrame'''

    config = read_params(config_path)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    train = pd.read_csv(raw_data_path, sep=",")
    for col in train.columns[train.dtypes=='object'].drop('Item_Identifier','Outlet_Identifier'):
        train[col]=ll.fit_transform(train[col])
    train = train.drop(['Item_Identifier','Outlet_Identifier','Outlet_Establishment_Year'],axis=1)
    train.to_csv(raw_data_path, sep=",", index=False)
    
    
if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    TrainEncoding(config_path=parsed_args.config)