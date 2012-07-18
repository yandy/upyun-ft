# -*- coding: utf8 -*-
#!/usr/bin/env python

from upyun import UpYun,md5,md5file
import sys, os
import os.path

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="又拍云python客户端")
    parser.add_argument("-b", "--bucket", type = str, default ="", help = "又拍云桶名")
    parser.add_argument("-u", "--username", type = str, default ="", help = "操作员用户名")
    parser.add_argument("-p", "--password", type = str, default ="", help = "操作员密码")
    parser.add_argument("-r", "--recursion", action = 'store_true', default = True, help = "是否递归子目录")
    parser.add_argument("path", help = "需要上传的目录", required=True)

    args = parser.parse_args(sys.argv[1:])
    kwargs = vars(args)

    u = UpYun(kwargs["bucket"],kwargs["username"],kwargs["password"])

    path = kwargs["path"]

    if kwargs["recursion"]:
        for root, dirs, files in os.walk(path):
            for f in files:
                data = open(os.path.join(root, f), 'rb')
                u.setCotentMD5(md5file(data))
                upfp = os.path.relpath(os.path.join(root, f), path)
                a = u.writeFile(upfp, data)
                print a
            if not kwargs["recursion"]:
                del dirs[0:len(dirs)]
