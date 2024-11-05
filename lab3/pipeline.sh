#!/bin/bash

echo "Create dataset"
python3 /app/create_dataset.py

echo "Train model"
python3 /app/train_model.py

echo "Prediction"
python3 /app/make_prediction.py