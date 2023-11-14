DATA = 'data/samplecode.txt'

def get_code ():
    print('INFO:  Running code.')
    with open(DATA) as fin:
        contents = fin.read()
    # print(contents)
    return contents

def main():
    get_code()

if __name__ == "__main__":
    main()