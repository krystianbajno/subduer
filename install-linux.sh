#!/bin/bash

sudo apt update
sudo apt install -y python3 python3-pip python3-venv
sudo apt install python3-playwright

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
pip install pytest-playwright playwright -U

playwright install-deps
playwright install --with-deps
playwright install

echo "Installation complete!"
