# Collect an email address from the user and then find out if the user has a custom domain name or a popular domain name. For example
# We collect an email address from the user and then we are going to find out if that email has a custom domain name or a popular domain name. For example:

mail = ''
while len(mail) != 2:
    mail = input('Please give an E-mail adress: ').split('@')

domain = mail[1]
domain = domain.replace('.com','').replace('.mx','').replace('.gob','')
if domain in ['yahoo','gmail','hotmail','outlook']:
    print(f"Hi {mail[0]} I'm seeing that your email is registered with {domain.title()}, That's great!")
else:
    print(f"Hi {mail[0]}, I'm noticing that you're using a custom domain of {domain.title()}, Awesome!")
