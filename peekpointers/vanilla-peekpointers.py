import gdb
import struct

offset = 0 

BEGIN = -1
END = -1

ranges = {}

u64 = lambda v: struct.unpack("<Q", v)[0]

def get_pid():
    info_proc = gdb.execute('info proc', to_string=True)
    pid_line = info_proc.splitlines()[0]
    return int(pid_line.split(' ')[1])

def get_ranges():

    maps = []
    with open("/proc/%d/maps" % get_pid()) as f:
        maps = f.read().split("\n")

    keys = []
    for m in maps:

        k = m.split(" ")[-1]
        if k and (k[0] == '/' or k == "[heap]" or k == "[stack]"):
            if k not in keys:
                keys.append(k)
    for k in keys:

        mem = [x.split(" ")[0] for x in maps if k in x]
        BEGIN = int(mem[0].split("-")[0], 16)
        END = int(mem[-1].split("-")[1], 16)

        ranges[k] = (BEGIN, END)



def peek_pointer(v):

    for k in ranges:
        if ranges[k][0] <= v < ranges[k][1]:
            gdb.write("%s pointer found at 0x%x, value 0x%x\n" % (k, offset, v))
            del ranges[k]
            return

def peek_pointers():
    global offset
    with open("/proc/%d/mem" % get_pid(), "rb") as f:
        try:
            while True:
                # info("looking at addr 0x%x" % offset)
                f.seek(offset)
                qw = u64(f.read(8))
                
                peek_pointer(qw)
                offset += 8
        except:
            return

class Snipe(gdb.Command):
    def __init__(self):
        super(Snipe, self).__init__('peek-pointers', gdb.COMMAND_STATUS)

    def invoke(self, arguments, from_tty):
        global offset
        argv = arguments.split()
        offset = int(argv[0], 16)
        get_ranges()
        peek_pointers()

Snipe()
