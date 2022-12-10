msg = "Journey Before Destination"
msg_upr = msg.upper()
msg_lwr = msg.lower()
msg_cap = msg.capitalize()
msg_title = msg.title()
msg_swp = msg.swapcase()
msg_cf = msg.casefold() # same as lower
print(msg)
print(msg_lwr)
print(msg_cap)
print(msg_title)
print(msg_swp)
print(msg_cf)

# aligment
print(msg.ljust(100,'-'))
print(msg.rjust(100))
print(msg.center(100))

# aligment with f-string on padding
print(f"{msg:>50}") #same as rjust
print(f"{msg:<50}") #same as ljust
print(f"{msg:^50}") #same as center