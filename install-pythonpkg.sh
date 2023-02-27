sudo apt-get update
sudo apt-get install -y python3 python3-dev python3-setuptools gcc libtinfo-dev zlib1g-dev build-essential cmake libedit-dev libxml2-dev
python -m pip install --upgrade pip 
pip install  Cython
pip install  numpy decorator attrs
pip install typing-extensions
pip install  tornado psutil 'xgboost>=1.1.0' cloudpickle
pip install pytest

