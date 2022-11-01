Zodiac_List = ["Capricorn","Aquarius","Pisces","Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio","Sagittarius"]
Month_List = ["January", "February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
Birth_Month = input("What is your Birth Month? ")
x = 0
test = 1
Zodiac = "Shouldn't be this"
def Zodiac_finder(Day):
  global Zodiac_List, Birth_Month, x, Month_List, Zodiac, test
  if Day >= 0: 
    for month in Month_List:
      if Birth_Month == Month_List[x]:
        #print(x)
        #print(type(x))
        if x == 0:
          if Day < 20:
            Zodiac = Zodiac_List[x]
          else: Zodiac = Zodiac_List[x+1]
        elif x == 1:
          if Day < 19:
            Zodiac = Zodiac_List[x]
          else: Zodiac = Zodiac_List[x+1]
        elif x == 2:
          if Day < 21:
            Zodiac = Zodiac_List[x]
          else: Zodiac = Zodiac_List[x+1]
        elif x == 3:
          if Day < 20:
            Zodiac = Zodiac_List[x]
          else: Zodiac = Zodiac_List[x+1]
        elif x == 4:
          if Day < 21:
            Zodiac = Zodiac_List[x]
          else: Zodiac = Zodiac_List[x+1]
        elif x == 5:
          if Day < 21:
            Zodiac = Zodiac_List[x]
          else: Zodiac = Zodiac_List[x+1]
        elif x == 6:
          if Day < 23:
            Zodiac = Zodiac_List[x]
          else: Zodiac = Zodiac_List[x+1]
        elif x == 7:
          if Day < 23:
            Zodiac = Zodiac_List[x]
          else: Zodiac = Zodiac_List[x+1]
        elif x == 8:
          if Day < 23:
            Zodiac = Zodiac_List[x]
          else: Zodiac = Zodiac_List[x+1]
        elif x == 9:
          if Day < 23:
            Zodiac = Zodiac_List[x]
          else: Zodiac = Zodiac_List[x+1]
        elif x == 10:
          if Day < 22:
            Zodiac = Zodiac_List[x]
          else: Zodiac = Zodiac_List[x+1]
        elif x == 11:
          if Day < 22:
            Zodiac = Zodiac_List[x]
          else: Zodiac = Zodiac_List[0]
        print(Zodiac)
      x += 1
      test = 0
  else:
    print("Please enter a positive number")
    test = 1
while test == 1:
  Birth_Day = int(input("What is your Birth Day "))
  Zodiac_finder(Birth_Day)