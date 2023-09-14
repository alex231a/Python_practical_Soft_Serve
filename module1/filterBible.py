def filterBible(scripture, book, chapter):
    output_list = []
    for i in scripture:
        if i[:2] == book and i[2:5] == chapter:
            output_list.append(i)
    return output_list


scripture = ["01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002", "02001003"]
print(filterBible(scripture, "01", "001"))
