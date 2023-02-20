import sys

def main_pwsearch() -> None:
    pages, problems = tuple(map(int, sys.stdin.readline().split()))
    pw_dict = {}
    for i in range(pages):
        site, pw = tuple(sys.stdin.readline().split())
        pw_dict[site] = pw
    for i in range(problems):
        print(pw_dict[sys.stdin.readline().strip()])
        
if __name__ == '__main__':
    main_pwsearch()