try:
    if '1' != 1:
        raise("someError")
    else:
        print('1')
except "someError":
    print('2')