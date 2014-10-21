#!/usr/bin/env python

import vmtapi


with open("nodelist.cfg") as f:

    print "Virtman Run ..."
    for line in f.readlines():
        params = line.split()
        if len(params) == 0:
            continue
        if params[0] == '+':
            if len(params) == 5:
                [cmd, node_ip, instance_name, image_server_ip, image_name] = params
                vmtapi.create(node_ip, instance_name, image_server_ip, image_name)
                print 'Compute Node ( ', node_ip, ' ) now included: ', vmtapi.list(node_ip)
            else:
                pass

        elif params[0] == '-':
            if len(params) >= 3:
                [cmd, node_ip, instance_name] = params[:3]
                vmtapi.destroy(node_ip, instance_name)
                print 'Compute Node ( ', node_ip, ' ) now included: ', vmtapi.list(node_ip)
            else:
                pass

        elif params[0] == '@':
            if len(params) == 2:
                [cmd, node_ip] = params
                print 'Compute Node ( ', node_ip, ' ) now included: ', vmtapi.list(node_ip)
            else:
                pass

        else:
            pass
    print "Virtman Runs Out!"