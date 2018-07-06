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
#For sqrt
import math

#Global vars :
kicadFile = ""
sizeX=10.0
sizeY=10.0
width=0.25
length=0
net=0
space=0.5
layer="F.Cu"

def Help(out):
	print os.path.basename(__file__) +' -x <size of X> -y <size of Y> -w <size of width> -l <name of layer> -n <number of net> -s <space between wires>'
	print("All options are optionnal, default is size X=10mm, Y=10mm, width=0.25mm, net=0, space=0.5mm, layer=F.Cu")
	print("Example : '"+os.path.basename(__file__) +" -x 10.0 -y 20.5'")
	print("  will create a sample of track resistor heater (10×20.5mm²)")
	print("  called test.kicad_pcb in the current folder,")
	print("  which needs to be included in a .kicad_pcb file.")
	sys.exit(out)

def setCoord(x1, y1, x2, y2):
	global length
	kicadFile.write("\n  (segment (start "+str(x1)+" "+str(y1)+") (end "+str(x2)+" "+str(y2)+") (width "+str(width)+") (layer "+str(layer)+") (net "+str(net)+"))")
	length+=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
	return

def main(argv):
	global sizeX
	global sizeY
	global width
	global length
	global net
	global space
	global layer
	global kicadFile
	try:
		opts, args = getopt.getopt(argv,"hx:y:X:Y:w:W:n:N:s:S:l:L",["help=", "width", "net", "space", "layer"])
	except getopt.GetoptError:
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
		elif opt in ("-w", "-W", "--width"):
			try:
				width = float(arg)
			except:
				Help(2)
		elif opt in ("-s", "-S", "--space"):
			try:
				space = float(arg)
			except:
				Help(2)
		elif opt in ("-n", "-N", "--net"):
			try:
				net = int(arg)
			except:
				Help(2)
		elif opt in ("-l", "-L", "--layer"):
			try:
				layer = arg
			except:
				Help(2)
		else:
			Help(0)
	print("Size of X="+str(sizeX)+"mm")
	print("Size of Y="+str(sizeY)+"mm")
	print("width of wire="+str(width)+"mm")
	print("Space between tracks="+str(space)+"mm")
	print("net number="+str(net))
	print("layer="+layer)
	
	#Create a new file kicad_pcb:
	kicadFile = open("test.kicad_pcb" , "w")

	for i in np.arange(0.0, sizeX, space):
		#Top Left to top right
		if i<space:
			setCoord(i, i, sizeX-i, i)
		elif i<2*space:
			setCoord(i-space, i, sizeX-i, i)
		else:
			setCoord(i-2*space, i, sizeX-i, i)
		if (i+1>space+sizeX/2 or i+1>space+sizeY/2):
			if sizeX<sizeY:
				setCoord(sizeX-i, i, i, sizeY-i)
				setCoord(i, sizeY-i, i-space, i-space+1)
			break
		#Top right to bottom right
		setCoord(sizeX-i, i, sizeX-i, sizeY-i)
		#Bottom right to bottom left
		setCoord(sizeX-i, sizeY-i, i, sizeY-i)
		#Bottom left to top left
		if (sizeY-i!=i+1):
			setCoord(i, sizeY-i, i, i+1)
		else:
			setCoord(i, sizeY-i, sizeX-i-space, i+space)
	
	return
	
	kicadFile.close()
	

if __name__ == "__main__":
	main(sys.argv[1:])
	print("---------------------------------------------")
	print("Size of heater = "+str(length)+"mm.")
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


