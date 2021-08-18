from Dictionary import Dictionary
from Equalizer import *

dictionary = Dictionary()
long_words = []
short_words = []
with open('short_forms.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        short_words.append(row[0])
        long_words.append(row[1])


class News:
    def __init__(self, id, content, url, equalizer):
        self.id = id
        self.content = content
        self.url = url
        self.equalizer = equalizer

    # add short forms
    def short_form(self, con):
        for i in range(len(short_words)):
            if long_words[i] in con:
                if short_words[i] in dictionary.dictionary.keys():
                    dictionary.dictionary[short_words[i]].append(int(self.id))
                    dictionary.words_total_count[short_words[i]] += 1
                else:
                    dictionary.dictionary[short_words[i]] = [int(self.id)]
                    dictionary.words_total_count[short_words[i]] = 1

    def tokenize_content(self):

        # add the id and url to its dict
        dictionary.id_to_url_dict[int(self.id)] = self.url
        corrected_content = ''
        # tokens = []
        # added half space u200c\
        alphabet = 'آاأبپتثجچحخدذرزژسشصضطظعغفقکكگلم‌نوؤهیيئء'  # نیم فاصله داره
        r = re.compile(f'[{alphabet}]+')
        position = 1
        for token in r.findall(self.content):
            if '\u200c' in token:
                token = re.sub('\u200c', '', token)
            # tmp = self.equalizer.char_equalizer(token, 'q')
            token = self.equalizer.char_equalizer(token, 'q')
            corrected_content += token + ' '
            # if token in tokens:
            #     dictionary.words_total_count[token] += 1
            # else:
            # tokens.append(token)
            if token in dictionary.dictionary.keys():
                dictionary.dictionary[token].append([int(self.id), position])
                dictionary.words_total_count[token] += 1
            else:
                dictionary.dictionary[token] = [[int(self.id), position]]
                dictionary.words_total_count[token] = 1
            position+=1
        return corrected_content


# from Dictionary import Dictionary
# from Equalizer import *
#
# dictionary = Dictionary()
# long_words = []
# short_words = []
# with open('short_forms.csv', encoding='utf8') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for row in csv_reader:
#         short_words.append(row[0])
#         long_words.append(row[1])
#
#
# class News:
#     def __init__(self, id, content, url, equalizer):
#         self.id = id
#         self.content = content
#         self.url = url
#         self.equalizer = equalizer
#
#     # add short forms
#     def short_form(self, con):
#         for i in range(len(short_words)):
#             if long_words[i] in con:
#                 if short_words[i] in dictionary.dictionary.keys():
#                     dictionary.dictionary[short_words[i]].append(int(self.id))
#                     dictionary.words_total_count[short_words[i]] += 1
#                 else:
#                     dictionary.dictionary[short_words[i]] = [int(self.id)]
#                     dictionary.words_total_count[short_words[i]] = 1
#
#     def tokenize_content(self):
#
#         # add the id and url to its dict
#         dictionary.id_to_url_dict[int(self.id)] = self.url
#         corrected_content = ''
#         tokens = []
#         # added half space u200c\
#         alphabet = 'آاأبپتثجچحخدذرزژسشصضطظعغفقکكگلم‌نوؤهیيئء'  # نیم فاصله داره
#         r = re.compile(f'[{alphabet}]+')
#         for token in r.findall(self.content):
#             if '\u200c' in token:
#                 token = re.sub('\u200c', '', token)
#             # tmp = self.equalizer.char_equalizer(token, 'q')
#             token = self.equalizer.char_equalizer(token, 'q')
#             corrected_content += token + ' '
#             if token in tokens:
#                 dictionary.words_total_count[token] += 1
#             else:
#                 tokens.append(token)
#                 if token in dictionary.dictionary.keys():
#                     dictionary.dictionary[token].append(int(self.id))
#                     dictionary.words_total_count[token] += 1
#                 else:
#                     dictionary.dictionary[token] = [int(self.id)]
#                     dictionary.words_total_count[token] = 1
#         return corrected_content
