echo [$(date)]:"start"
echo [$(date)]:"creating env with python 3.8 version"

conda create --prefix ./env python=3.8 -y 
echo [$(date)]:"activationg the environment"

# conda init
# conda activate K:\EndtoEndML\env
source activate ./env
echo [$(date)]:"installing the dev requirements"
pip install -r requirements.txt
echo [$(date)]:"END"
