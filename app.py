import webbrowser
from tkinter import Button, Label,Entry,Tk
import os
import datetime
import shutil
from tkinter import messagebox as msg
from tkinter import simpledialog as sd

top = Tk()

top.title("Library management app")
top.geometry("700x400")

Label(top, background="black", height="100", width="700").place(x=0,y=0)
Label(top, background="black", foreground="white", font=("Arial","23"), text="Library management app").place(x=20,y=0)

def rndm():
	return str(datetime.datetime.now()).replace(" ","").replace("-","").replace(".","").replace(":","")

def removeBook():
	w=sd.askstring("Remove book","Enter book id")
	if w in os.listdir("books"):
		shutil.rmtree("books/"+w)
		msg.showinfo("Remove book","Book removed successfully")
	else:
		msg.showerror("Remove book","Book is not available")

def removeMember():
	w=sd.askstring("Remove member","Enter member id")
	if w in os.listdir("members"):
		shutil.rmtree("members/"+w)
		msg.showinfo("Remove member","Member removed successfully")
	else:
		msg.showerror("Remove member","Member not found")

def addMember():
	gtk1=Tk()
	gtk1.title("Add member")
	gtk1.geometry("600x200")
	Label(gtk1, height="200", width="2000", background="green").place(x=0,y=0)
	Label(gtk1, text="Enter name", font=("Bahnschrift","15"), background="green").place(x=20,y=20)
	Label(gtk1, text="Enter phone number", font=("Bahnschrift","15"), background="green").place(x=20,y=70)
	def addMemberFunc():
		e = rndm()
		os.mkdir("members/"+e)
		open("members/"+e+"/name","a").write(w[0].get())
		open("members/"+e+"/phone","a").write(w[1].get())
		open("members/"+e+"/book","a").write("0")
		msg.showinfo("Add member",f"Member added successfully. The id of member added is {e}.")
		gtk1.destroy()
	Button(gtk1, text="Create member", font=("Bahnschrift","15"), command=addMemberFunc).place(x=20,y=130)
	w = [Entry(gtk1, bd=3, font=("Bahnschrift","15")),Entry(gtk1, bd=3, font=("Bahnschrift","15"))]
	w[0].place(x=230, y=20)
	w[1].place(x=230, y=70)
	gtk1.mainloop()

def addBook():
	gtk2=Tk()
	gtk2.title("Add book")
	gtk2.geometry("600x200")
	Label(gtk2, height="200", width="2000", background="green").place(x=0,y=0)
	Label(gtk2, text="Enter name", font=("Bahnschrift","15"), background="green").place(x=20,y=20)
	Label(gtk2, text="Enter author", font=("Bahnschrift","15"), background="green").place(x=20,y=70)
	def addBookFunc():
		e = rndm()
		os.mkdir("books/"+e)
		open("books/"+e+"/name","a").write(w[0].get())
		open("books/"+e+"/author","a").write(w[1].get())
		open("books/"+e+"/available","a").write("0")
		msg.showinfo("Add book",f"Book added successfully. The id of book added is {e}.")
		gtk2.destroy()
	w = [Entry(gtk2, bd=3, font=("Bahnschrift","15")),Entry(gtk2, bd=3, font=("Bahnschrift","15"))]
	Button(gtk2, text="Create book", font=("Bahnschrift","15"), command=addBookFunc).place(x=20,y=130)
	w[0].place(x=230, y=20)
	w[1].place(x=230, y=70)
	gtk2.mainloop()

def removeDue():
	w=sd.askstring("Remove due","Enter id of member")
	if (w in os.listdir("members")):
		book_id=open("members/"+w+"/book","r").read().split("\n")[1]
		open("books/"+book_id+"/available","w").write("0")
		open("members/"+w+"/book","w").write("0")
		msg.showinfo("Remove due","Due removed successfully.")
	else:
		msg.showerror("Error","Member not found")

