# amobin19

integer_input = int(input("Enter and integer: "))

thousands = int(integer_input/1000)
hundreds = int((integer_input-thousands*1000)/100)
tens = int(((integer_input-thousands*1000)-(hundreds*100))/10)
ones = int(((integer_input-thousands*1000)-(hundreds*100)-(tens*10)))

print(thousands)
print(hundreds)
print(tens)
print(ones)
