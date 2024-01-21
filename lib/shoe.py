#!/usr/bin/env python3

# class Shoe:
    
#     def __init__(self, brand, size=9):
#         self._brand = brand
#         self._size = size
#         self._condition = 'New'  # Initialize condition to 'Used'
        
#     def get_brand(self):
#         return self._brand 
    
#     def set_brand(self, new_brand):
#         self._brand = new_brand
        
#     def get_size(self):
#         return self._size 
    
#     def set_size(self, new_size):
#         if type(new_size) is  int:
#             self._size = new_size
#         else:
#             print('Size must be an integer')
            
#     def get_condition(self):
#         return self._condition
        
#     def set_condition(self, new_condition):
#         if new_condition.lower() == 'new':
#             print("The shoe has been repaired.")
#             self._condition = 'New'
#         else:
#             print("Invalid condition. The condition remains as 'Used'.")
            
#     def cobble(self):
#         print('Your shoe is as good as new!')
#         self._condition = 'New'  
        
#     brand = property(get_brand, set_brand)  
#     size = property(get_size, set_size)  
#     condition = property(get_condition, set_condition)
        
        
# luku = Shoe('Nike', 8)  
# luku.brand = 'Adidas'  # Correcting brand assignment
# luku.size = 'forty five' 
# luku.condition = 'repaired'
# print(luku.condition)

# print(f"Boniface prefers {luku.brand} shoes, size: {luku.size}")

#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else: 
            print('size must be an integer')

    def cobble(self):
        print('Your shoe is as good as new!')
        Shoe.condition = "New"

    size = property(get_size, set_size)