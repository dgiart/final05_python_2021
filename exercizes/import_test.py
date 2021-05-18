from modules.module_test import p
from modules.module_test import A
from modules.module_test import foo

if __name__ == '__main__':
    print(f'pi = {p}')
    a = A()
    a.a()
    from exercizes.modules.module_test import A
    foo()
