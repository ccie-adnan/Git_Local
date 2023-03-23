import yaml
from pprint import pprint
with open('172.16.30.101.yaml', 'r') as file:
    data=yaml.load(file, Loader=yaml.FullLoader)
    #pprint(data)
    Router_ID = (data['bgp']['router_id'])
    Networks = (data['bgp']['networks'])
    for network in Networks:
        print(network[0])
    