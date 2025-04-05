import matplotlib.pyplot as plt

text = open("log.txt", "r")
line_list = text.readlines()
char_count = {

}

for line in line_list: # Goes throug each line in text file
    for ch in line: # Goes through each character in text file
        if ch != ' ':
            if ch not in char_count:
                char_count[ch] = 1
            else:
                char_count[ch] += 1

y = list(char_count.keys())
x = list(char_count.values())

plt.bar(y, x, color = 'g')
plt.xlabel("Character", fontsize = 12)
plt.ylabel("Number of times", fontsize = 12)

plt.title("Keylogger count", fontsize = 30)
plt.legend()
plt.show()
