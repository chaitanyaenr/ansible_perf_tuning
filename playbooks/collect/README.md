# ansible_sosreport_facts
Collects sosreport, ansible_facts from remotes on to the local machine and deletes them on remotes.

## Requirements
You need to have these installed on your host
   - Ansible
   - python

### Run
```
$ ansible-playbook -i hosts generate.yml
```
### variables

SOSREPORT_PATH - Directory to save results

HOSTS_PATH - Inventory file path

### override
You can override the variables like
```
$ ansible-playbook --extra-vars '{"HOSTS_PATH":"/tmp/hosts"}' generate.yml
```
### Example output

```

PLAY [test] ********************************************************************

TASK [setup] *******************************************************************
ok: [host.example.com]

TASK [Install sos via dnf] *****************************************************
ok: [host.example.com] => (item=[u'sos', u'rsync', u'ansible'])

TASK [Install sos via yum] *****************************************************
skipping: [host.example.com] => (item=[]) 

TASK [Install rsync on local] **************************************************
changed: [host -> localhost

TASK [results directory] *******************************************************
changed: [host.example.com -> localhost]

TASK [register timestamp] ***********************************************************************
changed: [host.example.com]

TASK [create directory to store reults] ********************************************************************
changed: [host.example.com -> localhost]

TASK [see that directory doesn't have any files] ***************************************************
changed: [host.example.com]

TASK [Run sosreport] ***********************************************************
changed: [host.example.com]]

TASK [Sync the results from remote] ********************************************
changed: [host.example.com]`

TASK [Delete the results on remotes] ******************************************************
changed: [host.example.com]

TASK [Create dir for ansible_facts] ********************************************
changed: [host.example.com -> localhost]

TASK [Collect ansible_facts] ***************************************************
changed: [host.example.com -> localhost]

PLAY RECAP *********************************************************************
host.example.com : ok=12   changed=10   unreachable=0    failed=0

```
