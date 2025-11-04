def cp(name, age, city=""):
    if city:
        return f"kazvate se {name} na {age} godini ste i jiveete vuv {city}."
    else:
        return f"kazvate se {name} na {age} godini ste i jiveete vuv Wein."
nm = input("kak se kazvate:")
ag = input("na kolko godini ste:")
cty = input("ot kude ste:")
print(cp(nm,ag,cty))