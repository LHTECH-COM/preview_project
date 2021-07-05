from _ast import Num


    
def order(sentence):#sort chuoi theo so trong list
    return ' '.join(sorted(sentence.split(), key=lambda w:sorted(w)))

def digital_root(n): #cong 2 so trong chuoi vd nhu 16 = 1+6=7
#     count_str = list(str(n))
#     count = n
#     
#     while count >= 10:
#         count = 0
#         
#         for i in range(0, len(count_str)):
#             count += int(count_str[i])
#         count_str = list(str(count))
#     return count
    
    return n if n < 10 else digital_root(sum(map(int,str(n))))

def duplicate_encode(word):
#     count = {}
#     for s in word:
#         s_temp = s.lower()
#         if s_temp in count:
#             count[s_temp] += 1
#         else:
#             count[s_temp] = 1
#     
#     data = ""
#     
#     for s in word:
#         if count[s.lower()] > 1:
#             data = data + ")"
#         else:
#             data = data +"("
#         
#     return data
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o') 

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

def to_camel_case(text): #viet hoa chu dau tien cua chuoi
    #your code here
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    
    return s[0] + ''.join(i.capitalize() for i in s[1:])

def valid_parentheses(string): #kiem tra co dung dang ()()()
    #your code here

    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
    
def narcissistic(number):
    """
        153 = 1^3 + 5^3 + 3^3
        370 = 3^3 + 7^3 + 0^3
        407 = 4^3 + 0^3 + 7^3.    
    """
    return number == sum([int(x) ** len(str(number)) for x in str(number)])
        


def is_pangram(s): #chuoi string co chua ky tu tu a-z 
    #cach 1
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for char in alphabet:
#         if char not in s.lower():
#             return False
#     return True

    #cach pho bien
    import string
    return set(string.ascii_lowercase) <= set(s.lower())

def find_outlier(integers):
    
#     even_num = 0
#     odd_num = 0
#     even_list = []
#     odd_list = []
#     for i in integers:
#        
#         if int(i) % 2 == 0:
#             even_num +=1
#             even_list.append(i)
#         else:
#             odd_num +=1
#             odd_list.append(i)
#     return even_list[0] if even_num == 1 else odd_list[0]
    odds = [x for x in integers if x%2!=0]
    evens= [x for x in integers if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

def permutations(string):
    """
        permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
        ('a','b','c','d') -> abcd -> "".join('a','b','c','d') -> tupple -> string
        
        remove duplicate string in list []: list(dict.fromkeys(lists))
    """
#     import itertools
#     
#     lists = ["".join(str) for str in itertools.permutations(string)]
#     print (list(set(lists)))
#     return list(dict.fromkeys(lists))
    import itertools
    return list("".join(p) for p in set(itertools.permutations(string)))

def zeros(n):
    """
        zeros(6) = 1
        # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

        zeros(12) = 2
        # 12! = 479001600 --> 2 trailing zeros
    """
#     import operator as op
#     import functools as ft
#     
#     if n == 0:
#         return 0
#     
#     dem = ft.reduce(op.mul, range(1,n+1))
#     numbers = str(dem)[:: -1]
    from functools import reduce

    numbers = (reduce(lambda x, y: x * y, range(1, n+1)))
    numbers = str(numbers)[:: -1]
    dem = 0
    for n in str(numbers):
        if int(n) == 0:
            dem +=1
        else:
            break
        
    return dem

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
   
def perimeter(n):
    """
        The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. 
        It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80
    """
    square = 4 * sum(recur_fibo(i) for i in range(1, n+2))
    return square

def is_prime(n):
    import re
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None


def gap(g, m, n):
    previous_prime = n
    for i in range(m, n + 1):
        if is_prime(i):
            if i - previous_prime == g: 
                return [previous_prime, i]
            previous_prime = i
    return None
    


def format_duration(seconds):
    times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]
    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
        
        
        
if __name__ == "__main__":
#     print(order("is2 Thi1s T4est 3a"))
#     print(order("4of Fo1r pe6ople g3ood th5e the2"))
#     print(digital_root(16))
#     print(digital_root(942))
#     print (duplicate_encode("recede"))
#     print(xo('xo0'))
#     print(find_next_square(114))
#     print(find_next_square(625))
#     print(to_camel_case("the_stealth_warrior"))
#     print (valid_parentheses("apy(bgilw(asz))zo"))
#     print(narcissistic(371))
#     print(is_pangram("the quick brown fox jumps over the lazy dog"))
#     print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
#     print(sorted(permutations('aabb')))
#     print(zeros(30))
#     print(perimeter(30))
#     print(gap(6,100,110))
    print(format_duration(36007878979898080))
    
