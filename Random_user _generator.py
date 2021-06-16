import random

first_name = ['Aarav', 'Aditya', 'Dhruv', 'Kiran', 'Kabir', 'Veer', 'Rahul', 'Shreyas', 'Yash', 'Ishaan', 'Chethan', 'Vinay', 'Pramod']
last_name = ['Reddy', 'Singh', 'Patel', 'Kapoor', 'Gowda', 'Chawla', 'Lal', 'Khatri', 'Malhotra', 'Iyer', 'Jain', 'Khanna', 'Kumar']
States = ['Bangalore', 'Delhi', 'Kerela', 'Mumbai', 'Hyderabad', 'Patna', 'Shimla', 'Jaipur', 'Chennai', 'Kolkata', 'Lucknow', 'Gandhinagar']

for name in range(100):
    first_name_random = random.choices(first_name)
    second_name_random = random.choices(last_name)
    
    full_name = first_name_random + second_name_random
    phone = random.randint(6000000000,9999999999)
    state = random.choices(States)
    
    print(*full_name, sep = ' ')
    print(phone)
    print(*full_name,random.randint(1,100),"@gmail.com", sep = '')
    print(*state, sep = ' ')
    print('\n')
    
