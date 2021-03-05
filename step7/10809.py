s = input()
a_list = list(range(ord('a'),ord('z')+1))

for i in a_list:
    print(s.find(chr(i)), end=" ")


#find()함수는 값을 못 찾으면 자동으로 -1로 반환해준다. ascii코드를 이용하면 쉬운 문제였다.
#참고1: https://yang-wistory1009.tistory.com/73
#참고2: https://ooyoung.tistory.com/68