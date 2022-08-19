from Variables.variables import *

def edit_numbers(num):
  global calculations

  if first:
    calculations[0] = calculations[0] + num
    text.config(state=tk.NORMAL)  # Changes textfield to normal state so can edit
    text.delete("1.0", tk.END)  # Delete text field content (1.0 or "1.0" works)
    text.insert(tk.END, calculations[0])
    text.config(state=tk.DISABLED)

  else:
    calculations[2] = calculations[2] + num
    text.config(state=tk.NORMAL)
    text.delete("1.0", tk.END)
    text.insert(tk.END, calculations[2])
    text.config(state=tk.DISABLED)


def toggle(op):
  global calculations
  global first

  if first:
    first = False
  
  elif calculations[2] == "":
    return None
  
  elif not calculations[2] == "":
    answer = calculate()
    first = False
    calculations[0] = str(answer)
  
  calculations[1] = op


def calculate():
  global first

  if calculations == ["", "", ""]:
    text.config(state=tk.NORMAL)
    text.delete("1.0", tk.END)
    text.insert(tk.END, "CLEARED")
    text.config(state=tk.DISABLED)
    return None

  one = float(calculations[0])
  two = float(calculations[2])
  answer = 0
  op = calculations[1]

  if op == "/":
    if two == 0:
      if one == 0:
        answer = 0
      else:
        answer = "ZERO ERROR"
    else:
      answer = one / two
  elif op == "x":
    answer = one * two
  elif op == "-":
    answer = one - two
  elif op == "+":
    answer = one + two

  text.config(state=tk.NORMAL)
  text.delete("1.0", tk.END)
  text.insert(tk.END, str(answer))
  text.config(state=tk.DISABLED)

  for i in range(3):
    calculations[i] = ""

  first = True

  return answer
