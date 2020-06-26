# import sys


def main():
    x = input('What is yout newn idea: ')

    # f = open("ideabank.txt", "w+")
    # for i in range(3):
    #     f.write("This is line %d\n\r" % (i+1))

    f = open('ideabank.txt', 'a+')
    i = 1
    f.write(x)
    i += 1

    f.close()

if __name__ == '__main__':
    main()