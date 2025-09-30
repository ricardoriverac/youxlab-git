height = float (input('Enter your Height: '))
weight = float (input('Enter your Weight: '))
IMC = weight / (height * height)
if IMC<18.5:
    print ('Underweight!')
elif 18.5<=IMC<25:
    print ('Ideal weight!')
elif 25<=IMC<30:
    print ('Overweight!')
elif 30<=IMC<40:
    print ('Obesity!')
elif 40<=IMC:
    print ('Morbid obesity!')