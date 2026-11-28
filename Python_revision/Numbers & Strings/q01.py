# A. Numbers and strings
# Q1. Bill splitter. Write split_bill(total, people, tip_percent=10) that adds the tip and returns
# each person’s share, rounded to 2 decimals.
# Test: split_bill(3000, 4) → 825.0 · split_bill(2500, 3, 0) → 833.33

def split_bill(total, people, tip_percent=10):
    share_per_person = round((total*(1+tip_percent/100))/people,2)
    return share_per_person

print(split_bill(2500, 3, 0))
