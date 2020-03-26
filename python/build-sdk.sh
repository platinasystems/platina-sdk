#!/bin/bash
sudo -H python3 setup.py sdist
sudo -H pip3 uninstall -y platina_sdk
echo "*** Running PIP install"
export VERSION=`python3 platina_sdk/get_version.py`
sudo -H pip3 install dist/platina_sdk-${VERSION}.tar.gz 
