# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string:

gommi = {'https://','http://','www.'}

def domain_name(url):
    for key in gommi:
        url = url.replace(key,'')
    domain = ''
    for letter in url:
        if letter in {'.','/'}: break
        domain += letter
    return domain

print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
