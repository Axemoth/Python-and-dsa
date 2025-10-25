#Initializing and printing a dictionary
chai_types={'masala':'chai','ginger':'tea'}
#prints only keys
for chai in chai_types:
    print(chai)
    #prints keys and values
for key,value in chai_types.items():
    print(f"{key}-{value}")

chai_types['lemon']='green tea'
print(chai_types)

#You can call dictionary in dictionary
tea_types = {"chai": {"green tea": "lemon", "black tea": "masala"},
             "herbal": {"chamomile": "honey", "peppermint": "mint"}}
print(tea_types)
print(tea_types["chai"])
print(tea_types["chai"]["green tea"])
print(tea_types["chai"], tea_types["herbal"])

numbers = {1:"one",6:"six",7:"seven"}
print(numbers)
print(len(numbers))

print(chai_types["ginger"])