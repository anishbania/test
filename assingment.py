sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
ax=sentence.split()
num_a_or_e=0
for x in ax:
    if ('a'in x) or ('e' in x):
        num_a_or_e=num_a_or_e+1
print(num_a_or_e)
