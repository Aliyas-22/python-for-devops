#checking cpu threshold
def check_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU Threshold: ")) 
    disk_threshold = int(input("Enter the Disk threshold : "))
    memory_threshold = int(input("Enter the Memory threshold : "))


    current_cpu = psutil.cpu_percent(interval=1) 
    current_disk = psutil.disk_usage('/').percent
    current_memory = psutil.virtual_memory().percent
    
    print("Current CPU %: ",current_cpu)
    print("current disk usuage %: ", current_disk)
    print("current memory %:",current_memory)
    if current_cpu > cpu_threshold:  
        print("CPU Alert Email sent...")

    else:
        print("CPU in Safe state...")
    if current_disk > disk_threshold:
        print("disk Alert email sent!")
    else:
        print("disk is in safe")

    if current_memory > memory_threshold:
        print("memory Alert email sent!")
    else:
        print("your memory is in safe")


check_cpu_threshold()
