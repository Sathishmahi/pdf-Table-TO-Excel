echo "CREATE ENV"
conda create -p venv python=3.10 -y 
echo "ACTIVATE ENV"
source activate ./venv
echo "DOWNLOAD REQUIREMENTS"
pip install -r requirements_dev.txt
echo "FINSH DOWNLOAD REQUIREMENTS"