import sys
import argparse

def run_test():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Example Username", type=str)
    parser.add_argument("-p", "--password", help="Example Password", type=str)
    args = parser.parse_args()

    if len(sys.argv) != 3:
        print(sys.argv)
        print(len(sys.argv))
        parser.print_help()
        parser.exit()
        sys.exit(1)
    
    username = args.username
    password = args.password

    largs = [username,password]

    for arg in largs:
        print(f"ARG =  {arg}")

if __name__ == "__main__":
    run_test()