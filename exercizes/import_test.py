from module_test import p
from module_test import A
from module_test import foo
import module_test

if __name__ == '__main__':
    print(f'pi = {p}')
    a = A()
    a.a()
    from module_test import A
    foo()
