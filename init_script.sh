echo "A script to create, activate and install requirement.txt"
echo "......................"

virtualenv venv

echo "creation of virtualenv done..."
echo Activation my env"
source venv/bin/activate

echo "......................"
echo "install requirement.txt"
pip -install -r requirement.txt

sleep(2)
echo "Install done"
echo "Creation activation and installation of library done"