
# import a specific function - better than importing whole odule
from functions_greetings import greet_user as greet_user_alias
#from functions_greetings import *

#import entier module - dont use this generally
import functions_greetings as greets

userInfo = greets.greet_user("kieranrs", "smithy", age=40, attributes={"key1":"value1"})
print(f"userInfo={userInfo}")

greets.additional_greetings(userInfo, "Bob", "Roger")

greets.additional_args(userInfo, addtional1="additional1", additional2="additiona2")
print(userInfo)