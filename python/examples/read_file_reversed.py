In [185]: def plop(file):
     ...:     with open(file) as f:
     ...:         f.seek(0, os.SEEK_END)
     ...:         line = ""
     ...:         while f.tell() > 0:
     ...:             f.seek(-1, os.SEEK_CUR)
     ...:             c = f.read(1)
     ...:             f.seek(-1, os.SEEK_CUR)
     ...:             if c == "\n":
     ...:                 yield line + "\n"
     ...:                 line = ""
     ...:             else:
     ...:                 line += c
     ...:         yield line + "\n"
     ...:         
     ...:                 

In [186]: optimized  = [i for i in plop("ceph_cmd")]

In [187]: full = ["".join(reversed(line))[1:] + "\n" for line in reversed(open("ceph_cmd").readlines())]
