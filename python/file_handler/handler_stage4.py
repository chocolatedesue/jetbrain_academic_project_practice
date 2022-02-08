import os
import sys
import hashlib


def get_opt():
    ans = int(input("Enter a sorting option:"))
    if (ans == 1 or ans == 2):
        return ans
    else:
        print("\nWrong option")
        return get_opt()


def print_results(sorted_catalog):
    for key in sorted_catalog:
        print('\n{} bytes'.format(key))
        for v in sorted_catalog[key]:
            print(v)


def request():
    res = input()
    if (res == "yes" or res == "no"):
        return res
    else:
        print("\nWrong option")
        return request()

def delete(my_dic,size:dict):
    ans=request()
    if (ans!="no"):
        def get_num():
            ans="".join(input().split())
            if ans.isdigit():
                for i in ans:
                    if int(i) > len(my_dic):
                        print("Wrong format")
                        return get_num()
                return ans
            else :
                print ("Wrong format")
                return get_num()
        res=get_num()
        sum=0
        for i in res:
            sum+=size[i]
            os.remove(my_dic[i])
        print ("Total freed up space: %d bytes"%(sum))



def hash_handle(my_dic: dict):
    res = request()
    if (res != "no"):
        idx = 1
        inf={}
        size={}
        for key in my_dic:
            record = {}
            result = {}
            for i in my_dic[key]:
                with open(i, "rb") as f:
                    obj = hashlib.md5()
                    content = f.read()
                    obj.update(content)
                    res = obj.hexdigest()
                    if res in record:
                        record[res].append(i)
                        result[res]=record[res]
                    else:
                        record[res] = [i]
            if result:
                print("\n%d bytes" % key)

                for i in result:
                    print("Hash: %s" % (i))

                    for j in result[i]:
                        print(str(idx)+".",j)
                        inf[str(idx)]=j
                        size[str(idx)]=key
                        idx+=1
        delete(inf,size)

def search(Format: str, Opt: int):
    dic = {}
    global paths
    for root, dirs, files in os.walk(paths, topdown=True):
        for f in files:
            if ".{}".format(Format) in f:
                path = os.path.join(root, f)
                size = os.path.getsize(path)
                # if type(path)==bool:
                #     continue
                if size in dic:
                    dic[size].append(path)
                else:
                    dic[size] = [path]
    if Opt == 1:
        my_dic = dict(sorted(dic.items(), reverse=True))
    elif Opt == 2:
        my_dic = dict(sorted(dic.items(), reverse=False))
    print_results(my_dic)
    print("\nCheck for duplicates?")
    hash_handle(my_dic)


try:
    paths = sys.argv[1]
    print("\nEnter file format:")
    Format = input()
    print('''Size sorting options:
    1. Descending
    2. Ascending''')

except IndexError:
    print("Directory is not specified")
    sys.exit(0)

Opt = get_opt()
search(Format, Opt)



