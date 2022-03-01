logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

print("Welcome to the Secret Auction Program.")

bidder = ''
max_bid = 0
is_bidders = 'yes'
while is_bidders.lower() != 'no':
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))

    if max_bid < bid:
        max_bid = bid
        bidder = name

    is_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    import os
    os.system('cls')

print(f"The winner is {bidder} with a bid of ${max_bid}.")
