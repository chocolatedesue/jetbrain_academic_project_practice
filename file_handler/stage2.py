import os
import argparse

parser = argparse.ArgumentParser(description="Build a file structure tree")
parser.add_argument("directory", nargs='?', type=str,
                    default=None, help="Enter directory")
parsed_arguments = parser.parse_args()


def specify_additional_options():
    print("\nEnter file format: ")
    file_format = input()

    print('Size sorting options:\n1. Descending\n2. Ascending\n')

    def sorting_option():
        print("\nEnter a sorting option:")
        option = int(input())
        if option in [1, 2]:
            return option
        print("\nWrong option")
        return sorting_option()

    option = sorting_option()
    return [file_format, option]


def user_input_cheker(args):
    if args.directory is None:
        return print("Directory is not specified")

    file_format, sorting_option = specify_additional_options()

    return build_files_structure(args.directory, file_format, sorting_option)


def print_results(sorted_catalog):
    for key in sorted_catalog:
        print('\n{} bytes'.format(key))
        for v in sorted_catalog[key]:
            print(v)


def build_files_structure(directory, file_format, sorting_option):
    catalog = {}
    for root, dirs, files in os.walk(directory):
        for f in files:
            if '.{}'.format(file_format) in f:
                path = os.path.join(root, f)
                size = os.path.getsize(path)
                #处理文件大小相等时候的冲突
                if size in catalog:
                    catalog[size].append(path)
                else:
                    catalog[size] = [path]
                    #类似struct的自定义排序 以映射的方式实现绑定
    if sorting_option == 1:
        catalog = dict(sorted(catalog.items(), reverse=True))
    elif sorting_option == 2:
        catalog = dict(sorted(catalog.items()))
    print_results(catalog)


user_input_cheker(parsed_arguments)
