# This is a sample Python script.
import sys
from wfb_ng import server
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.argv.append('drone')
    sys.argv.append('wlx00c0caad63ee')
    server.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
