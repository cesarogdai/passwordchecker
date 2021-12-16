from tkinter import *
import requests
import hashlib
import sys

window = Tk()
window.title("Bienvenido")
window.geometry('500x200')
lbl = Label(window, text="Verifica tu contraseña")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)


btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/'+query_char
	res = requests.get(url)
	if res.status_code !=200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check api try again')
	return res




#split lines by : tuples
def  get_password_leaks(hashes, hash_to_check):
	hashes = (line.split(':')for line in hashes.text.splitlines())
	#h = hashes
	#count = what is after the :
	for h,count in hashes:
		if h == hash_to_check:
			return count
	return 0
#once it sees return it exits the function








#HASH module python
def pwned_api_check(password):
	#print(password.encode('utf-8'))

	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
						#0 to five characters  5 to rest of the characters
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char)
	
	return get_password_leaks(response,tail)


def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f'{password} se encontro {count} veces, deberias cambiar tu contraseña')
		else:
			print(f'{password} no se encontro. Todo bien')
	return 'done'	












if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
