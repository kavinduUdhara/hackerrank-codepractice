duration = int(input("duration in months: "))
inter_rate = float(input("interest rate [%]: "))
amount = int(input("amount [LKR]: "))
inter_renew = (input("renew: [m] monthly [a] anually [x] after mathurity: "))

final_payble = 0

if inter_renew.lower() == "m":
    for i in range(1, duration+1):
        interest = amount / 100 * inter_rate / 12
        final_payble += interest + amount

if inter_renew.lower() == "x":
    final_payble = (amount / 100 * inter_rate / 12 * duration) + amount
print(final_payble)
    