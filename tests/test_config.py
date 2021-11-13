import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "incorrect_range": 
    {"Item_Weight": 7897897, 
    "Item_Fat_Content": 555, 
    "Item_Visibility": 99, 
    "Item_Type": 99, 
    "Item_MRP": 12000, 
    "Outlet_Size": 789, 
    "Outlet_Location_Type": 75, 
    "Outlet_Type": 20
    },

    "correct_range":
    {"Item_Weight": 21.5, 
    "Item_Fat_Content": 1, 
    "Item_Visibility": 0.32, 
    "Item_Type": 15, 
    "Item_MRP": 270, 
    "Outlet_Size": 2, 
    "Outlet_Location_Type": 2, 
    "Outlet_Type": 2
    },

    "incorrect_col":
    {"Item Weight": 21.5, 
    "Item Fat Content": 1, 
    "Item Visibility": 0.32, 
    "Item Type": 15, 
    "Item MRP": 270, 
    "Outlet Size": 2, 
    "Outlet Location Type": 2, 
    "Outlet Type": 2
    }
}

TARGET_range = {
    "min": 31.0,
    "max": 15000
}

def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert  TARGET_range["min"] <= res <= TARGET_range["max"]

def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert  TARGET_range["min"] <= res["response"] <= TARGET_range["max"]

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)

def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message

def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message