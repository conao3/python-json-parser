from . import rep


def main():
    while True:
        res = rep.rep(input('user> '))
        if res:
            print(res)
