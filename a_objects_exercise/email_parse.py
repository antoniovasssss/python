def email_parse(email):
    username, domain = email.split('@')
    return {'username': username, 'domain': domain}

print(email_parse("coolcoder42@goodmail.com"))
print(email_parse("az@woohoomail.com"))
print(email_parse("1337pr0graMmer@coldmail.edu"))
    
