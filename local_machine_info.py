import socket

def print_machine_info(): 
	host_name = socket.gethostname()
	print "Host name: %s" %host_name
	print "IP address: %s" %socket.gethostbyname(host_name)

if __name__ == '__main__':
	print_machine_info()
