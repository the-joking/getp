import sys
import shutting
import urllib2
import threading
import time
import os
def install(apk,repo):
	print '[*]initializing download to repository:%s and package: %s' % (repo,apk)
	print '[*]initializing in %s ' % (time.date())
	try:
		src = urllib2.urlopen(repo)
		source_code = src.read()
		for n in repo:
			a += 1
			if n == '/':
				repo.rstrip(repo[:a])
				a = 0
		filesrc = open(repo,'wb')
		filesrc.write(source_code)
		filesrc.close()		
		print '[$]download conclued'
	except:
		print '[!]fail to save te file in your computer'
		sys.exit(1)
def usage():
	print 'using:getp [commands] [pkgname]'
	print '-g            - install a package'
	print '-r            - remove a package'
	print '-u            - update packages'

def pros(pack):
	
	if nmap:
	elif metasploit:
	elif beef:
	elif vollalitily:
	elif bitwalker:
	elif wireshark:
	elif netcat:
	elif vega:
	elif angryip:
	elif tor:
	elif proxychains:
	elif backdoor-factory:
	elif javasnoop:
	elif hashcat:
	elif john-the-ripper:
	elif burpsuit:
	elif t50:
	elif aircracking-ng
	elif wget:
	elif git:
	elif maltego:
	elif dmitry:
	elif sqlmap:
	elif hydra:
	elif dradis:
	elif 
	elif
	elif
	elif
	elif
	elif
	elif
	elif
	elif
	elif
	elif
	elif
	elif
	elif
	
def main():
	
	if len(sys.argv[4]) > 0:
		usage()
	elif sys.argv[2] == '-g':
		pros('g',sys.argv[3])
	elif sys.argv[2] == '-r':
		pros('r',sys.argv[3])
	elif sys.argv[2] == '-u':
		pros('u',sys.argv[3])
	else:
		usage()
		sys.exit(1)
