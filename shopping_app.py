money = 20
items = {'apple': 2, 'banana': 4, 'orange': 6}
for item_name in items:
    print('...........')
    print(f'You have {money} dollars in your wallet')
    print(f'Each {item_name} costs {items[item_name]} dollars')
    count = input(f'How many {item_name}s do you want?:')
    print(f'You will buy {count} {item_name}s')

    total_price = int(count) * items[item_name]
    print(f'The total price is {total_price} dollars')
    

    if money >= total_price:
        print(f'You have bought {count} {item_name}s')
        money -= total_price
    elif money == 0:
        print('Your wallet is now empty')
    else:
        print('...........')
        print('You do not have enough money')
        print(f'You cannot buy that many {item_name}s')
print(f'Your balance is {money} dollars')