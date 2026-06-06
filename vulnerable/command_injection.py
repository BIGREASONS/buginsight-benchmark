import subprocess

def ping_host(host):
    # Vulnerable to command injection
    cmd = f"ping -c 4 {host}"
    return subprocess.check_output(cmd, shell=True)
