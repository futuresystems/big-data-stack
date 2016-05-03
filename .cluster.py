
from socket import gethostname
import os

defaults = {
    'netmask': '255.255.255.0',
    'public_key': '~/.ssh/id_rsa.pub',
    'private_key': '~/.ssh/id_rsa',
    'domain_name': 'local',
    'extra_disks': {},

    'openstack': {
        'flavor': 'm1.small',
        'image': 'CC-Ubuntu14.04',
        'key_name': gethostname(),
        'network': '{}-net'.format(os.getenv('OS_PROJECT_NAME')),
        'create_floating_ip': True, 
        'floating_ip_pool': 'ext-net',
        'security_groups': ['default'],
    },

    'vagrant': {
        'provider': 'libvirt',
        'box': 'ubuntu/14.04'
    },

    'provider': 'openstack',
}


zk = lambda i: {
    'zk%d' % i: {}
}

master = lambda i: {
    'master%d' % i: {}
        # 'openstack': {'security_groups': ['default', 'hadoop-status']}
}

data = lambda i: {
    'data%d' % i: {}
}

frontend = lambda i: {
    'frontend%d' % i: {
        # 'extra_disks': {'vdb': {'size': '10G'}},
        # 'openstack': {'create_floating_ip': True},
    }
}

loadbalancer = lambda i: {
    'loadbalancer%d' % i: {
        # 'openstack': {'flavor': 'm1.medium',
        #               'security_groups': ['default', 'sshlb'],}

    }
}

monitor = lambda i: {
    'monitor%d' % i: {}
}

gluster = lambda i: {
    'gluster%d' % i: {
        'ip': '10.0.6.{}'.format(i+10),
        'openstack': {'flavor': 'm1.large',}

    }
}


from vcl.specification import expand, group, combine, chain

N_MASTER = 3
N_DATA = 3

machines = list(chain(
    expand(master, N_MASTER),
    # expand(data, N_DATA),
))

_zookeepernodes = [(master, [0,1,2])]
_namenodes = [(master, [0, 1])]
_journalnodes = [(master, [0,1,2])]
_historyservers = [(master, [2])]
_resourcemanagers = [(master, [0,1])]
_datanodes = [(master, xrange(N_DATA))]
_frontends = [(master, [0])]
_monitor = [(master, [2])]



zookeepers = group('zookeepernodes', _zookeepernodes)
namenodes = group('namenodes', _namenodes)
journalnodes = group('journalnodes', _journalnodes)
historyservers = group('historyservernodes', _historyservers)
resourcemanagers = group('resourcemanagernodes', _resourcemanagers)
datanodes = group('datanodes', _datanodes)
frontends = group('frontendnodes', _frontends)
hadoopnodes = combine('hadoopnodes', namenodes, datanodes,
                      journalnodes, historyservers, frontends)
monitor = group('monitornodes', _monitor)

inventory = [
    zookeepers,
    namenodes,
    journalnodes,
    historyservers,
    resourcemanagers,
    datanodes,
    frontends,
    hadoopnodes,
    monitor,
]


spec = {
    'defaults': defaults,
    'machines': machines,
    'inventory': inventory,
}


######################################################################
# hack to define zookeeper_id for zookeeper nodes automatically

host_vars = 'host_vars'
if not os.path.exists(host_vars):
    os.makedirs(host_vars)

import time
zk_id = 0
for grp in zookeepers.itervalues():
    for host in grp:
        zk_id += 1
        host_file = os.path.join(host_vars, host)
        if os.path.exists(host_file):
            print 'WARNING', host_file, 'already exists'
            now = time.time()
            bkp = host_file + '.' + str(now)
            os.rename(host_file, bkp)
        entry = 'zookeeper_id: {}\n'.format(zk_id)
        print host_file, 'WROTE', entry
        with open(host_file, 'w') as fd:
            fd.write(entry)
