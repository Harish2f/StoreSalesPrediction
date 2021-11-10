import argparse
import numpy as np
import pandas as pd
from get_data import read_params


def trainmissingvalues(config_path):
    config = read_params(config_path)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    train = pd.read_csv(raw_data_path, sep=",")
    train['Item_Weight'].fillna(0,inplace = True)
        
    ind = train[train['Item_Weight'] == 0].index
    for i in ind:
        it=train.iloc[i,0]
        train.iloc[i,1]=np.mean(train[train['Item_Identifier']==it]['Item_Weight'])
        
    train['Item_Weight'].replace(0,np.mean(train['Item_Weight']),inplace=True)
    train['Outlet_Size'].fillna('Missing',inplace=True)
    train['Outlet_Size'].replace('Missing','Small',inplace=True)
              
    train['Item_Fat_Content'].replace(['Low Fat','Regular','LF','reg','low fat'],['LF','REG','LF','REG','LF'],inplace=True)
    ind=train[train['Item_Visibility']==0].index
        
    for i in ind:
        it=train.iloc[i,1]
        train.iloc[i,3]=np.mean(train[train['Item_Weight']==it]['Item_Visibility'])
        
    return train


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    trainmissingvalues(config_path=parsed_args.config)




