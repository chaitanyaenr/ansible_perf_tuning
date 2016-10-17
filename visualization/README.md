# Visualize ansible_facts
This playbook will configure http server to render a static html page showing the parsed ansible_facts.
You can use playbooks/colect/sosreport_facts.yml to collect facts, generate sosreport.

### Run
```
$ ansible-playbook -i hosts --extra-vars '{"RESULTS_PATH": "/path/to/your/collected_facts"}'
```
