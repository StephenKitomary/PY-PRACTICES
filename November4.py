"""number_to_word = {1: 'one', 2:"two", 3: "three", 4: "four", 10: "ten"}
word_to_number = {w: d for d, w in number_to_word.items()}
print(word_to_number)
"""

##ASSIGNMENT SOLUTIONS####
"""prices = [100,150,200,250,300]

newprices = list(map(lambda x:x-(0.1*x), prices))
print(newprices)
"""
"""Side notes
def map(func, iterable):
    for i in iterable:
        yield func(i)
"""
"""
product_codes = ["abc123", "def456", "ghi789"]
new_product_codes = list(map(lambda x: x.upper(), product_codes))
print(new_product_codes)
"""
"""weights_kg = [50, 75, 100, 120]

def kg_to_lbs(x):
    lbs = x*2.20462
    return lbs
weights_lb = list(map(kg_to_lbs,weights_kg))

print(weights_lb)"""


recent_visitors = [101, 102, 103, 101, 104, 105, 102, 106]

unique_recent_visitors = set(recent_visitors)
print("These are the unique visitors: ",unique_recent_visitors)

recent_purchasers = {102, 103, 107, 108}
print("These are the customers who visited us recently and made purchases: ", recent_purchasers.intersection(unique_recent_visitors))

vip_customers = {105, 106, 109, 110}

resent_and_vip_customers = unique_recent_visitors.union(vip_customers)
print("These are the resent and VIP visitors", resent_and_vip_customers)

VIP_but_not_recent = vip_customers.difference(unique_recent_visitors)
print("These are VIP customers ut did not visit our website recently", VIP_but_not_recent)