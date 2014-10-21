import sys
import  datetime
sys.path.append('..')
from vmthunderclient import client
from time import ctime, sleep
if __name__ == '__main__':
    prop0 = {}
    prop0['target_portal'] = '10.107.14.164:3260'
    prop0['target_iqn'] = 'iqn.2010-10.org.openstack:1'
    prop0['target_lun'] = 1

    prop1 = {}
    prop1['target_portal'] = '10.107.14.168:3260'
    prop1['target_iqn'] = 'iqn.2010-10.org.openstack:1'
    prop1['target_lun'] = 1

    prop2 = {}
    prop2['target_portal'] = '10.107.14.167:3260'
    prop2['target_iqn'] = 'iqn.2010-10.org.openstack:1'
    prop2['target_lun'] = 1

    prop3 = {}
    prop3['target_portal'] = '10.107.14.166:3260'
    prop3['target_iqn'] = 'iqn.2010-10.org.openstack:1'
    prop3['target_lun'] = 1

    client1 = client.Client('10.107.14.169:8001')
    print "----------hello_world-------------"
    #client1.list()
    #client1.destroy('vm1')
    mic_s = datetime.datetime.now()
    client1.create('1', 'vm1', [prop0], '/dev/loop1')
    mic_e = datetime.datetime.now()
    instances = client1.list()['instances']
    print mic_e - mic_s
    for ins in instances:
        print ins['vm_name']
    assert len(instances) == 1, 'failed to create'

    client1 = client.Client('10.107.14.162:8001')
    #client1.list()
    #client1.destroy('vm1')
    mic_s = datetime.datetime.now()
    client1.create('1', 'vm1', [prop0], '/dev/loop1')
    mic_e = datetime.datetime.now()
    print  mic_e - mic_s
    instances = client1.list()['instances']
    for ins in instances:
        print ins['vm_name']
    assert len(instances) == 1, 'failed to create'

    client1 = client.Client('10.107.14.165:8001')
    #client1.list()
    #client1.destroy('vm1')
    mic_s = datetime.datetime.now()
    client1.create('1', 'vm1', [prop0], '/dev/loop1')
    mic_e = datetime.datetime.now() 
    print mic_e - mic_s
    instances = client1.list()['instances']
    for ins in instances:
        print ins['vm_name']
    assert len(instances) == 1, 'failed to create'

    sleep (4)
    client1 = client.Client('10.107.14.166:8001')
    #client1.list()
    #client1.destroy('vm1')
    mic_s = datetime.datetime.now()
    client1.create('1', 'vm1', [prop1, prop0, prop2, prop3], '/dev/loop1')
    print datetime.datetime.now().microsecond/1000000.0
    mic_e = datetime.datetime.now()
    print mic_e - mic_s
    
    instances = client1.list()['instances']
    for ins in instances:
        print ins['vm_name']
    assert len(instances) == 1, 'failed to create'
    


    client1 = client.Client('10.107.14.167:8001')
    #client1.list()
    #client1.destroy('vm1')
    mic_s = datetime.datetime.now()
    client1.create('1', 'vm1', [prop1, prop0, prop2, prop3], '/dev/loop1')
    print datetime.datetime.now().microsecond/1000000.0
    mic_e = datetime.datetime.now()
    print mic_e - mic_s

    instances = client1.list()['instances']
    for ins in instances:
        print ins['vm_name']
    assert len(instances) == 1, 'failed to create'

    client1 = client.Client('10.107.14.168:8001')
    #client1.list()
    #client1.destroy('vm1')
    mic_s = datetime.datetime.now()
    client1.create('1', 'vm1', [prop1, prop0, prop2, prop3], '/dev/loop1')
    print datetime.datetime.now().microsecond/1000000.0
    mic_e = datetime.datetime.now()
    print mic_e - mic_s

    instances = client1.list()['instances']
    for ins in instances:
        print ins['vm_name']
    assert len(instances) == 1, 'failed to create'

    client1 = client.Client('10.107.14.165:8001')
    client1.destroy('vm1')    
    
    client1 = client.Client('10.107.14.166:8001')
    client1.destroy('vm1')

    client1 = client.Client('10.107.14.167:8001')
    client1.destroy('vm1')

    client1 = client.Client('10.107.14.168:8001')
    client1.destroy('vm1')

    client1 = client.Client('10.107.14.162:8001')
    client1.destroy('vm1')

    client1 = client.Client('10.107.14.169:8001')
    client1.destroy('vm1') 

     
    '''
    client1.destroy('vm1')
    instances = client1.list()['instances']
    for ins in instances:
        print ins['vm_name']
    assert len(instances) == 0, 'failed to destroy'

    client1.create('1', 'vm1', [prop0], '/dev/loop1')
    instances = client1.list()['instances']
    print instances
    for ins in instances:
        print ins['vm_name']
    assert len(instances) == 1, 'failed to create'

    client1.create('1', 'vm1', [prop0], '/dev/loop1')
    instances = client1.list()['instances']
    for ins in instances:
        print ins['vm_name']
    assert len(instances) == 1, 'failed to create'

    client1.destroy('vm1')
    instances = client1.list()['instances']
    for ins in instances:
        print ins['vm_name']
    assert len(instances) == 0, 'failed to destroy'

    client1.destroy('vm1')
    instances = client1.list()['instances']
    for ins in instances:
        print ins['vm_name']
    assert len(instances) == 0, 'failed to destroy'
    '''
