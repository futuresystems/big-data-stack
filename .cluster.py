
from socket import gethostname
import os

defaults = {
    'netmask': '255.255.255.0',
    'public_key': '~/.ssh/id_rsa.pub',
    'private_key': '~/.ssh/id_rsa',
    'domain_name': 'local',
    'extra_disks': {},

    'openstack': {
        'flavor': 'm1.large',
        'image': 'Ubuntu-14.04-64',
        'key_name': gethostname(),
        'network': '{}-net'.format(os.getenv('OS_PROJECT_NAME')),
        'create_floating_ip': False, 
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

N_ZK = 3
N_MASTER = 3
N_DATA = 3
N_FRONTEND = 1
N_LOADBALANCER = 0
N_MONITOR = 1
N_GLUSTER = 0

machines = list(chain(
    expand(zk, N_ZK),
    expand(master, N_MASTER),
    expand(data, N_DATA),
    expand(frontend, N_FRONTEND),
    expand(loadbalancer, N_LOADBALANCER),
    expand(monitor, N_MONITOR),
    expand(gluster, N_GLUSTER)
))

zookeepers = group('zookeepernodes', [(zk, xrange(N_ZK))])
namenodes = group('namenodes', [(master, [0,1])])
journalnodes = group('journalnodes', [(master, xrange(N_MASTER))])
historyservers = group('historyservernodes', [(master, [2])])
resourcemanagers = group('resourcemanagernodes', [(master, xrange(N_MASTER))])
datanodes = group('datanodes', [(data, xrange(N_DATA))])
frontends = group('frontendnodes', [(frontend, xrange(N_FRONTEND))])
glusternodes = group('glusternodes', [(gluster, xrange(N_GLUSTER))])
hadoopnodes = combine('hadoopnodes', namenodes, datanodes,
                      journalnodes, historyservers, frontends)
loadbalancer = group('loadbalancernodes', [(loadbalancer,
                                            xrange(N_LOADBALANCER))])
monitor = group('monitornodes', [(monitor, xrange(N_MONITOR))])

inventory = [
    zookeepers,
    namenodes,
    journalnodes,
    historyservers,
    resourcemanagers,
    datanodes,
    frontends,
    glusternodes,
    hadoopnodes,
    loadbalancer,
    monitor,
]


spec = {
    'defaults': defaults,
    'machines': machines,
    'inventory': inventory,
}


