def result_add(index):
    with open('index.txt', 'r') as f:
        result = f.readlines()
        result = int(result[index]) + 1
        f.write(str(result))


result_add(1)
