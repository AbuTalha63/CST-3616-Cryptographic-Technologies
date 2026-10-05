# Create a login app that takes a username and password, add salt to them,
# hash them, and them compare them to their respective stored hashes.

# we will use the MD5 algorithm to hash the compounded username and password, such as
# username_compound = username + salt & password_compound = password + salt
# Salt: 16 length random set of letters/digits with no punctuation

# store the hashes of this compounds into a text file

# import libs
import os
import hashlib