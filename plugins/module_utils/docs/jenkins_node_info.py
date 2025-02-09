DOCUMENTATION = r"""
---
module: jenkins_node

short_description: Retrieve Jenkins node information
# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "0.0.1"

description: This is my longer description explaining my test module.

options:
    name:
        description: The name of the jenkins node.
        required: true
        type: str
        aliases:
        - agent
    server:
        description: URL of the jenkins instance
        required: true
        type: str
        aliases:
        - server_url
    username:
        description: Username to use for authentication to jenkins
        required: true
        type: str
        aliases:
        - user
    api_token:
        description: Jenkins API token for the user
        required: true
        type: str
author:
    - transcaffeine (@transcaffeine)
"""

EXAMPLES = r"""
# Pass in a message
- name: Retrieve information about the jenkins node named 'my_jenkins_node_name'
  finallycoffee.cicd.jenkins_node_info:
    name: my_jenkins_node_name
    server: https://jenkins.example.org
    username: admin
    api_token: yoursecretapitokenhere
"""

RETURN = r"""
# These are examples of possible return values, and in general should use other names for return values.
name:
    description: The name of the jenkins node
    type: str
    returned: always
    sample: 'jenkins-agent-jdk21-alpine'
secret:
    description: The secret of the agent
    type: str
    returned: always
    sample: 'secretverylongstringwith64chars'
work_dir:
    description: The local working directory of the jenkins agent
    type: str
    returned: always
"""
