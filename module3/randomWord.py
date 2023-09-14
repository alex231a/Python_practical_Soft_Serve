import random

def randomWord(word_list):
    if not word_list:
        yield None
        return

    while True:
        try:
            random.shuffle(word_list)
            i = 0
            for i in range(len(word_list)):
                yield word_list[i]
                if i == (len(word_list)-1):
                    i = 0
        except StopIteration:
            yield None


words = [3, 4, 7]
rand = randomWord([3, 2, 90])
list1 = []
list2 = []
for i in range(len(words)):
    list1.append(next(rand))
for i in range(len(words)):
    list2.append(next(rand))
print(list1)
print(list2)
print(list1 != list2)