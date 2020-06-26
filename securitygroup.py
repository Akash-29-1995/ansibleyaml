import sys
import boto
from boto import ec2
from boto import sns
connection=ec2.connect_to_region("us-east-1")

sg=connection.get_all_security_groups()
listOfInstances=""
messages="Following Instances have port 22 open"
def getTag(instanceId):
    reservations=connection.get_all_instances(filters={'instance_id':instanceId})
    for r in reservations:
        for i in r.instances:
            return i.tags['Name']
try:
    for securityGroup in sg:
        for rule in securityGroup.rules:
            global instanceId;
            if (rule.from_port=='22' and rule.to_port == '22') and '0.0.0.0/0' in str(rule.grants):
                for instanceid in securityGroup.instances():
                    print(instanceid)
                    instanceId=str(instanceid)
                    listOfInstances += "Instance Name : " + getTag(instanceId.split(':')[1]) + "\t State:" + instanceid.state + "\t SecurityGroup:" +securityGroup.name + "\n"
                    print(listOfInstances)
except :
    print('Some Error occurred : ')
    print(sys.exc_info())