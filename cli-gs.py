# This is a sample Python script.
import sys
from wfb_ng import cli
# Press the green button in the gutter to run the script.
# from get_nic import getnic
#
# interfaces = getnic.interfaces()
# print (getnic.ipaddr(interfaces))
if __name__ == '__main__':
    sys.argv.append('gs')
    cli.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
