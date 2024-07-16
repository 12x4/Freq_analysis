import codecs
import sqlite3


class freq_analysis():
    def __init__(self):
        self.direct = ".txt/"

        self.defolt_settings_file = f"{self.direct}defolt.txt"

        self.file_ru_text = f"{self.direct}war_and_peace_tom_1.txt"
        self.file_encrypted_text = f"{self.direct}encrypted_tom_2.txt"

        self.file_analysed_ru_1gramm = f"{self.direct}anRu1.txt"
        self.file_analysed_ru_2gramm = f"{self.direct}anRu2.txt"
        self.file_analysed_ru_3gramm = f"{self.direct}anRu3.txt"

        self.file_analysed_encrypted_1gramm = f"{self.direct}anEn1.txt"
        self.file_analysed_encrypted_2gramm = f"{self.direct}anEn2.txt"
        self.file_analysed_encrypted_3gramm = f"{self.direct}anEn3.txt"

        self.file_db_words = f"db/db.db"

        self.ru_locate = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def odnogramm_txt(self, input_txt, output_txt):
        out_file = codecs.open(output_txt, "w+", "utf-8")

        s = self.read_txt(input_txt)
        len_s = len(s)

        mass = dict()
        symbol_count = 0

        for i in self.ru_locate:
            mass[i] = 0

        for i in range(len_s):
            if s[i] in self.ru_locate:
                mass[s[i]] += 1
                symbol_count += 1

        mass = sorted(mass.items(), key=lambda x: x[1], reverse=True)
        mass = dict([(v, k) for v, k in mass])

        for i in mass:
            out_file.write(f"{i}-{mass[i] / symbol_count * 100}\n")

        print(f"symbol_count {symbol_count}")

        out_file.close()
        return

    def bigramm_txt(self, input_txt, output_txt):
        text = self.read_txt(input_txt)
        text.lower()
        len_text = len(text)
        symbol_count = 0

        mass = dict()

        for i in self.ru_locate:
            for g in self.ru_locate:
                mass[i + g] = 0

        for i in range(len_text - 1):
            if text[i] in self.ru_locate and text[i + 1] in self.ru_locate:
                mass[text[i] + text[i + 1]] += 1
                symbol_count += 1

        mass = sorted(mass.items(), key=lambda x: x[1], reverse=True)
        mass = dict([(v, k) for v, k in mass])

        out_file = codecs.open(output_txt, "w+", "utf-8")

        for i in mass:
            out_file.write(f"{i}-{mass[i] / symbol_count * 100}\n")

        print(f"symbol_count {symbol_count}")

        out_file.close()
        return

    def trigramm_txt(self, input_txt, output_txt):
        text = self.read_txt(input_txt)
        text.lower()
        len_text = len(text)
        symbol_count = 0

        mass = dict()

        for i in self.ru_locate:
            for g in self.ru_locate:
                for h in self.ru_locate:
                    mass[i + g + h] = 0

        for i in range(len_text - 2):
            if text[i] in self.ru_locate and text[i + 1] in self.ru_locate and text[i + 2] in self.ru_locate:
                mass[text[i] + text[i + 1] + text[i + 2]] += 1
                symbol_count += 1

        mass = sorted(mass.items(), key=lambda x: x[1], reverse=True)
        mass = dict([(v, k) for v, k in mass])

        out_file = codecs.open(output_txt, "w+", "utf-8")

        for i in mass:
            out_file.write(f"{i}-{mass[i] / symbol_count * 100}\n")

        print(f"symbol_count {symbol_count}")

        out_file.close()
        return

    def anwsru(self, input_txt):

        text_ = self.read_txt(input_txt)

        db = sqlite3.connect(self.file_db_words)
        data = dict()
        text = ""
        for i in text_:
            if i not in self.ru_locate:
                text += " "
            else:
                text += i

        text = text.split()
        words_count = len(text)

        for i in text:
            if i in data and i != "" and i != " ":
                data[i] += 1
            else:
                data[i] = 1

        data = sorted(data.items(), key=lambda x: x[1], reverse=True)
        data = dict([(v, (k / words_count) * 100) for v, k in data])

        c = db.cursor()
        c.execute("""DELETE FROM ru_words""")

        for i in data:
            c.execute(f"""INSERT INTO ru_words VALUES(?, ?)""", (i, data[i]))

        db.commit()
        db.close()

    def anwsen(self, input_txt):

        text_ = self.read_txt(input_txt)

        db = sqlite3.connect(self.file_db_words)
        data = dict()
        text = ""
        for i in text_:
            if i not in self.ru_locate:
                text += " "
            else:
                text += i

        text = text.split()
        words_count = len(text)

        for i in text:
            if i in data and i != "" and i != " ":
                data[i] += 1
            else:
                data[i] = 1

        data = sorted(data.items(), key=lambda x: x[1], reverse=True)
        data = dict([(v, (k / words_count) * 100) for v, k in data])

        c = db.cursor()
        c.execute("""DELETE FROM en_words""")

        for i in data:
            c.execute(f"""INSERT INTO en_words VALUES(?, ?)""", (i, data[i]))

        db.commit()
        db.close()

    def decryption_1gramm(self, encrypted_txt, e=0.0001, up=False):
        info_code_file = codecs.open(self.file_analysed_encrypted_1gramm, "r", "utf-8")
        info_ru_file = codecs.open(self.file_analysed_ru_1gramm, "r", "utf-8")
        data_code = dict()
        data_ru = dict()

        for i in info_ru_file.readlines():
            a, b = i[:1], i[2:]
            data_ru[a] = float(b)

        for i in info_code_file.readlines():
            a, b = i[:1], i[2:]
            data_code[a] = float(b)

        result = dict()
        h1 = list(data_ru.items())
        h2 = list(data_code.items())

        for i in range(33):
            result[h2[i][0]] = h1[i][0]

        decrypting = ""

        for i in encrypted_txt.lower():

            if i in self.ru_locate:
                decrypting += result[i]
            else:
                decrypting += i


        info_code_file.close()
        info_ru_file.close()

        if up:
            decrypting = self.replacement(decrypting, self.up_decrypt(decrypting))

        return decrypting

    def decryption_2gramm(self, encrypted_txt, e=0.001, up=False):
        info_code_file = codecs.open(self.file_analysed_encrypted_2gramm, "r", "utf-8")
        info_ru_file = codecs.open(self.file_analysed_ru_2gramm, "r", "utf-8")
        data_code = dict()
        data_ru = dict()

        for i in info_ru_file.readlines():
            a, b = i[:2], i[3:]
            data_ru[a] = float(b)

        for i in info_code_file.readlines():
            a, b = i[:2], i[3:]
            data_code[a] = float(b)

        result = dict()
        h1 = list(data_ru.items())
        h2 = list(data_code.items())

        for i in range(33 * 33):
            result[h2[i][0]] = h1[i][0]

        decrypting = ""

        len_encrypted = len(encrypted_txt)
        encrypted_txt = encrypted_txt.lower()
        i = 0
        while i < len_encrypted - 1:
            if encrypted_txt[i] in self.ru_locate and encrypted_txt[i + 1] in self.ru_locate:
                decrypting += result[encrypted_txt[i] + encrypted_txt[i + 1]]
                i += 1
            else:
                decrypting += encrypted_txt[i]

            i += 1

        info_code_file.close()
        info_ru_file.close()

        if up:
            decrypting = self.replacement(decrypting, self.up_decrypt(decrypting))

        return decrypting

    def decryption_3gramm(self, encrypted_txt, e=0.001, up=False):
        info_code_file = codecs.open(self.file_analysed_encrypted_3gramm, "r", "utf-8")
        info_ru_file = codecs.open(self.file_analysed_ru_3gramm, "r", "utf-8")
        data_code = dict()
        data_ru = dict()

        for i in info_ru_file.readlines():
            a, b = i[:3], i[4:]
            data_ru[a] = float(b)

        for i in info_code_file.readlines():
            a, b = i[:3], i[4:]
            data_code[a] = float(b)

        result = dict()
        h1 = list(data_ru.items())
        h2 = list(data_code.items())

        for i in range(33 * 33 * 33):
            result[h2[i][0]] = h1[i][0]

        decrypting = ""

        len_encrypted = len(encrypted_txt)
        encrypted_txt = encrypted_txt.lower()
        i = 0
        while i < len_encrypted - 2:
            if encrypted_txt[i] in self.ru_locate and encrypted_txt[i + 1] in self.ru_locate and\
                    encrypted_txt[i + 2] in self.ru_locate:
                decrypting += result[encrypted_txt[i] + encrypted_txt[i + 1] + encrypted_txt[i + 2]]
                i += 2
            else:
                decrypting += encrypted_txt[i]

            i += 1

        info_code_file.close()
        info_ru_file.close()

        if up:
            decrypting = self.replacement(decrypting, self.up_decrypt(decrypting))

        return decrypting

    def up_decrypt(self, text, e=0.2):
        db = sqlite3.connect(self.file_db_words)

        c = db.cursor()

        ru_words = c.execute("SELECT * FROM ru_words").fetchall()
        en_words = c.execute("SELECT * FROM en_words").fetchall()

        en_words = dict([(v, k) for v, k in en_words])

        len_ru_words = len(ru_words)
        len_en_words = len(en_words)

        _text = ""

        for i in text:

            if i in self.ru_locate:
                _text += i
            else:
                _text += " "

        text = _text.split()
        words = set()

        for i in text:
            words.add(i)

        replacement = dict()
        for i in words:
            if i not in en_words:
                continue
            nn = en_words[i]
            bb = []

            for g in ru_words:
                if abs(g[1] - nn) <= e and len(g[0]) == len(i):
                    bb.append(g[0])

            if len(bb) < 3:
                replacement[i] = bb[0]

        print(replacement)
        return replacement

    def replacement(self, text, data):

        boom = ""
        i = 0
        if len(data) == 0:
            return text

        while i < len(text):
            word = ""
            if text[i] not in self.ru_locate:
                boom += text[i]
                i += 1
            else:

                while True:

                    if i < len(text) and text[i] in self.ru_locate:
                        word += text[i]
                        i += 1
                    else:
                        if word in data:
                            boom += data[word]
                        else:
                            boom += word
                        break

        return boom

    def write_txt(self, txt, out_file):
        file = codecs.open(out_file, "w+", "utf-8")
        file.write(txt)
        file.close()

    def read_txt(self, in_file):

        try:
            file = codecs.open(in_file, "r", "utf-8")
            text = file.read()
            file.close()
        except Exception as e:
            file = codecs.open(in_file, "r")
            text = file.read()
            file.close()

        return text
