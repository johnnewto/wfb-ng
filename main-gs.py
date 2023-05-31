# This is a sample Python script.
import sys
import os
os.environ['WIFIBROADCAST_CFG'] = '/home/john/PycharmProjects/wfb-ng/wfb_ng/conf/primary.cfg'
print(os.environ['WIFIBROADCAST_CFG'])

from wfb_ng import server
from get_nic import getnic

interfaces = getnic.interfaces()
print (getnic.ipaddr(interfaces))


if __name__ == '__main__':
    sys.argv.append('gs')
    sys.argv.append('wlx00c0caad63f0')
    # sys.argv.append('wlx00c0caad63ee')
    server.main()

