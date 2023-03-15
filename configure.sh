#!/bin/bash
whoami=user
echo "alias oneshot='python3 ${PWD}/oneshot.py'" >> /home/$USER/.bashrc
source /home/$USER/.bashrc
