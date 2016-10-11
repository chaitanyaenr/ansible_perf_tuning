import sys

with open(sys.argv[1], 'r') as my_file: 
    lines=my_file.readlines()
for line in lines:
        line = line.rstrip()
        # Grab forks parameter from ansible.cfg
        if line.startswith('#forks'):
                print "Looks like you are not using fork feature, If the number of forks are more than number of hosts, there will be a penalty for each task since there will be multiple processes running and it will take some time to shut them down. On the other hand if the number of forks are less than the number of hosts, then each task will take a lot more time since hosts configured by ansible in parallel will be less inthis case" 
        # Grab pipelining parameter from ansible.cfg
        if line.startswith('#pipelining'):
 		print "Looks like you are not using pipelining, If you can use pipelining, Ansible will reduce the amount of files transferred over the wire, making everything much more efficient. Enabling pipelining reduces the number of SSH operations required to execute a module on the remote server"
        
