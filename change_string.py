# Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    new_string = "".join(l)
    print new_string

string = raw_input()
pos,char = raw_input().split()

print string
print pos, char

mutate_string(string, int(pos), char)