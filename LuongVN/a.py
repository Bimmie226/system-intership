import math
import random

def isPrime(n):
  for i in range(2, math.isqrt(n) + 1):
    if n % i == 0:
      return False
  return True if n > 1 else False

def powmod(a, exp, Mod):
  res = 1
  while exp > 0:
    if exp % 2 == 1: res = res * a % Mod 
    a = a * a % Mod 
    exp /= 2
  return res

while True:
  p = int(input("\nNhập p (số nguyên tố): "))
  g = int(input("Nhập g (generator): "))

  if not isPrime(p):
    print("p không phải là số nguyên tố. Nhập lại!")
    continue
  break

a = random.randint(1, 50)
b = random.randint(1, 50)
print(f"\nSố ngẫu nhiên tạo ra: a = {a}, b = {b}")

r1 = powmod(g, a, p)
r2 = powmod(g, b, p)
print(f"\nR1 = {r1}\nR2 = {r2}")

k1 = powmod(r2, a, p)
k2 = powmod(r1, b, p)
print(f"\nKhóa bí mật chung tính bởi Alice: {k1}")
print(f"Khóa bí mật chung tính bởi Bob: {k2}")

k3 = powmod(g, a * b, p)
print(f"\nKiểm tra khóa chung g^(a*b) mod p = {k3}")

if k1 == k2 == k3:
  print("\nCả hai bên đã tạo ra cùng một khóa bí mật chung!")
else:
  print("\nCó lỗi! Các khóa không trùng khớp.")