#!/usr/bin/env python

import vmtapi


with open("image.cfg") as f:

    print "Image Service: Starts ..."
    for line in f.readlines():
        params = line.split()
        if len(params) == 0:
            continue
        if params[0] == '+':
            if len(params) == 4:
                [cmd, image_server_ip, image_name, file_path] = params
                w = vmtapi.create_image_target(image_server_ip, image_name, file_path)
                print params, ' -> ', w
                print 'Image Sever ( ', image_server_ip, ' ) now included: ', vmtapi.list_image_target(image_server_ip)
            else:
                pass

        elif params[0] == '-':
            if len(params) >= 3:
                [cmd, image_server_ip, image_name] = params[:3]
                w = vmtapi.destroy_image_target(image_server_ip, image_name)
                print params, ' -> ', w
                print 'Image Sever ( ', image_server_ip, ' ) now included: ', vmtapi.list_image_target(image_server_ip)
            else:
                pass

        elif params[0] == '@':
            if len(params) == 2:
                [cmd, image_server_ip] = params
                print 'Image Sever ( ', image_server_ip, ' ) now included: ', vmtapi.list_image_target(image_server_ip)
            else:
                pass

        else:
            pass

    print "Image Service: Completed!"
