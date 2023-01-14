import sys

def sort_1181():
    times = int(sys.stdin.readline())
    if times==1:
        print(sys.stdin.readline().strip())
        return 0
    word = {}
    for i in range(times):
        read = sys.stdin.readline().strip()
        word[read] = len(read)
    
    words = sorted(word.items(), key=lambda x: (x[1], x[0]))
    for wor in words:
        print(wor[0])
    return 0
    
sort_1181()