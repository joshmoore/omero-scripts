#!/usr/bin/env python

import omero
from omero.scripts import client
from omero.gateway import BlitzGateway
from multiprocessing import Process
import os
import time


c = client(name="multiprocessing example")
uuid = c.getSessionId()
props = c.getPropertyMap()

def lts():
    c = omero.client(props)
    c.joinSession(uuid)
    gw = BlitzGateway(client_obj=c)
    print "Connected", gw.isConnected()
    ms = gw.getMetadataService()
    print "LTS Begin"
    ms.loadTagSets(options=None)
    print "LTS Complete"

if __name__ == "__main__":
    print "PreThread Test"
    lts()
    print "Start"
    before = time.time()

    p = Process(target=lts)
    p.start()
    p.join()

    after = time.time()
    taken = after-before
    print taken
