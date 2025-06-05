def print_name(n:int)-> None:
    if n<=0:
        return
    print_name(n-1)
    print("Praveena Krishnan")
    
if __name__ == "__main__":
    print_name(5)
    
    