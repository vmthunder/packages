
import subprocess
import re


def get_devkey(prefix='', table=''):
    return [key[:-1] for key in re.findall(prefix+'_\S+:', table)]


def dm_remove(device=''):
    if device != '':
        print 'removing %s' % device
        subprocess.call(['dmsetup', 'remove', device])


def dm_removes(prefix='', table=''):
    devices = get_devkey(prefix, table)
    for device in devices:
        dm_remove(device)


def get_loopkey(table=''):
    return [key[:-1] for key in re.findall(r'/dev/loop\d+:', table)]

pids = subprocess.check_output(["ps aux|grep vmtmanserver.py|awk -F' ' '{print "
                                "$2}'"], shell=True).split()
for pid in pids:
    subprocess.call(['kill -9 ' + pid], shell=True)

devtable = subprocess.check_output(['dmsetup', 'table'])
print 'device mapper table is'
print devtable

#subprocess.call(['/etc/init.d/tgt', 'restart'])
subprocess.call(['iscsiadm', '-m', 'node', '-u'])
subprocess.call(['tgt-admin', '--delete', 'ALL'])

dm_removes('snapshot', devtable)
dm_removes('origin', devtable)
dm_removes('cached', devtable)

dm_remove('cache_fcg')
dm_remove('ssd_fcg')
dm_remove('fcg')

dm_removes('multipath', devtable)

devtable_now = subprocess.check_output(['dmsetup', 'table'])
print 'now, table mapper table is'
print devtable_now

#looptable = subprocess.check_output(['losetup', '-a'])
#loopkeys = get_loopkey(looptable)
#if '/dev/loop0' in loopkeys:
#    index = loopkeys.index('/dev/loop0')
#    del loopkeys[index]
#for key in loopkeys:
#    subprocess.call(['losetup', '-d', key ])

#subprocess.call(['cd /root/packages/virtman && python setup.py install'], shell=True)
subprocess.call(['cd .. && echo "" > virtman.log'], shell=True)
subprocess.call(['cd .. && echo "" > volt.log'], shell=True)
