# A basic example of a dictionary comprehension

squares = { f'{number}-squared': number * number
            for number in range(1, 6) }
print(squares)
