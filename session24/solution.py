def solution_function(given_int: int) -> str:
    if (2 <= given_int <= 6 or  20 < given_int) and not given_int % 2:
        return 'Blue'
    else:
        return 'Red'
def solution_to_different_problem():
    pass

#def solution_function(given_int: int) -> str:
#     if given_int % 2:
#         return 'Red'
#     elif 2 <= given_int <= 6 or  20 < given_int:
#         return 'Blue'
#     else:
#         return 'Red'
# def solution_to_different_problem():
#     pass