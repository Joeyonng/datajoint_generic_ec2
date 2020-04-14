# This file is the script to execute on each instance in one cluster.
#
# First of all, we need to initialize the instance.
# Set variables
export BASE_PATH="data/Github/"
export GIT_REPO="https://github.com/Joeyonng/datajoint_generic_ec2.git"
export GIT_NAME="datajoint_generic_ec2"
# Download your GitHub project.
cd $BASE_PATH
sleep $(shuf -i 1-10 -n 1)
rm -rf $GIT_NAME # If your GitHub project has existed in the AMI and is up-tp-date, comment this line.
git clone $GIT_REPO

# Activate or set up the virtual environment. Ensure essential tools are ready in the AMI (virtualenv or Anaconda).
# It is better to have the environment and required packages installed in the AMI.
# Option 1: Create a configure.sh file in your GitHub project to set up the environment. (Recommend)
source $GIT_NAME/configure.sh
# Option 2: Set up the environment here. Use conda or virtualenv.
# ...

# Run the task file.
python schema.py

