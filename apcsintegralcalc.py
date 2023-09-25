def integral_power_rule(a, n):
  int_exponent = n + 1
  int_coefficient = a
  if int_exponent != 0:
    int_coefficient = a * 1/(int_exponent)


  if int_coefficient == 0:
    int_str = "C"
  elif int_exponent == 0:
    int_str = str(a) + "ln(x)"
  elif int_exponent == 0:
    int_str = str(int_coefficient) + "x"
  else:
    int_str = f"{int_coefficient}*x^{int_exponent}"

  return int_str

a = float(input("Enter the value of 'a': "))
n = float(input("Enter the value of 'n': "))

derivative = integral_power_rule(a, n)
print(f"The integral of {a}x^{n} is: {derivative}")
