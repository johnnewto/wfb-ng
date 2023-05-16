# This is a sample Python script.
import sys
import os
os.environ['SOME_VAR'] = 'qwerty'
os.environ['WIFIBROADCAST_CFG'] = 'wifibroadcast.cfg'
# print(os.environ['WIFIBROADCAST_CFG'])

from wfb_ng import server
# Press the green button in the gutter to run the script.
from get_nic import getnic

interfaces = getnic.interfaces()
print (getnic.ipaddr(interfaces))
if __name__ == '__main__':
    sys.argv.append('gs')
    sys.argv.append('wlx00c0caad63f0')
    # sys.argv.append('wlx00c0caad63ee')

    server.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
