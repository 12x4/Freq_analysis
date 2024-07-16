import sqlite3
from freq_analysis import freq_analysis as fa
import cezar


class _console(fa):

    def main(self):
        print("Welcome frequency analysis v 1.0.0.0")

        db = sqlite3.connect("db/data.db")

        self.console_write = ""

        self.fl_up_dec = False
        self.x = 0
        self.y = 300
        self.user_input()

        while self.console_write != "exit":
            if self.console_write == "help":
                self.help()

            elif self.console_write == "anru":
                try:
                    if self.file_encrypted_text == "":
                        self.file_encrypted_text = input("File_encrypted_txt: ")
                    self.odnogramm_txt(self.file_ru_text, self.file_analysed_ru_1gramm)
                    self.bigramm_txt(self.file_ru_text, self.file_analysed_ru_2gramm)
                    self.trigramm_txt(self.file_ru_text, self.file_analysed_ru_3gramm)
                    self.successfully()
                except Exception:
                    print("Error")

            elif self.console_write == "anen":
                try:
                    if self.file_encrypted_text == "":
                        self.file_encrypted_text = input("File_encrypted_txt: ")
                    self.odnogramm_txt(self.file_encrypted_text, self.file_analysed_encrypted_1gramm)
                    self.bigramm_txt(self.file_encrypted_text, self.file_analysed_encrypted_2gramm)
                    self.trigramm_txt(self.file_encrypted_text, self.file_analysed_encrypted_3gramm)
                    self.successfully()
                except Exception as e:
                    print(f"Error {e}")

            elif self.console_write == "decry":
                print("1 - odnogramm, 2 - bigramm, 3 - trigramm")
                self.user_input()
                text = ""
                f = True
                try:
                    if self.console_write == "1":
                        text = self.decryption_1gramm(self.read_txt(self.file_encrypted_text), up=self.fl_up_dec)
                    elif self.console_write == "2":
                        text = self.decryption_2gramm(self.read_txt(self.file_encrypted_text), up=self.fl_up_dec)
                    elif self.console_write == "3":
                        text = self.decryption_3gramm(self.read_txt(self.file_encrypted_text), up=self.fl_up_dec)
                    else:
                        print("No command")
                        f = False
                except Exception as e:
                    print(f"Error {e}")
                    f = False

                if f:
                    if self.x != -1 and self.y != -1 and text is not None:
                        print(text[self.x:self.y])
                    else:
                        print(text)

            elif self.console_write == "anws":
                self.user_input()

                try:
                    if self.console_write == "en":
                        self.anwsen(self.file_encrypted_text)
                        self.successfully()

                    elif self.console_write == "ru":
                        self.anwsru(self.file_ru_text)
                        self.successfully()

                    else:
                        print("No command")
                except Exception as e:
                    print(f"Error {e}")

            elif self.console_write == "size_out_txt":
                try:
                    self.x = int(input("index 1:"))
                    self.y = int(input("index 2:"))
                except Exception:
                    print("incorrect format")

            elif self.console_write == "up_dec":
                self.up_dec()
                
            else:
                print("No command")
            self.user_input()

    def user_input(self):
        self.console_write = input().lower()

    def successfully(self):
        print("successfully")

    def up_dec(self):
        y = input()
        if y == "1":
            self.fl_up_dec = True
        elif y == "0":
            self.fl_up_dec = False
        else:
            print("incorrect format")

    def help(self):
        print("anen - analysis encrypted text")
        print("anru - analysis ru text")
        print("decry - decryption encrypted text")
        print("anws - analysis words")
        print("size_out_txt - from which to which index should I output")
        print("up_dec - improve decoding using word analysis 1/0")
        print("exit")

    def defolt_setings(self):
        pass

#a = fa()
#a.write_txt(cezar.pleyfer(a.read_txt(".txt/war_and_peace_tom_2.txt")), ".txt/encrypted_tom_2.txt")

if __name__ == "__main__":
    #a = fa()
    #a.write_txt(cezar.cezar(a.read_txt(".txt/anna_karenina.txt"), 4), ".txt/encrypted_tom_2.txt")

    boom = _console()
    boom.main()
