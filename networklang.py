import networkyacc

if __name__ == '__main__':
    while(True):
        try:
            s = input('NetworkLang> ')
            if s == "quit":
                break
        except EOFError:
            break
        networkyacc.parser.parse(s)
