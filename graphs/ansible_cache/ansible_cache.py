import matplotlib.pyplot as plt

number_of_hosts_cache_disabled = [ 1, 3 ]
time_taken_cache_disabled = [ 3.09, 5.45  ]
number_of_hosts_cache_enabled = [ 1, 3 ]
time_taken_cache_enabled = [ 0.45, 1.23 ]
plt.xlabel("number of hosts")
plt.ylabel("time in seconds")
plt.bar(number_of_hosts_cache_disabled, time_taken_cache_disabled, width=0.2, color='cyan', label= 'no_cache', align='center')
plt.bar(number_of_hosts_cache_enabled, time_taken_cache_enabled, width=0.2, color='red', label= 'cache', align='center')
plt.legend()
plt.show()
