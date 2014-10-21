#!/usr/bin/env bash

function dmsetup_remove
{
    for table in `dmsetup table | grep $1_ | awk -F ':' '{print $1}'`
    do
        dmsetup remove $table
    done
}

for i in `ps ax|grep vmt |grep python | awk '{print $1}'`;do kill -9 $i;done
iscsiadm --mode node --logout
dmsetup_remove snapshot
dmsetup_remove origin
dmsetup_remove cached

dmsetup remove cache_fcg
dmsetup remove ssd_fcg
dmsetup remove fcg

dmsetup_remove multipath

cd /root/packages/virtman
python setup.py install
cd ..
echo "" > virtman.log
echo "" > virtman.log
#python virtmand.py --debug --log-file virtman.log
