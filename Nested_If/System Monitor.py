import random
cpu_usage = random.randint(0, 100)

if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage is not 90:
    pass
elif cpu_usage > 40 and cpu_usage < 80:
    print("Moderate CPU usage")
else:
    print("Low-cpu")
    