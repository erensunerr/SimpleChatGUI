import socket, time, random, threading,sys, tkinter, subprocess,platform
from  tkinter import messagebox
hostConnect = ""
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 0


#def ipParse():
#	if platform.system() == 'Windows':
#		x = subprocess.check_output(['ipconfig'])
#	else:
#		x = subprocess.check_output(['ifconfig'])


def send():
	j = SendEntry.get()
	s.send(j.encode('utf-8'))
	Label(0,j)
	SendEntry.delete(0,len(j))

def receive():
	global s, hostConnect
	while True:
			data = s.recv(1024)
			if data:
				Label(0,data.encode('utf-8'))

def reset():
	global port,IPtoConnect
	PortButton.config(state='normal')
	PortEntry.config(state='normal')
	PortEntry.delete(0,len(PortEntry.get()))
	IPButton.config(state='normal')
	IPEntry.config(state='normal')
	IPEntry.delete(0,len(IPEntry.get()))
	SendEntry.config(state='disabled')
	SendButton.config(state='disabled')
	port = 0
	IPtoConnect = ''
	checkIPP = [0,0]


def openConnection():
	global IPtoConnect,port
	T_IB = threading.Thread(target=IggyBiggy)
	T_IB.start()


def IggyBiggy():
	try:
		s.connect((IPtoConnect,port))
		T_Receive = threading.Thread(target=receive)
		T_Receive.start()
		SendEntry.config(state='normal')
		SendButton.config(state='normal')
		SendEntry.delete(0,'end')
	except:
		messagebox.showwarning("Connection Error","Can't Connect to {0}:{1}".format(IPtoConnect,port))
		reset()



def checkPortEntry():
	global port
	if len(PortEntry.get()) > 5 :
		messagebox.showwarning("Port Error","Length of port (5 max) is shorter than "+str(len(PortEntry.get())))
		PortEntry.delete(0,len(PortEntry.get()))
	else:
		try:
			port = int(PortEntry.get())
			PortButton.config(state='disabled')
			PortEntry.config(state='disabled')
			checkIPP[1] = 1
			if checkIPP[0] == 1:
				openConnection()
		except:
				messagebox.showwarning("Port Error", "Port number must be an integer")

def checkIPEntry():
	global IPtoConnect, checkIPP
	if  not("." in IPEntry.get()) :
		messagebox.showwarning("IP Error","IP Adresses must include dots")
		IPEntry.delete(0,len(PortEntry.get()))
	else:
		try:
			for i in IPEntry.get().split('.'):
				 int(i)
			IPtoConnect = IPEntry.get()
			IPEntry.config(state='disabled')
			IPButton.config(state='disabled')
			checkIPP[0] = 1
			if checkIPP[1] == 1:
				openConnection
		except Exception as e:
			messagebox.showwarning("Port Error","IP Adresses must include just dots and numbers")

def Label(event,x):
	global Before
	MainText.config(state='normal')
	print(Before)
	Before += [x+"\n"]
	Before.pop(0)
	print(Before)
	MainText.delete('1.0','end')
	MainText.insert('1.0',"".join(Before))
	MainText.config(state='disabled')


top = tkinter.Tk()
top.geometry("500x500")
top.title("Simple Chat")
top.resizable(False,False)

top.bind('<Return>', Label)

ResetButton = tkinter.Button(top,text="Reset",command=reset,width=6, height=1,relief='groove')
ResetButton.place(x=3,y=3)

PortLabel = tkinter.Label(top,text="Port: ")
PortLabel.place(x = 407, y = 10)

PortEntry = tkinter.Entry(top,justify='left',relief='flat',width=8)
PortEntry.place(x=440,y=12)

PortButton = tkinter.Button(top,text="Set Port",command=checkPortEntry, width=6, height=1,relief='groove')
PortButton.place(x = 440 , y = 35)

IPLabel = tkinter.Label(top,text="IP: ")
IPLabel.place(x = 305, y = 10)

IPEntry = tkinter.Entry(top,justify='left',relief='flat',width=13)
IPEntry.place(x=325,y=12)

IPButton = tkinter.Button(top,text="Set IP",command=checkIPEntry, width=6, height=1,relief='groove')
IPButton.place(x = 355 , y = 35)

SendButton = tkinter.Button(top,text="Send",command=send, width=5, height=1,relief='groove')
SendButton.place(x = 355, y = 400)
SendButton.config(state='disabled')

SendEntry = tkinter.Entry(top,justify='left',relief='flat',width=48)
SendEntry.place(x = 50 , y= 403)
SendEntry.insert(1,"Enter IP and Port, be Patient")
SendEntry.config(state='disabled')


MainText = tkinter.Text(top,relief='flat',height=20,width=36)
MainText.place(x=50,y=62)
MainText.config(state='normal')
for i in range(1,20):
	MainText.insert(str(float(i)),'\n')
MainText.config(state='disabled')
Before = ['\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n']

checkIPP = [0,0]

top.mainloop()
