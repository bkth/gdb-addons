# gdb-addons
Repo for custom gdb commands

# Peek-pointers
Given an address it will check pointers present starting at the address and spit out pointers for shared objects

```
peek-pointers address <object_name> <all>
```

Example `cat -`

```
gef➤  peek-pointers 0x55555575c000
cat pointer at 0x55555575c008, value 0x55555575c008
[stack] pointer at 0x55555575c0c0, value 0x7fffffffe498
libc-2.24.so pointer at 0x55555575c0c8, value 0x7ffff7dd2600 <_IO_2_1_stdout_>
[heap] pointer at 0x55555575d038, value 0x55555575d010
locale-archive pointer at 0x55555575d0b8, value 0x7ffff774e5c0
Could not read from address 0x55555577e000, stopping.
gef➤  peek-pointers 0x55555575c000 libc-2.24.so
libc-2.24.so pointer at 0x55555575c0c8, value 0x7ffff7dd2600 <_IO_2_1_stdout_>
gef➤  peek-pointers 0x55555575c000 libc-2.24.so all
libc-2.24.so pointer at 0x55555575c0c8, value 0x7ffff7dd2600 <_IO_2_1_stdout_>
libc-2.24.so pointer at 0x55555575c0e0, value 0x7ffff7dd2520 <_IO_2_1_stderr_>
libc-2.24.so pointer at 0x55555575dfe8, value 0x7ffff7ba1b40 <_nl_default_dirname>
Could not read from address 0x55555577e000, stopping.
```
