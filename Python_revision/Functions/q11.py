# Q11. Monthly expenses (*args and a default). Write total_expense(*amounts,
# budget=5000) that returns a tuple of (total, money left, "Within budget" or "Over
# budget").
# Test: total_expense(1200, 800, 2500) → (4500, 500, 'Within budget') · total_expense(3000,
# 2500) → (5500, -500, 'Over budget')

def total_expenses(*amounts, budget=5000):
    total = sum(amounts)
    money_left = budget-total
    if total<budget:
        status="within budget"
    else:
        status="over budget"
    return total ,money_left ,status

print(total_expenses(3000,2500))