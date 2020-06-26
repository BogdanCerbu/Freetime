# import sys


def main():
    x = input('%d. What is yout newn idea? \r\n' % (1))
    f = open('ideabank.txt', 'a+')
    f.write('\n'+x)

    f.close()

if __name__ == '__main__':
    main()