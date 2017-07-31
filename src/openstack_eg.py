"""Example usage of OpenStack libcloud.

This example was tested using trystack. You will need to make sure your
trystack tenant is setup correctly (networks..). Take a look at the following
repository for configuring your trystack tenant.

https://github.com/rywillia/trystack_utilities
"""
from providers import OpenStack
import time

if '__main__' == __name__:
    obj = OpenStack('../examples/auth.yml')

    node = 'node1'
    image = 'Fedora26'
    flavor_size = 'm1.small'
    internal_network = ''

    obj.create(
        node,
        image,
        flavor_size,
        internal_network
    )

    time.sleep(10)

    obj.delete(node)
