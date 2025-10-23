r = "This is python string, and its types, methods, and functions"
print(r.upper())
print(r.lower())
print(r.split(", ")) 
p_list = ['naruto', 'sasuke', 'sakura', 'kakashi']
print(", ".join(p_list))
print(r.replace("python", "Java"))
print(r.find("types"))
print("python" in r)
books = "I have ordered {} volumes and its price is {}"
v1 = "one piece"
v2 = 2000
print(books.format(v1,v2))
print(r[0:31])
print(r[:])