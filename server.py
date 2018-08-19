import socket, time, random, threading,sys, tkinter, subprocess,platform
from  tkinter import messagebox
from requests import get



#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = random.randint(500,20000)




def send(Entry=0):
	global cs
	j = SendEntry.get()
	cs.send(j.encode('utf-8'))
	Label(0,j)
	SendEntry.delete(0,len(j))

def receive():
	global cs
	while True:
			data = cs.recv(1024)
			if data:
				Label(0,data.decode('utf-8'))

def Connection():
	R1.config(state='disabled')
	R2.config(state='disabled')
	RadioPick.config(state = 'disabled')
	SendEntry.config(state='normal')
	SendEntry.delete(0,'end')
	SendEntry.insert(0,"Waiting for someone to connect")
	SendEntry.config(state='disabled')
	T_SB = threading.Thread(target=SocketyBuckety)
	T_SB.start()

def SocketyBuckety():
	global LorP,LIP,PIP,port,s
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	if LorP == 0:
		s.bind((LIP,port))
		print("Port {0} has been binded at {1}".format(port,LIP))
	elif LorP == 1:
		s.bind((PIP,port))
		print("Port {0} has been binded at {1}".format(port,LIP))
	T_Listen = threading.Thread(target=Listen)
	T_Listen.start()


def Listen():
	global s,cs,address
	print("Listening...")
	s.listen(1)
	cs, address = s.accept()
	print("Someone accepted")
	SendEntry.config(state='normal')
	SendEntry.delete(0,'end')
	Label(0,"{0} is now connected.".format(address[0]))
	SendButton.config(state='normal')
	T_Receive = threading.Thread(target=receive)
	T_Receive.start()




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

top.bind('<Return>', send)


PortLabel = tkinter.Label(top,text="Port: {0}".format(port))
PortLabel.place(x = 210, y = 10)


PIP = get('https://api.ipify.org').text
PublicIPLabel = tkinter.Label(top,text="Public IP: {0}".format(PIP))
PublicIPLabel.place(x = 295, y = 30)


def get_ip():
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	try:
		s.connect(('10.255.255.255',1))
		IP= s.getsockname()[0]
	except:
		IP='127.0.0.1'
	finally:
		s.close()
	return IP

LIP = get_ip()
LocalIPLabel = tkinter.Label(top,text="Local IP: {0}".format(LIP))
LocalIPLabel.place(x = 295, y = 10)


SendButton = tkinter.Button(top,text="Send",command=send, width=5, height=1,relief='groove')
SendButton.place(x = 355, y = 400)
SendButton.config(state='disabled')

SendEntry = tkinter.Entry(top,justify='left',relief='flat',width=48)
SendEntry.place(x = 50 , y= 403)
SendEntry.insert(1,"Waiting for you to press connect")
SendEntry.config(state='disabled')

LorP = 0
R1 = tkinter.Radiobutton(top, variable = LorP, value = 0)
R1.place(x=271,y=10)

R2 = tkinter.Radiobutton(top, variable = LorP, value = 1)
R2.place(x=271,y=30)


RadioPick = tkinter.Button(top, text = "Connect", command= Connection,width=8,height=1,relief='groove')
RadioPick.place(x=350,y=50)


MainText = tkinter.Text(top,relief='flat',height=20,width=36)
MainText.place(x=50,y=62)
MainText.config(state='normal')
for i in range(1,20):
	MainText.insert(str(float(i)),'\n')
MainText.config(state='disabled')
Before = ['\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n']

checkIPP = [0,0]



top.mainloop()
