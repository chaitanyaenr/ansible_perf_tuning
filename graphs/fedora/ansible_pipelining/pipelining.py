import matplotlib.pyplot as plt

number_of_hosts_pipelining_enabled = [ 2, 4, 5 ]
time_taken_pipelining_disabled = [ 21.023, 27.256, 33.394 ]
number_of_hosts_pipelining_disabled = [ 2, 4, 5 ]
time_taken_pipelining_enabled = [ 19.671, 23.123, 28.638 ]
plt.xlabel("number of hosts")
plt.ylabel("time in seconds")
plt.bar(number_of_hosts_pipelining_disabled, time_taken_pipelining_disabled, width=0.2, color='cyan', label= 'pipelining_disabled', align='center')
plt.bar(number_of_hosts_pipelining_enabled, time_taken_pipelining_enabled, width=0.2, color='red', label= 'pipelining_enabled', align='center')
plt.title("ansible-performance stats")
plt.legend()
plt.show()
