import subprocess as sp
import os

def run(cmd):
    os.environ['PATH'] = '/usr/local/bin:' + os.environ['PATH']
    process = sp.run(cmd, shell = True,
        stdout = sp.PIPE, stdin = sp.PIPE, stderr = sp.PIPE, 
        universal_newlines = True)
    return (process.returncode, process.stdout, process.stderr)
