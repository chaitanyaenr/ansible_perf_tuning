### Ara playbook
Playbook to install, configure and use ara which makes ansible runs easier to visualize and troubleshoot.

### Run
```
$ ansible-playbook -i hosts --extra-vars '{"HOST":"host-to-run-server", "CONFIG_PATH":"/PATH/TO/ANSIBLE.CONFIG", "PORT":"port"}' ara.yml
```

### systemd
systemd is configured to start ara on failures, boot

By default if you do not mention any port, it runs on 8080, you can access the dashboard at http://{{ HOST }}:8080 
