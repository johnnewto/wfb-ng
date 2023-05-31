# This is a sample Python script.
import sys
import os
os.environ['WIFIBROADCAST_CFG'] = '/home/john/PycharmProjects/wfb-ng/wfb_ng/conf/primary.cfg'
print(os.environ['WIFIBROADCAST_CFG'])

from wfb_ng import server
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.argv.append('drone')
    sys.argv.append('wlx00c0caad63ee')
    server.main()
