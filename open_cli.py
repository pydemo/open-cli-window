import win32gui
import win32process
from subprocess import Popen, CREATE_NEW_CONSOLE

def get_hwnds_for_pid ( pid):
	def callback (hwnd, hwnds):
		if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
			_, found_pid = win32process.GetWindowThreadProcessId (hwnd)
			if found_pid == pid:
				hwnds.append (hwnd)
		return True

	hwnds = []
	win32gui.EnumWindows (callback, hwnds)
	#print hwnds
	return hwnds
def open_CLI(title, pos):
	if 1:
		p = Popen(["cmd.exe"],  creationflags=CREATE_NEW_CONSOLE)
		


	if 1:
		if 1:
			hwnd=None
			while not hwnd:
				hwnd=get_hwnds_for_pid(p.pid)
				#print (hwnd)
			assert hwnd
			win=hwnd[0]
			#print(window1)
			if 0:
				(x,y) = win.GetScreenPosition()
				print('GetScreenPosition: ', x,y)
				(l,w) =win.GetClientSize()
				print ('GetClientSize: ',l,w)
				dl,dw= win.GetSize()
				print ('GetSize:', dl,dw)
			if 1:
				win32gui.SetWindowText(win, title)
				win32gui.SetForegroundWindow(win)
				
				win32gui.MoveWindow(win,*pos , True)	
				
if __name__=='__main__':
	pos=[150, 100, 12000, 800]
	for i in range(1,6):
		posi= pos
		posi[0:2]=[150+i*50, 100+i*50]
		open_CLI(title= 'Test CLI #{}'.format(i), pos=posi)
			
