# Bonus: Marks converter (closure)
# Write make_percent(total) that returns a function. The returned function takes obtained
# marks and returns the percentage for that total.
# Test: out_of_50 = make_percent(50), then out_of_50(40) → 80.0 · out_of_75 =
# make_percent(75), then out_of_75(60) → 80.0

def make_percent(total):
    def calculate(obtained):
        return (obtained/total)*100
    return calculate

out_of_50=make_percent(50)
print(out_of_50(40))