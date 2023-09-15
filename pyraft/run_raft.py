import os
import sys
import threading
import time

from pyraft import raft

node = raft.make_default_node()

node.start()
node.join()
