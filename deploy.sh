#!/bin/bash

eval "$(ssh-agent -s)" &&
ssh-add -k ~/.ssh/id_rsa &&
cd /home/ubuntu/Docker-Api-Ecommerce
git pull

source ~/.profile
echo "$DOCKERHUB_PASS" | sudo docker login --username $DOCKERHUB_USER --password-stdin
sudo docker stop numberforth
sudo docker rm numberforth
sudo docker rmi ilfarro/numberforth
sudo docker run -d --name numberforth -p 5000:5000 ilfarro/numberforth:latest