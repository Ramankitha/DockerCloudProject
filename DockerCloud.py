import socket
import os
from collections import Counter

Counter = Counter()


def get_my_ip_address():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr


def get_number_of_words(file):
    total_word_count = 0
    with open(file, 'r') as file:
        for line in file:
            if (line != '\n'):
                if (file.name.endswith("IF.txt")):
                    Counter.update(line.replace("Â", "").split())
                total_word_count = total_word_count + \
                    len(line.replace("Â", "").split())
    return total_word_count


text_files_word_counts = {}
path = "/home/data"
if os.path.exists(path + "/" + "result.txt"):
    os.remove(path + "/" + "result.txt")
output_string = "###########|| Text file at location: /home/data ||##########\n"
for eachFile in os.listdir(path):
    if eachFile.endswith(".txt"):
        output_string = output_string+eachFile+"\n"
        text_files_word_counts[eachFile] = get_number_of_words(
            path + "/" + eachFile)

output_string = output_string+"\n"
output_string = output_string + \
    "###########|| Read the two text files and count total number of words in each text files ||###########\n"
all_files_word_count = 0
all_files_names = ""
for eachkey in text_files_word_counts.keys():
    all_files_names = all_files_names + eachkey + ","
    all_files_word_count = all_files_word_count + \
        text_files_word_counts.get(eachkey)
    output_string = output_string + \
        "Total number of words in [" + eachkey + "] is : " + \
        str(text_files_word_counts.get(eachkey))+"\n"

output_string = output_string + "\n"
output_string = output_string + \
    "###########|| Grand Total (total number of words in both files) ||###########\n"
output_string = output_string + "total number of words in both files [" + all_files_names[0:len(
    all_files_names) - 1] + "] is: " + str(all_files_word_count)+"\n"

output_string = output_string + "\n"
output_string = output_string + \
    "###########|| Top 3 words with maximum number of counts in IF.txt ||###########\n"
output_string = output_string + str(Counter.most_common(3))+"\n"

output_string = output_string + "\n"
output_string = output_string + "###########|| IP address ||###########\n"
output_string = output_string + "Your Computer IP Address is:" + get_my_ip_address()

results_text_file = open(path + "/" + "result.txt", "w")
results_text_file.write(output_string)
results_text_file.close()
for eachline in open(path + "/" + "result.txt", "r").readlines():
    print(eachline.replace("\n", ""))
