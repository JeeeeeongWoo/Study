A, B, C = input().split()       #split은 문자열.split 형식으로 사용하며, 구분자 파라미터를 사용한다.
A = int(A)      #input()은 문자열로 값을 받아오고 split을 사용하였으므로 정수값을 받기 위해 int로 변환
B = int(B)
C = int(C)

print((A + B) % C) 
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)