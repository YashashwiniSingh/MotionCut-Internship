#Week2 - Temparature Convertor 

print("Welcome to Temparature Convertor!\n ")

print("Choose conversion\n")
print("1. Celsius To Farenheit")
print("2. Celsius To Kelvin")
print("3. Kelvin To Farenheit")
print("4. Kelvin To Celsius")
print("5. Farenheit To Celsius")
print("6. Farenheit To Kelvin")
c=1
while(c):
  try:
    choice=int(input("Enter Conversion Choice Number: "))
    print(choice)
    try:
      t1=int(input("Enter temparature: "))
      if choice==1:
        f=t1*(9/5)+32
        print(f"Farenheit Temparature is {f}")

      elif choice==2:
        k=273.15+t1
        print(f"Kelvin Temparature is {k}")

      elif choice==3:
        if t1<0:
          print("Kelvin Temparature cannot be negative. Try valid temp.")
        else:
          f=(t1-273.15)*(9/5)+32
          print(f"Farenheit Temparature is {f}")

      elif choice==4:
        if t1<0:
          print("Kelvin Temparature cannot be negative. Try valid temp.")
        else:
          c=t1-273.15
          print(f"Celsius Temparature is {c}")

      elif choice==5:
        c=(t1-32)*(5/9)
        print(f"Celsius Temparature is {c}")

      elif choice==6:
        k=(t1-32)*(5/9)+273.15
        print(f"Kelvin Temparature is {k}")
  
      else:
        print("Enter valid choice.")
    except:
      print("Enter valid choice")

  except:
    print("Enter valid choice")

  c=int(input("Press 1 to continue, 0 to quit "))
