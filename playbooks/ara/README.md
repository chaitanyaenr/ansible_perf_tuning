### Ara playbook
Playbook to install, configure and use ara which makes ansible runs easier to visualize and troubleshoot.

### Run
```
$ ansible-playbook -i hosts --extra-vars '{"HOST":"host-to-run-server", "CONFIG_PATH":"/PATH/TO/ANSIBLE.CONFIG"}' ara.yml
```
You can access the dashboard at http://{{ HOST }}:8080 
