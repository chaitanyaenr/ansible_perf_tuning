# ansible_perf_tuning
Tunes the performance of ansible by changing the number of forks, by enabling pipelining, profiling of tasks and by caching facts to a redis container

### facts_cache.yml
Ansible first uses setup module to gather facts about all the hosts involved and deletes them after each run which consumes time, instead
this playbook will install docker, start redis container i.e enable caching of facts to a redis container running on the controller machine
on which you are running playbook which will boost the performance by caching the facts thus reducing the time taken to gather each time a
playbook is run.

### forks_pipelining.yml
This playbook will set the number of forks equal to number of hosts. 
If the number of forks are more than number of hosts, there will be a penalty for each task since there will be multiple processes running
and it will take some time to shut them down. On the other hand if the number of forks are less than the number of hosts, then each task will 
take a lot more time since hosts configured by ansible in parallel will be less in this case.

If you can use pipelining, Ansible will reduce the amount of files transferred over the wire, making everything much more efficient. 
It is enabled automatically when yor are running RHEL > 6, Centos, Fedora.

You can also choose to enable profiling of tasks.

### collect/sosreport_facts.yml
Collects sosreport, ansible_facts from remotes on to the local machine and deletes them on remotes. This will help in finding out
performance bottlenecks.

## Requirements
You need to have these installed on your host
   - Ansible
   - python

### Run facts_cache.yml
```
$ ansible-playbook -i hosts facts_cache.yml 
```

### Run forks_pipelining.yml playbook
```
$ ansible-playbook -i hosts forks_pipelining.yml
```

### Run sosreport_facts.yml
```
$ ansible-playbook -i hosts sosreport_facts.yml
```

#### variables

SOSREPORT_PATH - Directory to save results

HOSTS_PATH - Inventory file path

#### override
You can override the variables like
```
$ ansible-playbook --extra-vars '{"HOSTS_PATH":"/tmp/hosts"}' generate.yml
```
#### Example output

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

### Enable profiling of tasks
```
$ ansible-playbook -i hosts --extra-vars '{"CONFIG_PATH":"/tmp/ansible.cfg", "SET_PROFILING":"yes" }' forks_pipelining.yml
```
### Testing
Ansible profile plugin can be used to findout the time taken by each task. You can enable it by adding this line to ansible.cfg
callback_whitelist = profile_tasks

Profiling tasks will also help in identifying which steps are slow.
