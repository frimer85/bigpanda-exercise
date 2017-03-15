#!/usr/bin/python3

import os
import argparse

__author__ = 'Moran Frimer'

service_list = ["gify-panda", "counter-panda"]

def get_args():
    '''This function parses and return arguments passed in'''
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description='Deployment script for python nanoservices: gify-panda and counter-panda')
    # Add arguments
    parser.add_argument(
        '-s', '--service', type=str, help='Service Name. '+str(service_list), required=True)
    parser.add_argument(
        '-b', '--branch', type=str, help='Branch to deploy', required=True)
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    service = args.service
    branch = args.branch
    # Return all variable values
    return service, branch

service, branch = get_args()

if service not in service_list:
    print("ERROR: service argument must be on of this: " + str(service_list))
    exit(1)

os.system("git fetch")
os.system("git checkout " + branch)

os.system("vagrant up --no-provision")
os.system('ansible-playbook --private-key=.vagrant/machines/base/virtualbox/private_key -u vagrant -i dev/hosts -e "service=' + service + '" base.yml')
