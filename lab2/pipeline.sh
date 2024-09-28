#!/bin/bash

mkdir "/root/home"
cd /root/home
git clone https://github.com/windn19/jenkins.git
cd /root/home/jenkins
python3 -m venv .venv

source  .venv/bin/activate
pip install -r requirements.txt
echo "Create dataset"
python3 create_dataset.py

echo "Train model"
python3 train_model.py

echo "Prediction"
python3 make_prediction.py