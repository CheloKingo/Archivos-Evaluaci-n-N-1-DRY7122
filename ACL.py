ACLNum = int(input("¿Cual es tu numero de IPv4 ACL ? "))
if ACLNum >= 1 and ACLNum <= 99:
    print(" Esta es una ACL ipv4 Estandar.")
elif ACLNum >=100 and ACLNum <= 199:
    print("Esta es una ACL ipv4 Extendida.")
else:
    print("esta no es una ACL Estandar y tampoco es una Extendida.")