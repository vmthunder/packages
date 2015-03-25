import argparse
import re
# import pickle

MASTER = '10.107.8.10'
IPS = (
#'10.107.8.10',
 '10.107.8.20',
)


def check_ip(string):
    pattern = re.compile(r'((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.)'
                         r'{3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))')
    match = pattern.match(string)
    if match:
        return True
    return False

def ip_type(string):
    if check_ip(string):
        return string
    msg = "%r is not a ip type" % string
    raise argparse.ArgumentTypeError(msg)

parser = argparse.ArgumentParser()

parser.add_argument('-a', action="store", dest="action", default='+',
                    choices=['+', '-'])
parser.add_argument('-i', action="store", dest="img_addr", default=MASTER,
                    type=ip_type)
parser.add_argument('-n', action="store", dest="img_name", type=str)
parser.add_argument('-m', action="store", dest="vm_num", default=0, type=int)

arg_results = parser.parse_args()

ip_List = IPS

# with open("running_list.pk", 'rb') as input_file:
#     running_list = pickle.load(input_file)
#
# ip_List = [i[1] for i in running_list]
print ip_List

with open('nodelist.cfg', "w+") as cfg_file:
    if arg_results.vm_num > 0:
        for num in range(1, arg_results.vm_num + 1):
            for ip in ip_List:
                cfg_file.writelines("%s %s vm_%s_%s %s %s\n" %
                                    (arg_results.action, ip,
                                     arg_results.img_name, num,
                                     arg_results.img_addr,
                                     arg_results.img_name))
