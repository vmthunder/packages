#!/usr/bin/env python

import xmlrpclib


"""
    //An Example for Calling Python Code in Java
    import org.python.core.PyFunction;
    import org.python.core.PyInteger;
    import org.python.core.PyObject;
    import org.python.util.PythonInterpreter;

    public class Test
    {
        public static void main(String args[])
        {
            PythonInterpreter interpreter = new PythonInterpreter();
            interpreter.execfile("E:\\vmtapi.py");
            PyFunction vmtcreate = (PyFunction)interpreter.get("create", PyFunction.class);
            PyFunction vmtdestroy = (PyFunction)interpreter.get("destroy", PyFunction.class);
            PyFunction vmtlist = (PyFunction)interpreter.get("list", PyFunction.class);

            //String node_ip="192.168.63.101", instance_name="vm1", image_name="image1", image_server_ip="192.168.63.16";
            PyObject pyobj = vmtcreate.__call__(new PyString(node_ip), new PyString(instance_name), new PyString(image_name), new PyString(image_server_ip));
            PyObject pyobj = vmtdestroy.__call__(new PyString(node_ip), new PyString(instance_name));
            PyObject pyobj = vmtlist.__call__(new PyString(node_ip));
            System.out.println("Anwser = " + pyobj.toString());
        }
    }
"""


def create(node_ip, instance_name, image_server_ip, image_name, image_server_port=3260,
           iqn_prefix='iqn.2010-10.org.openstack:', target_lun=1, snapshot_dev=None):
    """
    :param node_ip:                 string, the compute node to create a VM instance
    :param instance_name:           string, a name of the VM instance to create
    :param image_name:              string, which image to use in the Image Server
    :param image_server_ip:         string, the ip of the Image Server
    :param image_server_port:       (optional) int, the port of the image target in the Image Server
    :param iqn_prefix:              (optional) string, the prefix of the image target's name in the Image Server,
    :param target_lun:              (optional) int, target_lun of the image target in the Image Server
    :param snapshot_dev:            (optional) string, the block device in this compute node to create the VM
    :returns : string
        "0:info" specifies SUCCESS, info=instance_path, instance_path is '' or like '/dev/mapper/snapshot_vm1' in local deployment
        "1:info" specifies WARNING, info indicates instance_name exists
    """
    if not image_name.startswith("volume-"):
            image_name = "volume-" + image_name
    image_connection = {
        'target_portal': image_server_ip + ':' + str(image_server_port),
        'target_iqn': iqn_prefix + image_name,
        'target_lun': target_lun,
    }
    server = xmlrpclib.ServerProxy('http://%s:7774' % node_ip, allow_none=True)
    print "Instance starts in", node_ip, ", name =", instance_name, " in server node ", server
    return server.create(instance_name, image_name, image_connection, snapshot_dev)


def destroy(node_ip, instance_name):
    """
    :param node_ip:             the compute node to destroy a VM instance
    :param instance_name:       a name of the VM instance to destroy
    :returns : string
        "0:info" specifies SUCCESS, info=""
        "1:info" specifies WARNING, info indicates instance_name not exists
    """
    server = xmlrpclib.ServerProxy('http://%s:7774' % node_ip)
    return server.destroy(instance_name)


def list(node_ip):
    """
    :param node_ip:             the compute node to list VM instances
    :returns :                  a list, like ["instance_name+':'+image_id",..]
    """
    server = xmlrpclib.ServerProxy('http://%s:7774' % node_ip)
    return server.list()


def create_image_target(image_server_ip, image_name, file_path, loop_dev=None,
                        iqn_prefix='iqn.2010-10.org.openstack:'):
    """
    :param image_server_ip:         string, the Image Sever node to create an image Target
    :param image_name:              string, which image to use to create target in the Image Server
    :param file_path:               string, the realpath of the image
    :param loop_dev:                (optional) string, the loop device for the image file to bind
    :param iqn_prefix:              (optional) string, the prefix of the image target's name, like 'iqn.2010-10.org.openstack:'
    :returns : string
        "0:info" specifies SUCCESS, info="target_id:loop_dev", target_id (int) is the id of the target in the the Image Sever node
        "1:info" specifies WARNING, info indicates image_name exists
        "2:info" specifies WARNING, info indicates image file_path not exists
    """
    server = xmlrpclib.ServerProxy('http://%s:7774' % image_server_ip, allow_none=True)
    return server.create_image_target(image_name, file_path, loop_dev, iqn_prefix)


def destroy_image_target(image_server_ip, image_name):
    """
    :param image_server_ip:         string, the Image Sever node to destroy an image Target
    :param image_name:              string, which image to use to destroy target in the Image Server
    :returns : string
        "0:info" specifies SUCCESS, info="nothing"
        "1:info" specifies WARNING, info indicates image_name not exists
    """
    server = xmlrpclib.ServerProxy('http://%s:7774' % image_server_ip)
    return server.destroy_image_target(image_name)

def list_image_target(image_server_ip):
    """
    :param image_server_ip:         string, the Image Sever node to list image Target
    :returns :                      a list, like ["image_name+':'+target_id+':'+loop_dev",..]
    """
    server = xmlrpclib.ServerProxy('http://%s:7774' % image_server_ip)
    return server.list_image_target()

