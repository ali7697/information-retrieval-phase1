from Equalizer import *


class Retriever:
    query: str

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.equalizer = Equalizer(self.dictionary)

    def get_dict(self):
        self.dictionary.dictionary, self.dictionary.id_to_url_dict = self.dictionary.read_dict()

    def get_query(self):
        self.query = input('Please enter the query: ')

    def get_equalized_query(self):
        alphabet = 'آاأبپتثجچحخدذرزژسشصضطظعغفقکكگلم‌نوؤهیيئء' # نیم فاصله داره
        r = re.compile(f'[{alphabet}]+')
        words = r.findall(self.query)
        words = self.equalizer.equalize_query(words)
        return words

    def retrieve(self):
        # id -> num of reps
        keys = self.dictionary.dictionary.keys()
        output = dict()
        lists = []
        words = self.get_equalized_query()
        for word in words:
            if word in keys:
                lists.append(self.dictionary.dictionary[word])
        sum_lists = []
        for lis in lists:
            sum_lists += lis
        sum_lists = sorted(sum_lists)
        for news_id in sum_lists:
            if news_id in output.keys():
                # counting the repetitions of each word
                output[news_id] += 1
            else:
                output[news_id] = 1
        output = sorted(output.items(), key=lambda x: x[1], reverse=True)
        output = dict(output)
        # id -> url
        output_printed = dict()
        print('Num of docs: ' + str(len(output.keys())))
        for news_id in output:
            output_printed[news_id] = self.dictionary.id_to_url_dict[news_id]
            print(str(news_id)+'\t'+output_printed[news_id])
        return output_printed
