#!/bin/sh
cwd=`pwd`

apt-get install -y python-dev python-pip python-setuptools git make gcc tgt open-iscsi
pip install pbr

for p in brick virtman volt python-voltclient
do
	echo installing $p
	cd $p
	python setup.py install
	cd ..
	echo ======================================================================
done

mkdir -p /var/log/volt
touch /var/log/volt/volt-api.log

apt-get install -y linux-headers-`uname -r`

s1=/usr/src/linux-headers-`uname -r`
cd $cwd
cd flashcache
make KERNEL_TREE=$s1
make KERNEL_TREE=$s1 install

cd ../..

modprobe dm_snapshot
sudo ufw disable
