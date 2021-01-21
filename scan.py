
import subprocess
import os
with open(os.devnull, "wb") as limbo:
        for n in range(100, 120):
                ip="192.168.0.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print (ip, "inactive")
                else:
                        print (ip, "active")