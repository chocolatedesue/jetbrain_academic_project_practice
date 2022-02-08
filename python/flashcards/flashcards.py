import os
import sys
import random
import io
import argparse

parse=argparse.ArgumentParser(description='This is helpful to study')
parse.add_argument("--import_from",default=None)
parse.add_argument("--export_to",default=None)
Args=parse.parse_args()


mem_buffer = io.StringIO()


def print_and_log(string: str):
    mem_buffer.write(string + '\n')
    print(string)


def input_and_log():
    ans = input()
    mem_buffer.write(ans)
    return ans


class flashcards:
    def __init__(self):
        self.num = 0
        self.dic = {}
        self.re_dic = {}
        self.wrong_dic = {}
        self.opt_chart={"add":"self.add_one()","remove":"self.remove()","import":"self.Import()","export":"self.Export()","ask":"self.ask()","exit":"self.exit()",
                        "log":"self.make_log()","hardest card":"self.find_hardcard()","reset stats":"self.re_set()"}

    def begin(self):
            if Args.import_from:
                self.INIT_import(Args.import_from)



            while True:
                print_and_log(
                    'Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
                Opt = input_and_log()
                eval(self.opt_chart[Opt])

    def INIT_import(self,file:str):
        with open(file, "r") as f:
            cnt = 0
            for item in f.readlines():
                cnt += 1
                item = list(item.split())
                self.dic[item[0]] = item[1]
                self.re_dic[item[1]] = item[0]
        print_and_log(f'{cnt} cards have been loaded.')


    def add_one(self):
        print_and_log("The card:")
        card = input_and_log()
        while card in self.dic:
            print_and_log(f'The card "{card}" already exists. Try again:')
            card = input_and_log()
        print_and_log("The definition of the card:")
        define = input_and_log()
        while define in self.re_dic:
            print_and_log(
                f'The definition "{define}" already exists. Try again:')
            define = input_and_log()
        combination = (f"{card}", f"{define}")
        self.dic[card] = define
        self.re_dic[define] = card
        print_and_log(f'The pair {combination} has been added.')

    def remove(self):
        print_and_log("Which card?")
        res = input()
        if res not in list(self.dic.keys()):
            print_and_log(f'Can\'t remove "{res}": there is no such card.')
        else:
            define = self.dic[res]
            self.dic.pop(res)
            self.re_dic.pop(define)
            print_and_log("The card has been removed.")

    def ask(self):
        print_and_log("How many times to ask?")
        times = int(input_and_log())
        keys = list(self.dic.keys())
        for i in range(times):
            question = random.choice(keys)
            print_and_log(f'Print the definition of "{question}":')
            ans = input_and_log()
            if (ans == self.dic[question]):
                print_and_log("Correct!")
            elif ans in self.re_dic:
                self.update(question)
                print_and_log(
                    f'Wrong. The right answer is "f{self.dic[question]}", but your definition is correct for \"{self.re_dic[ans]}\".')
            else:
                self.update(question)
                print_and_log(f"Wrong. The right answer is \"{self.dic[question]}\".")

    def update(self, question):
        if question not in self.wrong_dic:
            self.wrong_dic[question] = 1
        else:
            self.wrong_dic[question] += 1

    def re_set(self):
        self.wrong_dic.clear()
        print_and_log('Card statistics have been reset.')

    def find_hardcard(self):
        Max = 0;
        name = {}
        if not self.wrong_dic:
            print_and_log('There are no cards with errors.')
        else:
            for i in self.wrong_dic:
                if self.wrong_dic[i] > Max:
                    Max = self.wrong_dic[i]
                    name.clear()
                    name[i] = Max
                elif self.wrong_dic[i] == Max:
                    name[i] = Max
            if (len(name) == 1):
                for key in name:
                    print_and_log(f'The hardest card is "{key}". You have {name[key]} errors answering it.')
            else:
                _key = list(name.keys())
                num = _key[0]
                print_and_log(
                    f'The hardest cards are{",".join(_key)}. You have {self.wrong_dic[num]} errors answering them.')

    def make_log(self):
        target = input("File name:\n")
        with open(target, 'w') as f:
            for i in mem_buffer.getvalue():
                f.write(i)

        print_and_log('The log has been saved.')

    def Final_save(self,file_name):
        with open(file_name, 'w') as f:
            for keys, val in self.dic.items():
                f.writelines([keys, " ", val, "\n"])
        print_and_log(f'{len(self.dic)} cards have been saved.')

    def exit(self):
        print_and_log ('Bye bye!')
        if (Args.export_to):
            self.Final_save(Args.export_to)
        sys.exit(0)


    def Export(self):
        print_and_log("File Name:\n")
        file_name=input_and_log()
        with open(file_name, 'w') as f:
            for keys, val in self.dic.items():
                f.writelines([keys, " ", val, "\n"])
        print_and_log(f'{len(self.dic)} cards have been saved.')

    def Import(self):
        print_and_log("File name:")
        file = input_and_log()
        if os.path.isfile(file):
            with open(file, "r") as f:
                cnt = 0
                for item in f.readlines():
                    cnt += 1
                    item = list(item.split())
                    self.dic[item[0]] = item[1]
                    self.re_dic[item[1]] = item[0]
            print_and_log(f'{cnt} cards have been loaded.')
        else:
            print_and_log('File not found.')

begin = flashcards()
begin.begin()
mem_buffer.close()
