from freq import get_freq

freq_file = 'src/data/internet-jp-forms.num'
freq_dict = get_freq(freq_file)

def print_rimedict_with_freq(text, code):
    if (text in freq_dict):
        print(text, code, freq_dict[text], sep = '\t')
    else:
        print(text, code, sep = '\t')
