#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import commands
import os
import re
import time
import requests
import json

cmd = '/usr/local/bin/soundmeter -s 30 -c'
output = commands.getoutput(cmd)

if os.environ.get('MACKEREL_AGENT_PLUGIN_META') == '1':
    #TODO mackrel agent
    sys.exit()

params = []
for line in output.split("\n"):
    m = re.match(r"^\s+(min|max|avg):\s+(\d+)", line)
    if m is not None:
        #print "\t".join(str(e) for e in ['soundmeter.rms.' + m.groups()[0], m.groups()[1], int(time.time())])
        params.append({
            "name": m.groups()[0],
            "time": int(time.time()),
            "value": int(m.groups()[1])
            })

serviceName = 'room-noice-RMS'
appendedHeaders = {
        "Content-Type": "application/json",
        'X-Api-Key': os.environ.get('MACKEREL_API_KEY')
        }
res = requests.post(
        "https://mackerel.io/api/v0/services/%s/tsdb" % (serviceName),
        json.dumps(params),
        headers=appendedHeaders
        )
#print(res.json())


