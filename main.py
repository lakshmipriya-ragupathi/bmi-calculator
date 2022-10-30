from tkinter import *
root = Tk()

root.geometry("+750+500")
def bmi():
    h = int(height.get())
    w = int(weight.get())
    bmi_sum = 10000*w/(h*h)
    label.config(text = "BMI is : " + str(bmi_sum))

weight_label = Label(root, padx = 0, pady = 1, text = "Enter the weight (kgs): ")
weight_label.pack()
weight = Entry(root, width = 15, bg = 'grey', fg = 'white', borderwidth= 2)
weight.pack()

height_label = Label(root, padx = 0, pady = 2, text = "Enter the height in (cms): ")
height_label.pack()
height = Entry(root, width = 15, bg = 'grey', fg = 'white', borderwidth = 2)
height.pack()

label = Label(root, text = "BMI is : ")
label.pack()

Button(root, text = "Calculate BMI", command = bmi).pack()
root.mainloop()
