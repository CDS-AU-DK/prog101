"""
Driver script for creating instances of class Person in persons
"""
import argparse
from persons import Researcher


def main():
    ap = argparse.ArgumentParser(description = "[INFO] creating instances of researchers")
    ap.add_argument("-n", "--name", required=True, type=str, help="str, name of researcher")
    ap.add_argument("-a", "--age", required=False, type=int, default=-1, help="int, age of researcher")
    ap.add_argument("-t", "--title", required=False, type=str, default="graduate", help="str, academic title")
    ap.add_argument("-r", "--research", required=False, type=str, help="str, research area-s")
    args = vars(ap.parse_args())
    
    kristoffer = Researcher(name = args["name"], age = args["age"], title = args["title"], area = args["research"])
    kristoffer.says_hello()
    print()
    kristoffer.talks_research()
    
if __name__=="__main__":
    main()