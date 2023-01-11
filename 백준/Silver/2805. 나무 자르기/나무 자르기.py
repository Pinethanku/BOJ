import sys

def tree_2805():
    trees, lenth = (map(int, sys.stdin.readline().split()))  #나무의 수, 가져가려는 길이
    treelist = list(map(int, sys.stdin.readline().split())) #나무 높이
    if trees == 1:
        print(treelist[0]-lenth)
        return 0
    else:
        treelist.sort(reverse=True)
        treelist.append(0)
        
        setlen = treelist[0]
        nth = 0
        sumlen = 0
        while(sumlen < lenth and nth < trees) :
            if treelist[nth+1] == 0:
                print(((sumlen-lenth)//(nth+1) + setlen))
                return 0
            sumlen += (treelist[nth]-treelist[nth+1])*(nth+1)
            setlen -= treelist[nth]-treelist[nth+1]
            nth += 1
            #print("sum =", sumlen," set =", setlen, " nth =", nth)

        print(((sumlen-lenth)//nth) + setlen)
        return 0

tree_2805()
