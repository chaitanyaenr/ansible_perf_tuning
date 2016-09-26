# ansible_perf_tuning
Tunes the performance of ansible by changing the number of forks. 

This playbook will set the number of forks equal to number of hosts. 
If the number of forks are more than number of hosts, there will be a penalty for each task since there will be multiple process running
and it will take some time to shut them down. On the other hand if the number of forks are less than the number of hosts, then each task will 
take a lot more time since hosts configured by ansible in parallel will be less in this case.

## Requirements
You need to have these installed on your host
   - Ansible
   - python

### Run
$ ansible-playbook -i hosts forks.yml

### Testing
Ansible profile plugin can be used to findout the time taken by each task. You can enable it by adding this line to ansible.cfg
callback_whitelist = profile_tasks

Profiling tasks will also help in identifying which steps are slow.