def getInfo():
	gtk3=Tk()
	gtk3.title("Info")
	gtk3.geometry("350x250")
	def instagram():
		webbrowser.open("http://instagram.com/abhineetraj1")
	def telegram():
		webbrowser.open("http://t.me/abhineetraj1")
	def github():
		webbrowser.open("http://github.com/abhineetraj1")
	Label(gtk3,background="purple", height="100", width="300").place(x=0,y=0)
	Label(gtk3,background="purple" ,text="This app is made by Abhineet Raj",foreground="white", font=("Bahnschrift","15")).place(x=0,y=0)
	Button(gtk3, text="Instagram", background="pink", foreground="black" ,font=("Bahnschrift","18"), command=instagram).place(x=10,y=50)
	Button(gtk3, text="Telegram", background="blue", foreground="white" ,font=("Bahnschrift","18"), command=telegram).place(x=10,y=110)
	Button(gtk3, text="Github", background="black", foreground="white" ,font=("Bahnschrift","18"), command=github).place(x=10,y=170)
	gtk3.mainloop()

def assignBook():
	gtk3=Tk()
	gtk3.title("Assign book")
	gtk3.geometry("600x200")
	Label(gtk3, height="200", width="2000", background="green").place(x=0,y=0)
	Label(gtk3, text="Enter member id", font=("Bahnschrift","15"), background="green").place(x=20,y=20)
	Label(gtk3, text="Enter book id", font=("Bahnschrift","15"), background="green").place(x=20,y=70)
	def assignBookFunc():
		e=[w[0].get(), w[1].get()]
		bln =[((w[0].get() in os.listdir("members")) , (w[1].get() in os.listdir("books")) , (open("books/"+e[1]+"/available","r").read() == "0") , (open("members/"+e[0]+"/book","r").read() == "0"))]
		if False not in bln:
			book_name=open("books/"+e[1]+"/name","r").read()
			open("members/"+e[0]+"/book","w").write(f"{book_name}\n{e[1]}")
			open("books/"+e[1]+"/available","w").write(e[0])
			msg.showinfo("Assign book","Book assigned successfully.")
			gtk3.destroy()
		else:
			msg.showerror("Error","Cannot assign book")
	w = [Entry(gtk3, bd=3, font=("Bahnschrift","15")),Entry(gtk3, bd=3, font=("Bahnschrift","15"))]
	Button(gtk3, text="Create book", font=("Bahnschrift","15"), command=assignBookFunc).place(x=20,y=130)
	w[0].place(x=230, y=20)
	w[1].place(x=230, y=70)
	gtk3.mainloop()

def listBooks():
	gtk4 = Tk()
	gtk4.title("Books")
	gtk4.geometry("700x600+0+0")
	lb = os.listdir("books")
	dfk=[0,9]
	def prev():
		if (dfk[0] < 9) == False:
			dfk[0]=dfk[0]-9
			dfk[1]=dfk[1]-9
			listBks()
	def prec():
		dfk[0]=dfk[0]+9
		dfk[1]=dfk[1]+9
		listBks()
	def listBks():
		y_l = [10,60,110,160,210,260,310,360,410,460,510]
		Label(gtk4,background="black", height="500", width="1000").place(x=0,y=0)
		if (len(lb) < dfk[1]):
			for i in range(dfk[0],len(lb)):
				if (open("books/"+lb[i]+"/available","r").read() == "0"):
					gh="AV"
				else:
					gh="NA"
				text=lb[i] + "  " + gh + "  " + open("books/"+lb[i]+"/name","r").read()
				Label(gtk4, text=text, font=("Bahnschrift","18"), foreground="white", background="black").place(x=0,y=y_l[range(dfk[0],len(lb)).index(i)])
			if dfk[0] > 0:
				Button(gtk4,text="Back", font=("Bahnschrift","18"), foreground="white", background="green", command=prev).place(x=120,y=510)
		else:
			for i in range(dfk[0],dfk[1]):
				if (open("books/"+lb[i]+"/available","r").read() == "0"):
					gh="AV"
				else:
					gh="NA"
				text=lb[i] + "  " + gh + "  " + open("books/"+lb[i]+"/name","r").read()
				Label(gtk4, text=text, font=("Bahnschrift","18"), foreground="white", background="black").place(x=0,y=y_l[range(dfk[0],dfk[1]).index(i)])
			if dfk[0] > 0:
				Button(gtk4,text="Back", font=("Bahnschrift","18"), foreground="white", background="green", command=prev).place(x=120,y=510)
			Button(gtk4,text="Next", font=("Bahnschrift","18"), foreground="white", background="green", command=prec).place(x=300,y=510)
	listBks()
	gtk4.mainloop()


