#1.2
print("*" * 20)
print('*' + 'Welcome' .center(18) + '*')
print('*' * 20)

word = 'CAT'
print(f"{word[0]}: index 0, index -3")
print(f"{word[1]}: index 1, index -2")
print(f"{word[2]}: index 2, index -1")
#2.1

text = "Computer Science"
print(text[:8])      # "Computer"
print(text[-7:])     # "Science"
print(text[3:6])     # "put"

#2.2
# Extract first 4 characters

date = 20260126  # "20240615"
year = date[:4]
month = date[5:7]
day = date[-2:]

#reverse text
text1 = "Python"
reversed1 = text1[::-1]
print(reversed1)  # "nohtyP"

text2 = "programming"
every_other = text2[::2]
print(every_other)  # "pormig"
#last 3 characters of Hello World reversed



#2.3