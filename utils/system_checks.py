import psutil


def check_memory_usage() -> str:
    """Check if the system memory usage is below a certain threshold."""
    memory = psutil.virtual_memory()
    threshold = 80  # Set threshold to 80%

    if memory.percent < threshold:
        return "HIGH MEMORY USAGE"
    else:
        return "OK"


def check_cpu_usage() -> str:
    """Check if the system CPU usage is below a certain threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    threshold = 90  # Set threshold to 90%

    if cpu_usage < threshold:
        return "HIGH CPU USAGE"
    else:
        return "OK"


def check_disk_usage() -> str:
    """Check if the system disk usage is below a certain threshold."""
    disk = psutil.disk_usage('/')
    threshold = 90  # Set threshold to 90%

    if disk.percent < threshold:
        return "HIGH DISK USAGE"
    else:
        return "OK"


def check_system_health() -> dict:
    """Check the overall system health by checking memory, CPU, and disk usage."""
    health_status = {
        "memory": check_memory_usage(),
        "cpu": check_cpu_usage(),
        "disk": check_disk_usage()
    }
    return health_status
