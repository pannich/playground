
def reverse(S):
    print(S)
    n = len(S)
    if n == 1:
        return S[-1]
    else:
        return S[-1] + reverse(S[:n-1])


if __name__ == "__main__":
  S = input()
  print(reverse(S))
