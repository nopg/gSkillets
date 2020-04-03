import sys
import argparse

def run_test(username,password):
    print(f"Username = {username}")
    print(f"Password = {password}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Please use this syntax:")
    parser.add_argument("-u", "--username", help="Example Username", type=str, required=True)
    parser.add_argument("-p", "--password", help="Example Password", type=str, required=True)
    args = parser.parse_args()
    
    print(parser.print_help())
    print(parser.print_usage())

    username = args.username
    password = args.password

    largs = [username,password]

    run_test(*largs)