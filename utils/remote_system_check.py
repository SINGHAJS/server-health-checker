import winrm
import json


def check_remote_system_health(host, username, password):
    session = winrm.Session(host, auth=(username, password))

    ps_script = r"""
    $os = Get-WmiObject Win32_OperatingSystem
    $freeMem = $os.FreePhysicalMemory
    $totalMem = $os.TotalVisibleMemorySize
    $memUsage = [math]::Round((($totalMem - $freeMem) / $totalMem) * 100, 2)

    $cpuLoad = Get-WmiObject Win32_Processor | Measure-Object -Property LoadPercentage -Average | Select-Object -ExpandProperty Average

    $disk = Get-PSDrive C
    $diskUsage = [math]::Round(($disk.Used / ($disk.Used + $disk.Free)) * 100, 2)

    $uptime = (Get-Date) - (gcim Win32_OperatingSystem).LastBootUpTime
    $uptimeDays = [math]::Floor($uptime.TotalDays)
    $uptimeHours = $uptime.Hours
    $uptimeMinutes = $uptime.Minutes

    $result = @{
        memoryPercent = $memUsage
        cpuPercent = $cpuLoad
        diskPercent = $diskUsage
        uptime = "{0} days, {1} hours, {2} minutes" -f $uptimeDays, $uptimeHours, $uptimeMinutes
    }
    $result | ConvertTo-Json
    """

    try:
        result = session.run_ps(ps_script)
        if result.status_code != 0:
            raise Exception(
                f"PowerShell error: {result.std_err.decode().strip()}")

        data = json.loads(result.std_out.decode())

        memory_status = "OK" if data["memoryPercent"] <= 80 else "HIGH MEMORY USAGE"
        cpu_status = "OK" if data["cpuPercent"] <= 90 else "HIGH CPU USAGE"
        disk_status = "OK" if data["diskPercent"] <= 90 else "HIGH DISK USAGE"

        output = f"""
        Server: {host}
        -------------------------
        Memory Usage : {data['memoryPercent']}% [{memory_status}]
        CPU Load     : {data['cpuPercent']}% [{cpu_status}]
        Disk Usage   : {data['diskPercent']}% [{disk_status}]
        Uptime       : {data['uptime']}
        """

        return output

    except Exception as e:
        return f"\nServer: {host}\nError: {e}\n"