def listMembers():
	gtk5 = Tk()
	gtk5.title("Books")
	gtk5.geometry("700x600+0+0")
	lb = os.listdir("members")
	dfk=[0,9]
	def prev():
		if (dfk[0] < 9) == False:
			dfk[0]=dfk[0]-9
			dfk[1]=dfk[1]-9
			listMbr()
	def prec():
		dfk[0]=dfk[0]+9
		dfk[1]=dfk[1]+9
		listMbr()
	def listMbr():
		y_l = [10,60,110,160,210,260,310,360,410,460,510]
		Label(gtk5,background="black", height="500", width="1000").place(x=0,y=0)
		if (len(lb) < dfk[1]):
			for i in range(dfk[0],len(lb)):
				if (open("members/"+lb[i]+"/book","r").read() == "0"):
					gh="AV"
				else:
					gh="NA"
				text=lb[i] + "  " + gh + "  " + open("members/"+lb[i]+"/name","r").read() + "  " + open("members/"+lb[i]+"/phone","r").read()
				Label(gtk5, text=text, font=("Bahnschrift","18"), foreground="white", background="black").place(x=0,y=y_l[range(dfk[0],len(lb)).index(i)])
			if dfk[0] > 0:
				Button(gtk5,text="Back", font=("Bahnschrift","18"), foreground="white", background="green", command=prev).place(x=120,y=510)
		else:
			for i in range(dfk[0],dfk[1]):
				if (open("members/"+lb[i]+"/book","r").read() == "0"):
					gh="AV"
				else:
					gh="NA"
				text=lb[i] + "  " + gh + "  " + open("members/"+lb[i]+"/name","r").read() + "  " + open("members/"+lb[i]+"/phone","r").read()
				Label(gtk5, text=text, font=("Bahnschrift","18"), foreground="white", background="black").place(x=0,y=y_l[range(dfk[0],dfk[1]).index(i)])
			if dfk[0] > 0:
				Button(gtk5,text="Back", font=("Bahnschrift","18"), foreground="white", background="green", command=prev).place(x=120,y=510)
			Button(gtk5,text="Next", font=("Bahnschrift","18"), foreground="white", background="green", command=prec).place(x=300,y=510)
	listMbr()
	gtk5.mainloop()

Button(top, text="Add member", background="green", foreground="white", font=("Bahnschrift","15"), command=addMember).place(x=20,y=50)
Button(top, text="Add book", background="green", foreground="white", font=("Bahnschrift","15"), command=addBook).place(x=20,y=110)
Button(top, text="Assign book", background="green", foreground="white", font=("Bahnschrift","15"), command=assignBook).place(x=20,y=170)
Button(top, text="Remove member", background="green", foreground="white", font=("Bahnschrift","15"), command=removeMember).place(x=320,y=50)
Button(top, text="Remove book", background="green", foreground="white", font=("Bahnschrift","15"), command=removeBook).place(x=320,y=110)
Button(top, text="Get info", background="green", foreground="white", font=("Bahnschrift","15"), command=getInfo).place(x=320,y=170)
Button(top, text="List members", background="green", foreground="white", font=("Bahnschrift","15"),command=listMembers).place(x=20,y=230)
Button(top, text="List books", background="green", foreground="white", font=("Bahnschrift","15"),command=listBooks).place(x=320,y=230)
Button(top, text="Remove due", background="green", foreground="white", font=("Bahnschrift","15"), command=removeDue).place(x=20,y=290)

top.mainloop()