import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=30,pady=30)

def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()
    if weight == "" or height == "":
        result_label.config(text="Enter both  weight and height!")
    else:
        try:
            bmi = float(weight) / (float(height)/ 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number")

#ui
weight_input_label = tkinter.Label(text="Enter your weight (kg)")
weight_input_label.pack()

weight_input = tkinter.Entry(width=10)
weight_input.pack()

height_input_label = tkinter.Label(text="Enter your height (cm)")
height_input_label.pack()

height_input = tkinter.Entry(width=10)
height_input.pack()

calculator_button = tkinter.Button(text="Calculator",command = calculate_bmi)
calculator_button.pack()

result_label = tkinter.Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Your BMI is: {round(bmi,2)}.your are"
    if bmi <= 16:
        result_string += "severely thin!"
    if bmi > 16 and bmi <=17:
        result_string += "moderately thin!"
    if bmi > 17 and bmi <=18.5:
        result_string += "mild thin!"
    if bmi > 18.5 and bmi <=25:
        result_string += "normal"
    if bmi > 25 and bmi <=30:
        result_string += "overweight"
    if bmi > 30 and bmi <=35:
        result_string += "obese classs 1"
    if bmi > 35 and bmi <=40:
        result_string += "obese classs 2"
    else:
        result_string += "obese classs 3"
    return result_string

window.mainloop()
