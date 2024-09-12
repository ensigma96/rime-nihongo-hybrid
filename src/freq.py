def get_freq(filename):
    freq_dict = {}
    with open(filename, 'r') as f:
        for i in range(4):
            next(f)
        for line in f:
            data = line.split(' ')
            temp_word = data[2].strip('\n')
            temp_freq = str(int(float(data[1]) * 100))
            freq_dict.update({temp_word: temp_freq})
    return freq_dict
