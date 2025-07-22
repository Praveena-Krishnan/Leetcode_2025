# n=int(input("enter the no. of days"))
# weeks=n//7
# rev=0
# for i in range(n):
#     rev+=100
# t_rev=rev-((weeks*2)*100)
# print("Total revenue is", t_rev)

def total_revenue(n):
    total = 0
    for day in range(n):
        weekday = day % 7
        if weekday == 5 or weekday == 6:  # Friday or Saturday
            revenue = 0
        else:
            revenue = (weekday + 1) * 100
        total += revenue
    return total

# Example usage:
n = int(input("Enter number of days: "))
print("Total revenue over", n, "days is:", total_revenue(n))
