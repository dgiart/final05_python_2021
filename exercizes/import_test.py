from modules.module_test import A
import sys

def main():
    aa = A()
    aa.a()
    for el in sys.path:
        print(el)

if __name__ == '__main__':
    main()
