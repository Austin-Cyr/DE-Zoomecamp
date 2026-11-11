# navigating in terminalcd /workspaces/DE-Zoomcamp/DE-zoomcamp
git fetch && git status
uv sync
docker compose up
cd /workspaces/DE-Zoomcamp/DE-zoomcamp
lspwd

#check python version
python -V
#to shorten code entry in terminal
PS1="> "
# to add the above step to bashrc - appends it
echo 'PS1="> "' >> ~/.bashrc
# apply teh change 
source ~/.bashrc
# check docker is loaded
docker
# confirm docker is configured correctly 
docker run hello-world # hello world is an image
# run below and you'll be in a ctr
docker run -it ubuntu
# check if python is in this docker image
python3 
# add pythion
apt update
apt install python3
# to check python version
python3 -V
# to get out
exit
# image with python
docker run -it python:3.13.11-slim
# in above, you have a python prompt
# to run with entry point of bash i/o python
docker run -it --entrypoint=bash python:3.13.11-slim
# be careful with below
 rm -rf - ## be carefule
 # to look at docker ctrs that were run during session
 docker run -it --entrypoint=bash python:3.13.11-slim
 # goal to remove ctrs, start with below
 docker ps -aq # this gets the id fo ctrs
 # belwo will remove ctrs -- make sure to use the `
 docker rm `docker ps -aq`
 # to check docker environment
 docker ps -a
 # to run a py file 
 python script.py
 # to map folders on your pc/git to docker from test onwards to python can change
 docker run -it --entrypoint=bash -v $(pwd)/test:/app/test python
:3.13.11-slim
# can then run files from your pc bc they are mapped to the virtual container
root@f9df81042b3c:/app/test# python script.py
# need to install pandas
pip install pandas
# need ot install pyarrow to use parquet
pip install pyarrow
