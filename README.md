# `finallycoffee.cicd` ansible collection

## Overview

This collection contains roles focused on various components around CI/CD, including
automation servers like Jenkins, its agents or vaguely related components like caching
proxies and artifact registries.

## Roles

- [`jenkins`](roles/jenkins/README.md): Deploy [jenkins](https://jenkins.io), the self-proclaimed 'leading open source automation server'.
- [`jenkins_inbound_agent`](roles/jenkins_inbound_agent/README.md): Deploy Jenkins 'inbound agent', formerly known as 'JNLP agent'.

## License

[CNPLv7+](LICENSE.md): Cooperative Nonviolent Public License
