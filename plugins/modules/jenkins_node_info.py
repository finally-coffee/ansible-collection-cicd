# pylint: disable=E0401

from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type  # pylint: disable=C0103

from typing import TYPE_CHECKING

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.finallycoffee.cicd.plugins.module_utils.Jenkins import Jenkins

if TYPE_CHECKING:
    from typing import Optional, Dict, Any

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


def run_module():
    module_args = dict(
        name=dict(type="str", required=True, aliases=["node", "node_name"]),
        server=dict(type="str", required=True, aliases=["server_url", "url"]),
        username=dict(type="str", required=True, aliases=["user"]),
        api_token=dict(type="str", required=True, aliases=["password", "pass"]),
    )
    result = dict(changed=False)
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    jenkins = Jenkins(
        module.params["server"], module.params["username"], module.params["api_token"]
    )
    node = jenkins.get_node_info(module.params["name"])

    result["name"] = node.name
    result["secret"] = node.secret
    result["work_dir"] = node.work_dir

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
