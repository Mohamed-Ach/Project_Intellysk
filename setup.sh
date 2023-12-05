// ** Create The Python Environment {Make Sure Anaconda is installed and set up with $PATH }

conda create --name py11 python=3.11.0 -y


// ** To activate The Conda environment on your terminal {You should notice (py11) added before path to your terminal}

conda activate py11

// ** Check the python version


// ** To deactivate The Conda environment on your terminal 

conda deactivate py11

// ** To install The Correct Module version {Make Sure You're On the same Directory as the requirements.txt File}:

pip install -r requirements.txt


// ** You Run the program in this Repo to check if everything is working fine:

python main.py