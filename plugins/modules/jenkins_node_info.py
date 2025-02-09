# pylint: disable=E0401

from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type  # pylint: disable=C0103

from typing import TYPE_CHECKING

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.finallycoffee.cicd.plugins.module_utils.Jenkins import Jenkins
from ansible_collections.finallycoffee.cicd.plugins.module_utils.docs.jenkins_node_info import (
    DOCUMENTATION,
    EXAMPLES,
    RETURN,
)

if TYPE_CHECKING:
    from typing import Optional, Dict, Any


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
