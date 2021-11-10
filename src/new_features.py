import pandas as pd
import numpy as np
import pandas as pd
import argparse
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
import warnings
from get_data import read_params
from load_data import load_and_save
from missing_values import trainmissingvalues


def TrainNewfeatures(config_path):
    '''
    Meathod for adding new features deriving
    from already existed features

    input: None
      
    output: return train_data as pandas DataFrame
    '''
    config = read_params(config_path)
    raw_data_path = config["missing_values"]["raw_dataset_csv"]
    train = pd.read_csv(raw_data_path, sep=",")
    
    def feature(s):
        if s<=67.5:
            return 0
        elif (s>67.5) & (s<=134.5):
            return 1
        elif (s>134.5) & (s<=201.1):
            return 2
        else:
            return 3
    train['MRP_bins']=train['Item_MRP'].apply(feature)
    train['new_out']=train['Outlet_Identifier'].str.split('0').str.get(1).astype('int')
    train['total']=2021-train['Outlet_Establishment_Year']
    train['new_item']=train['Item_Identifier'].str[-2:].astype('int')
    train['Item_category']=train['Item_Identifier'].str[:2]
    train.to_csv(raw_data_path, sep=",", index=False)
    
    
if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    TrainNewfeatures(config_path=parsed_args.config)