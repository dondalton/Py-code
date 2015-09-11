from __future__ import print_function
import sys
message = []
rec = 0

while 1:
    line = sys.stdin.readline()
    if not line:
        break

    if "Internet Protocol Version 4," in line:
        src=line.split("Src: ")[1].split(" ")[0]
        dst=line.split("Dst: ")[1].split(" ")[0]

    if line.strip():
        if rec == 1:
            message.append(line)
        if "Message Type:" in line:
            rect = 1



    if not line.strip() or "Stream Control Transmission Protocol" in line :
        print('insert into messages (date, src, dst, message) values (current_date, "' + src + '", "' + dst + '","', end="")
        for mes in message:
            print(mes, end="")
        print('");\n',end="")
        del message[:]