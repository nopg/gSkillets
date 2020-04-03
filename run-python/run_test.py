import sys
import argparse

def run_test(username,password):
    print(f"Username = {username}")
    print(f"Password = {password}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Example Username", type=str)
    parser.add_argument("-p", "--password", help="Example Password", type=str)
    args = parser.parse_args()

    if len(sys.argv) != 5:
        print(sys.argv)
        print(len(sys.argv))
        parser.print_help()
        parser.exit()
        sys.exit(1)
    
    username = args.username
    password = args.password

    largs = [username,password]

    run_test(*largs)