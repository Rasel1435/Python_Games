email_id = input("Enter your Email ID: ").strip()

# First We have to slice user name

username = email_id[:email_id.index("@")]

# Second we have slice domain

domain = email_id[email_id.index("@")+1:]

# Print Output here

print(f"Your username is {username} and your domain is {domain}")