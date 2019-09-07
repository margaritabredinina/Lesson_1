
def get_summ(one, two, delimiter='&'):
    
    return f'{one}{delimiter}{two}'

one = 'Learn'
two = 'python'
#delimiter = ' '
summed = get_summ(one, two)
print(summed) 

