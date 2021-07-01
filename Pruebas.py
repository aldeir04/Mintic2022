num = (input("Digite un número de 4 dígitos: "))

p1 = int((num[0]%2 == 0))
p2 = int((num[1]%2 == 0))
p3 = int((num[2]%2 == 0))
p4 = int((num[3]%2 == 0))
print(p1, p2, p3, p4)

#if (int(num) >= 1000) and (int(num) <= 9999):
    
    
    #if (int(p1%2 == 0)) and (int(p2%2 == 0)) and (int(p3%2 == 0)) and (int(p4%2 == 0)):
    #    print(f"En el número {num}, todos sus dígitos son pares")
    #elif ((int(p1%2 == 0)) and (int(p2%2 != 0)) and (int(p3%2 == 0)) and (int(p4%2 == 0))) or (int(p1%2 == 0)) and (int(p2%2 == 0)) and (int(p3%2 != 0)) and (int(p4%2 == 0)) or (int(p1%2 == 0)) and (int(p2%2 == 0)) and (int(p3%2 == 0)) and (int(p4%2 != 0)) or (int(p1%2 != 0)) and (int(p2%2 == 0)) and (int(p3%2 == 0)) and (int(p4%2 == 0)):
    #    print(f"En el número {num}, hay mas dígitos pares (3) que impares (1)")
    #elif ((int(p1%2 == 0)) and (int(p2%2 != 0)) and (int(p3%2 != 0))) and (int(p4%2 == 0)) or (int(p1%2 != 0)) and (int(p2%2 == 0)) and (int(p3%2 != 0)) and (int(p4%2 == 0)) or (int(p1%2 != 0)) and (int(p2%2 == 0)) and (int(p3%2 == 0)) and (int(p4%2 != 0)) or (int(p1%2 != 0)) and (int(p2%2 != 0)) and (int(p3%2 == 0)) and (int(p4%2 == 0)) or (int(p1%2 == 0)) and (int(p2%2 != 0)) and (int(p3%2 == 0)) and (int(p4%2 != 0)) or (int(p1%2 == 0)) and (int(p2%2 == 0)) and (int(p3%2 != 0)) and (int(p4%2 != 0)):
    #    print(f"En el número {num}, hay igual dígitos pares e impares")
    #elif ((int(p1%2 == 0)) and (int(p2%2 != 0)) and (int(p3%2 != 0))) and (int(p4%2 != 0)) or (int(p1%2 != 0)) and (int(p2%2 == 0)) and (int(p3%2 != 0)) and (int(p4%2 != 0)) or (int(p1%2 != 0)) and (int(p2%2 != 0)) and (int(p3%2 == 0)) and (int(p4%2 != 0)) or (int(p1%2 != 0)) and (int(p2%2 != 0)) and (int(p3%2 != 0)) and (int(p4%2 == 0)):
    #    print(f"En el número {num}, hay mas dígitos impares (3) que pares (1)")
    #else:
    #    print(f"En el número {num}, todos sus dígitos son impares")
        
#else:
    #print("Digite un número de 4 digitos")
