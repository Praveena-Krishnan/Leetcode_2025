def printing(n:int)->None:
    if n<1:
        return
    printing(n-1)
    print(n)
if __name__ == "__main__":
    printing(5)