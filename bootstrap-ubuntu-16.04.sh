#!/usr/bin/env bash

# Recent (16.04+) versions of Ubuntu do not come with python 2
# installed. This script bootstraps the nodes in the inventory by
# installing an appropriate python


ansible all -b -m raw -a 'apt -y update && apt install -y python-minimal' $@
