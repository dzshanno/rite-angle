number_of_cards = 1024
m=5
piles = 2 ** m
cards_per_pile = number_of_cards / piles

print('piles' + str(piles))
print('cards per pile ' + str(cards_per_pile))

def time_to_order(cards,stacks):
    time_taken_to_order = cards * (cards+1) * 0.5 * stacks
    return time_taken_to_order

def time_to_collate(cards,piles):
    time_taken_to_collate = number_of_cards * m + (2**(m-1))
    return time_taken_to_collate

overall_time = 0
time_to_divide = 1000
overall_time = time_to_divide + time_to_order(cards_per_pile,piles)+ time_to_collate(cards_per_pile,piles)

print(time_to_divide)
print(time_to_order(cards_per_pile,piles))
print(time_to_collate(cards_per_pile,piles))
print(overall_time)
        
        
# m=0 time = 525800
# m-1 time = 264681
# m=2 time = 134634
# m=3 time = 70123
# m-4 time = 38380
# m=5 time = 23032
# m=6 time = 15880
# m=7 time = 12840
# m=8 time = 11880 = 119 seconds quickest solution
# m=9 time = 12008    
# m=10 time = 12776   

answer = 119
result = int(answer* 0.017)
#result = 2
