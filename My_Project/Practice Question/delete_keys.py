user = {
    "username": "my_user",
    "password": "test@123",
    "email": "myuser@test.com",
    "address": "ABC Road, 111",
    "country": "US",
}

sensitive_data = ["password", "address","phone"]

# for key in user:
#     if key in sensitive_data:
#         user.pop(key)
# print(user)
#o/p:
# Traceback (most recent call last):
#   File "/Users/bhushanpawar/Desktop/Python/My_Project/Practice Question/delete_keys.py", line 11, in <module>
#     for key in user:
#                ^^^^
# RuntimeError: dictionary changed size during iteration

for key in sensitive_data:
    if key in user:
        user.pop(key)
    else:
        print(f"wrong key {key}")
print(user)

#import note when we are using loop on dict or list and want to change the same list it will give runtime error, as above