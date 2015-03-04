'''
 - Requires the user to login..
 - To test application type username as SmithJ and Password as testing as shown in dictionary
 - Modifications can be to read the password from a file or a server. 
 - Author: Tony Otite 
'''

import getpass

confirm_password = None

user = dict()
user['SmithJ'] = 'testing'
user['CandyK'] = 'sweetie'
user['JackP'] = 'birdie'

def Username():
 username = raw_input("Enter your username ")
 while username == "":
  username = raw_input("Enter your username")
 return username
 
def Password():
 password = getpass.getpass("Enter your password ")
 while password == "":
  password = getpass.getpass("Enter your password ")
 return password

# call the Username and Password function
# fine username from user
# assign value to confirm_password
confirm_password = user[Username()]
entered_password =  Password()

 
if entered_password != "":
 if entered_password == confirm_password:
  print 'Access Granted'
  print 'This is your list of items, what would you like to do?'
 else: 
  print 'Access Denied'
  
 
