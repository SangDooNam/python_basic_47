"""Task 1"""




# def sum_series(num, x = 0):
#     """This function returns the sum of the positive integers of n+(n-2)+(n-4)..."""
#     if num - x <= 0:
        
#         return 0
    
#     x += 2
    
#     return num + sum_series(num - x)



# print(sum_series(7))
# print(sum_series(8))
# print(sum_series(15))


"""Task 2"""


# test_data1 = [
#     1,
#     [1, 2],
#     [1, [2, 3]],
#     [1, [2, [3, 4]]],
#     [1, [2, [3, [4, 5]]]],
# ]
# test_data2 = [
#     [1, [[2, 6], [3, 4]]],
#     [[5, 6, [7, 8]], [2, [3, [4, 5]]]],
#     [1, [2, 3]],
#     [1, 2],
#     1,
# ]




# def drill_sum(lst):
#     """This function returns the sum of integers from lists, including those within nested lists """
#     total = 0
    
#     for i in lst:
        
#         if isinstance(i, int):
            
#             total += i
            
#         elif isinstance(i, list):
            
#             total += drill_sum(i)
    
#     return total
    
    


    


# print(drill_sum(test_data1))
# print(drill_sum(test_data2))




"""Taks 3"""


test_data1 = [
    {
        "title": "Home",
        "pages": [
            {
                "title": "About",
                "pages": [
                    {
                        "title": "The company"
                    },
                    {
                        "title": "Our services"
                    },
                    {
                        "title": "Our products"
                    },
                    {
                        "title": "Our deliveries",
                        "pages": [
                            {
                                "title": "National"
                            },
                            {
                                "title": "International"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Shop",
                "pages": [
                    {
                        "title": "Browse all"
                    },
                    {
                        "title": "Categories"
                    }
                ]
            },
            {
                "title": "My account",
                "pages": [
                    {
                        "title": "Settings"
                    },
                    {
                        "title": "Edit profile"
                    },
                    {
                        "title": "My transactions"
                    }
                ]
            }
        ]
    }
]




def count_pages(lst):
    """This counts the amount of pages in a website."""
    if not lst:
        return 0
    
    total = 0
    
    for page in lst:
        total += 1
        
        if 'pages' in page:
            
            total += count_pages(page['pages'])
        
    return total
    
    
print(count_pages(test_data1))


