def myBMI(w, h):
  'take two argument and show the bmi is normal or not'
  bmi = (w*709)/(h**2)

  if bmi >= 25:
    print('Overweight')
  elif 18.5 <= bmi < 25:
    print("Normal")
  else:
    print("Underweight")
    
    
def myBMIuser():
  w = eval(input('enter weight: '))
  h = eval(input('enter height: '))
  bmi = (w*709)/(h**2)

  if bmi >= 25:
    print('Overweight')
  elif 18.5 <= bmi < 25:
    print("Normal")
  else:
    print("Underweight")