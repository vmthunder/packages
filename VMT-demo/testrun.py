import vmtapi
import time
import threading

MAX_THREAD = 60


def run_api(*line):
    params = line
    if len(params) == 0:
        return 0
    if params[0] == '+':
        if len(params) == 5:
            [cmd, node_ip, instance_name, image_server_ip, image_name] = params
            vmtapi.create(node_ip, instance_name, image_server_ip, image_name)
            print 'Compute Node  %s now included: %s' % \
                  (node_ip, vmtapi.list(node_ip))
        else:
            return 0

    elif params[0] == '-':
        if len(params) >= 3:
            [cmd, node_ip, instance_name] = params[:3]
            vmtapi.destroy(node_ip, instance_name)
            print 'Compute Node  %s now included: %s' % \
                  (node_ip, vmtapi.list(node_ip))
        else:
            return 0

    elif params[0] == '@':
        if len(params) == 2:
            [cmd, node_ip] = params
            print 'Compute Node  %s now included: %s' % \
                  (node_ip, vmtapi.list(node_ip))
        else:
            return 0

if __name__ == '__main__':
    with open("nodelist.cfg") as f:
        print "Virtman Run ..."
        start_time = time.time()
        line_list = f.read().strip().split("\n")
        index = 0
        while index < len(line_list):
            thread_number = min(MAX_THREAD, (len(line_list)-index))
            thread_list = []
            for thread_id in range(thread_number):
                thread = threading.Thread(target=run_api,
                                          args=(line_list[index].split()))
                thread.start()
                thread_list.append(thread)
                index += 1
            for thread in thread_list:
                thread.join()
        end_time = time.time()
        print  end_time-start_time
