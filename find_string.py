# the user enters a string and a substring.
# You have to print the number of times that the substring
# occurs in the given string. String traversal will take
# from left to right, not from right to left.

def count_substring(string, sub_string):
    sub_len=len(sub_string)
    count = 0
    for i in range(len(string)):
        if string[i:i+sub_len]==sub_string:
            count += 1
    print count


string = raw_input()
sub_string = raw_input()

count_substring(string, sub_string)