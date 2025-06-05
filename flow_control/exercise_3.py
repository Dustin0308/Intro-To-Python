# Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')         # Product2. Matches case '113' which prints 'Product2'.
bar_code_scanner(142)           # Product not found!. Doesn't match any case so it goes to default 
                                # value (case _). '142' is not the same as 142.
