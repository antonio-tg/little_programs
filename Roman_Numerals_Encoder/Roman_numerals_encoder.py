# Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

roman = {'1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX','10':'X','20':'XX','30':'XXX','40':'XL','50':'L','60':'LX','70':'LXX','80':'LXXX','90':'XC','100':'C','200':'CC','300':'CCC','400':'CD','500':'D','600':'DC','700':'DCC','800':'DCCC','900':'CM','1000':'M','2000':'MM','3000':'MMM'}

def decoder(n):
    l = len(n)
    m = ''
    if n in roman.keys():
        m = roman[n]
    else:
        for d in n:
            for i in range(l-1):
                d += '0'
            l -= 1
            if d in roman.keys():
                d = roman[d]
            m += d 
    m = m.replace('0','')
    return m


n = input('Enter a number to convert to Roman: ')

m = decoder(n)

print(f'The number {n} in roman is {m}')
