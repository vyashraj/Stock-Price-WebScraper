from tkinter import *
import Check_N_114719 as c
global l1
global l2
def create(price1,price2):
    root2 = Tk()
    root2.geometry("350x350")
    print(price1,price2)
    p1 = StringVar()
    p1=price1
    p2 = StringVar()
    p2=price2
    root2.title("Coin Price")
    show = Label(root2, text=price1)
    show.grid(row=1, column=2)
    show2 = Label(root2, text=price2)
    show2.grid(row=2, column=2)
    exit=Button(root2,text="Next",command=root2.destroy)
    exit.grid(row=3,column=2)
    root2.mainloop()

def main():
    def input_window():
        def verify():
            l1 = website_1.get()
            l2 = website_2.get()
            print(l1, "     ", l2)

            an = c.Start()
            while True:
                c.checkkk(l1=l1,l2=l2,xpath="priceValue")
        input_window = Tk()
        input_window.title("Website Details")
        input_window.minsize(500, 200)

        headlines = Label(input_window, text="Enter Website Details")
        headlines.grid(row=1, column=3)

        website_1 = StringVar()
        website_2 = StringVar()
        w1 = Entry(input_window, textvariable=website_1)
        w1_name = Label(input_window, text="Website 1  : ")
        w1_name.grid(row=2, column=1)
        w1.grid(row=2, column=3)
        w2 = Entry(input_window, textvariable=website_2)
        w2.grid(row=3, column=3)
        w2_name = Label(input_window, text="Website 2  : ")
        w2_name.grid(row=3, column=1)

        w1_button = Button(input_window, text="Start", command=lambda: (input_window.destroy(), verify()))
        w1_button.grid(row=4, column=3)
        input_window.mainloop()

    input_window()


if __name__ == "__main__":
    main()
