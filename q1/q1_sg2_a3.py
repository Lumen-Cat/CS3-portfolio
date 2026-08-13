userBirth = int(input("What is your year of birth? "))
while userBirth < 1900:
    print("Invalid Year, it should not be earlier than 1900")
    userBirth = int(input("\nWhat is your year of birth? "))

if (userBirth - 1900) % 12 == 0:
    print("\nYour Chinese Zodiac Sign is: Rat (鼠 / Shǔ)")
    
elif (userBirth - 1900) % 12 == 1:
    print("\nYour Chinese Zodiac Sign is: Ox (牛 / Niú)")
    
elif (userBirth - 1900) % 12 == 2:
    print("\nYour Chinese Zodiac Sign is: Tiger (虎 / Hǔ)")
    
elif (userBirth - 1900) % 12 == 3:
    print("\nYour Chinese Zodiac Sign is: Rabbit (兔 / Tù)")
    
elif (userBirth - 1900) % 12 == 4:
    print("\nYour Chinese Zodiac Sign is: Dragon (龙 / Lóng)")
    
elif (userBirth - 1900) % 12 == 5:
    print("\nYour Chinese Zodiac Sign is: Snake (蛇 / Shé)")
    
elif (userBirth - 1900) % 12 == 6:
    print("\nYour Chinese Zodiac Sign is: Horse (马 / Mǎ)")
    
elif (userBirth - 1900) % 12 == 7:
    print("\nYour Chinese Zodiac Sign is: Goat (羊 / Yáng)")
    
elif (userBirth - 1900) % 12 == 8:
    print("\nYour Chinese Zodiac Sign is: Monkey (猴 / Hóu)")
    
elif (userBirth - 1900) % 12 == 9:
    print("\nYour Chinese Zodiac Sign is: Rooster (鸡 / Jī)")
    
elif (userBirth - 1900) % 12 == 10:
    print("\nYour Chinese Zodiac Sign is: Dog (狗 / Gǒu)")
    
elif (userBirth - 1900) % 12 == 11:
    print("\nYour Chinese Zodiac Sign is: Pig (猪 / Zhū)")
    

