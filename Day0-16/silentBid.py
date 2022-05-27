name = input("Enter bidder's Name: ")
bid = int(input("Enter amount: "))
auction = {}
choice = input("Are there other bidders (yes/no): ")
auction[bid] = name
while (choice == "yes"):
    name = input("Enter bidder's Name: ")
    bid = int(input("Enter amount: "))
    choice = input("Are there other bidders (yes/no): ")
    auction[bid] = name

val = sorted(auction.keys())
print("The winner of the auction is: ", auction.get(val[len(val)-1]))
