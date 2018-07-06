#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create kicad_pcb sample of a resistor heater.


import sys
#Used for args :
import getopt
#Used for get the script name:
import os
#Used to create an array
import numpy as np

def Help(out):
	print os.path.basename(__file__) +' -x <size of X> -y <size of Y>'
	print("Example : '"+os.path.basename(__file__) +" -x 10.0 -y 20.5'")
	print("  will create a sample of track resistor heater (10×20.5mm²)")
	print("  which needs to be included in a .kicad_pcb file.")
	sys.exit(out)

def main(argv):
	sizeX=10.0
	sizeY=10.0
	width=0.25
	length=0
	net=0
	space=0.5
	try:
		opts, args = getopt.getopt(argv,"hx:y:X:Y:l:L:w:W:n:N:",["help=", "length", "width", "net"])
		print("opts="+str(opts)+"len="+str(len(opts)))
		print("args="+str(args))
	except getopt.GetoptError:
		Help(2)
	if len(opts)!=2:
		#X and Y not parsed
		Help(2)
	for opt, arg in opts:
		if opt in ("-x", "-X"):
			try:
				sizeX = float(arg)
			except:
				Help(2)
		elif opt in ("-y", "-Y"):
			try:
				sizeY = float(arg)
			except:
				Help(2)
		elif opt in ("-l", "-L", "--length"):
			try:
				length = float(arg)
			except:
				Help(2)
		elif opt in ("-w", "-W", "--width"):
			try:
				width = float(arg)
			except:
				Help(2)
		elif opt in ("-n", "-N", "--net"):
			try:
				net = int(arg)
			except:
				Help(2)
		else:
			Help(0)
	print("X="+str(sizeX)+"mm")
	print("Y="+str(sizeY)+"mm")
	print("length="+str(length))
	print("width="+str(width))
	print("Space="+str(space))
	print("net="+str(net))
	print("layer=F.Cu")
	
	#Create a new file kicad_pcb:
	kicadFile = open("test.kicad_pcb" , "w")

	for i in np.arange(0.0, sizeX, width):
		#Top Left to top right
		print("(start "+str(0+2*i-2*width)+" "+str(0+2*i)+") (end "+str(sizeX-2*i)+" "+str(0+2*i)+")")
		kicadFile.write("\n  (segment (start "+str(0+2*i-4*width)+" "+str(0+2*i)+") (end "+str(sizeX-2*i)+" "+str(0+2*i)+") (width 0.25) (layer F.Cu) (net 0))")
		if (2*i+1>2*width+sizeX/2):
			print("(start "+str(sizeX-2*i)+" "+str(0+2*i)+") (end "+str(2*i)+" "+str(sizeY-2*i)+")")
			kicadFile.write("\n  (segment (start "+str(sizeX-2*i)+" "+str(0+2*i)+") (end "+str(2*i)+" "+str(sizeY-2*i)+") (width 0.25) (layer F.Cu) (net 0))")
			break
		#Top right to bottom right
		print("(start "+str(sizeX-2*i)+" "+str(2*i)+") (end "+str(sizeX-2*i)+" "+str(sizeY-2*i)+")")
		kicadFile.write("\n  (segment (start "+str(sizeX-2*i)+" "+str(2*i)+") (end "+str(sizeX-2*i)+" "+str(sizeY-2*i)+") (width 0.25) (layer F.Cu) (net 0))")
		#Bottom right to bottom left
		print("(start "+str(sizeX-2*i)+" "+str(sizeY-2*i)+") (end "+str(2*i)+" "+str(sizeY-2*i)+")")
		kicadFile.write("\n  (segment (start "+str(sizeX-2*i)+" "+str(sizeY-2*i)+") (end "+str(2*i)+" "+str(sizeY-2*i)+") (width 0.25) (layer F.Cu) (net 0))")
		#Bottom left to top left
		print("(start "+str(2*i)+" "+str(sizeY-2*i)+") (end "+str(2*i)+" "+str(2*i+1)+")")
		kicadFile.write("\n  (segment (start "+str(2*i)+" "+str(sizeY-2*i)+") (end "+str(2*i)+" "+str(2*i+1)+") (width 0.25) (layer F.Cu) (net 0))")
	
	return
	
	kicadFile.close()
	

if __name__ == "__main__":
	main(sys.argv[1:])
	print("---------------------------------------------")
	print("End of "+os.path.basename(__file__))

# nb = raw_input("Nombre:")	#Demande nb
# nb = int(nb)
# R = [2,3,5]		#tableau de nb prem
# a = 0		#resultat
# while i<(nb):
	# a = pow(2,i)%(i+1)
	# print "nombre ", i+1, " . Module ", a
	# if a==1:
	#	 R.append(int(i+1))	#on stock i+1 dans R


