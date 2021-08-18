import pickle


class Dictionary:

    def __init__(self):
        self.dictionary = dict()
        self.words_total_count = dict()
        self.id_to_url_dict = dict()

    def sort_dict(self):
        # create the sorted final dictionary
        words = sorted(self.dictionary.keys())
        final_dictionary = dict()
        for word in words:
            final_dictionary[word] = self.dictionary[word]
        self.dictionary = final_dictionary

    def save_dict(self):
        filename = 'dict'
        outfile = open(filename, 'wb')
        pickle.dump(self.dictionary, outfile)
        outfile.close()
        filename = 'dict_url'
        outfile = open(filename, 'wb')
        pickle.dump(self.id_to_url_dict, outfile)
        outfile.close()


    def read_dict(self):
        infile = open('dict', 'rb')
        s = pickle.load(infile)
        infile.close()
        infile = open('dict_url', 'rb')
        ss = pickle.load(infile)
        infile.close()
        return s, ss

    def test_dict(self, input_word):
        if input_word in self.dictionary.keys():
            print(self.dictionary[input_word])
        else:
            print("This word is not in the dictionary")

    def get_frequency_based_dict(self):
        freq_based_dict = sorted(self.words_total_count.items(), key=lambda x: x[1], reverse=True)
        # freq_based_dict = dict(freq_based_dict)
        return freq_based_dict

    def remove_k_frequent_words(self, k):
        words = self.get_frequency_based_dict()[0:k]
        for word in words:
            del self.dictionary[word[0]]
