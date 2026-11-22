# Exercise 12: Ride fare calculator
# Fare = Rs 100 base + Rs 40 per km. At night (hour 22 or later, or before 6), add 20%. Take
# the km and the hour (0–23) and print the final fare.
# Test: 10 km at hour 23 → Fare: Rs 600.0

ride_in_km = int(input("How many kilometers you want to ride?: "))
ride_time = int(input("At what time you want to ride?: "))
fare = 100 + (ride_in_km * 40)
if ride_time >= 22 or ride_time < 6:
    fare = fare + (fare * 0.20)
print(f"Final Fare: Rs. {fare}")