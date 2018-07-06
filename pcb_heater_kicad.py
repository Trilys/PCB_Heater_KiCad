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

def setCoord(x1, y1, x2, y2, width, layer, net, length):
	kicadFile.write("\n  (segment (start "+str(x1)+" "+str(y1)+") (end "+str(x2)+" "+str(y2)+") (width "+str(width)+") (layer "+str(layer)+") (net "+str(net)+"))")
	length+=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
	return

def main(argv):
	sizeX=10.0
	sizeY=10.0
	width=0.25
	length=0
	net=0
	space=0.5
	layer="F.Cu"
	try:
		opts, args = getopt.getopt(argv,"hx:y:X:Y:w:W:n:N:s:S:l:L",["help=", "width", "net", "space", "layer"])
		print("opts="+str(opts)+"len="+str(len(opts)))
		print("args="+str(args))
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
	print("X="+str(sizeX)+"mm")
	print("Y="+str(sizeY)+"mm")
	print("length="+str(length)+"mm")
	print("width="+str(width)+"mm")
	print("Space="+str(space)+"mm")
	print("net="+str(net))
	print("layer="+layer)
	
	#Create a new file kicad_pcb:
	kicadFile = open("test.kicad_pcb" , "w")

	for i in np.arange(0.0, sizeX, space):
		#Top Left to top right
		kicadFile.write("\n  (segment (start "+str(i-2*space)+" "+str(i)+") (end "+str(sizeX-i)+" "+str(i)+") (width "+str(width)+") (layer F.Cu) (net 0))")
		length+=abs((sizeX-i)-(i-2*space))
		if (i+1>space+sizeX/2 or i+1>space+sizeY/2):
			if sizeX<sizeY:
				kicadFile.write("\n  (segment (start "+str(sizeX-i)+" "+str(i)+") (end "+str(i)+" "+str(sizeY-i)+") (width "+str(width)+") (layer F.Cu) (net 0))")
				length+=sqrt((sizeX-2*i)*(sizeX-2*i)+(sizeY-2*i)*(sizeY-2*i))
				kicadFile.write("\n  (segment (start "+str(i)+" "+str(sizeY-i)+") (end "+str(i-space)+" "+str(i-space+1)+") (width "+str(width)+") (layer F.Cu) (net 0))")
				length+=sqrt((sizeX-2*i)*(sizeX-2*i)+(sizeY-2*i)*(sizeY-2*i))
			break
		#Top right to bottom right
		kicadFile.write("\n  (segment (start "+str(sizeX-i)+" "+str(i)+") (end "+str(sizeX-i)+" "+str(sizeY-i)+") (width "+str(width)+") (layer F.Cu) (net 0))")
		#Bottom right to bottom left
		kicadFile.write("\n  (segment (start "+str(sizeX-i)+" "+str(sizeY-i)+") (end "+str(i)+" "+str(sizeY-i)+") (width "+str(width)+") (layer F.Cu) (net 0))")
		#Bottom left to top left
		if (sizeY-i!=i+1):
			kicadFile.write("\n  (segment (start "+str(i)+" "+str(sizeY-i)+") (end "+str(i)+" "+str(i+1)+") (width "+str(width)+") (layer F.Cu) (net 0))")
		else:
			kicadFile.write("\n  (segment (start "+str(i)+" "+str(sizeY-i)+") (end "+str(sizeX-i-space)+" "+str(i+space)+") (width "+str(width)+") (layer F.Cu) (net 0))")
	
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


