'''
Created on 2015/10/14

@author: shuichiro.imai
'''

if __name__ == '__main__':
    f = open('todo.txt')
    todo_str = f.read()
    print(todo_str)
    f.close()
    w = open('todo.txt','a')
    w.write('hello')
    w.write('world\n')
    w.close()