import xml.etree.ElementTree as ET
from typing import Optional
from dataclasses import dataclass

import requests
from pathspec import PathSpec


class Jenkins:

    @dataclass
    class NodeInfo:
        server_url: str
        name: str
        secret: Optional[str]
        work_dir: PathSpec
        internal_dir: PathSpec
        server_url: str

    def __init__(self, server_url, username, api_token):
        self.server_url = server_url
        self.username = username
        self.api_token = api_token

    def _log_in(self, username: str, password: str) -> (str, str):
        response = requests.get(f"{self.server_url}/crumbIssuer/api/json")
        response.raise_for_status()
        payload = response.json()
        return payload["crumbRequestField"], payload["crumb"]

    def get_node_jnlp(self, node_name) -> str:
        response = requests.get(
            f"{self.server_url}/manage/computer/{node_name}/slave-agent.jnlp",
            auth=(self.username, self.api_token),
        )
        response.raise_for_status()
        return response.text

    def get_node_info(self, node_name: str) -> NodeInfo:
        jnlp_info_raw = self.get_node_jnlp(node_name)
        tree = ET.ElementTree(ET.fromstring(jnlp_info_raw))
        arguments = tree.findall("./application-desc/")
        (node_secret, node_name, _, work_dir, _, internal_dir, _, url) = [
            arg.text for arg in arguments[:8]
        ]
        return Jenkins.NodeInfo(url, node_name, node_secret, work_dir, internal_dir)
