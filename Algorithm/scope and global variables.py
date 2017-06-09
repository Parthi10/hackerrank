def en_func():
    m = 13
    def local():
        print(m)

m=5
print(m)

en_func()
en_func.local()
