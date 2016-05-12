## Ansible playbook to deploy nagios+nrpe
### What is this playbook?

This playbook helps to deploy nagios and nrpe with essential monitoring
resources configurations (CPU, RAM, Swap, connected users)


Tested environment:

- Ansible 2.0.2.0

- Remote host: CentOS 6.7 Final

    - Nagios Core 3.5.1

    - Nagios plugin 2.0.3

    - NRPE 2.15

### Configuration file

This playbook centralizes configurations into file `config.yml`.

- `nagios_lan_iface`: Specify interface for services. Useful when you have
  multiple interfaces in server.
    
    - Default value: `eth0`

- `nagios_admin_user`: Admin account to login nagios web interface.

    - Default value: `nagiosadmin`

- `nagios_admin_password`: Password for admin account.

    - Default value: `nagios`

- `nagios_email`: Email to send notification.

    - Default value: `root@localhost.localdomain`


### Template files in roles

There are only two roles: `nagios` and `nrpe`. 

This playbook automatically generate custom configuration files for monitored
server in each role.

-`nagios` role: custom configurations are stored in `templates/hosts`. These
files are generated from `files/nagios_commons.cfg` file. When you have changes
to monitored servers, you should edit files in `templates/hosts/`.

-`nrpe` role: custom configurations are stored in `templates/nrpe.d`. These
files are generated on first run from `files/nrpe_commons.cfg` file. When you
have changes to monitored servers, you should edit files in `templates/nrpe.d/` 


### How to run

Clone this repository into your machine. 

Execute:

```
$ ansible-playbook -i inventory site.yml
```

### License

[MIT](https://github.com/cuongnv23/ansible-nagios-nrpe/blob/master/LICENSE)
