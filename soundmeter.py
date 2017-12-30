#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import commands
import os
import re
import time
import json

# agentの起動時にグラフ定義情報を出力
if os.environ.get('MACKEREL_AGENT_PLUGIN_META') == '1':
    meta = {
        'graphs': {
            'room-noice-RMS': {
                'label': 'room-noice-RMS',
                'unit': 'integer',
                'metrics': [
                    {
                        'name': 'min',
                        'label': 'Min',
                    },
                    {
                        'name': 'max',
                        'label': 'Max',
                    },
                    {
                        'name': 'avg',
                        'label': 'Avg',
                    },
                ],
            },
        },
    }
    print '# mackerel-agent-plugin'
    print json.dumps(meta)
    sys.exit()

# notice mackerel-agentのpluginのcommandは，30秒でtimeoutになる
cmd = '/usr/local/bin/soundmeter -s %s -c' % os.getenv('COLLECT_SOUND_SECONDS', 3)
output = commands.getoutput(cmd)

time = time.time()
for line in output.split("\n"):
    m = re.match(r"^\s+(min|max|avg):\s+(\d+)", line)
    if m is not None:
        print "\t".join(str(e) for e in [
            m.groups()[0],
            m.groups()[1],
            time
            ])
