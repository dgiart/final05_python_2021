from math import pi
print('Hi from MODULE')
import flask

def foo(text = 'foo'):
    print(f'Hi from {text}')

class A:
    def a(self):
        print('hi from class')
p = pi

def main():
    print('hi from main() func')

if __name__ == '__main__':
    print('hi from if...')
    main()

print(flask)
foo()
print('END')