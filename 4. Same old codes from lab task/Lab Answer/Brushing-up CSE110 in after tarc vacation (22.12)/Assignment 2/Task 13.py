num=int(input("Enter your mark: "))
if num>0 and num<=100:
  if num>=90 :
    print("A")
  elif num>=80 :
    print("B")
  elif num>=70 :
    print("C")
  elif num>=60 :
    print("D")
  elif num>=50 :
    print("E")
  else:
    print("Bellow 50")
else :
  print("It's not your cup of tea to get over 100. Only Rahi can do this")