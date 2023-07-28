#NoEnv
#SingleInstance, Force
#Persistent
SendMode, Input
SetTitleMatchMode Fast
ListLines, Off
Process, Priority, , High
SetWorkingDir %A_ScriptDir%                   

*y::
	Send, {ENTER DOWN}
	Sleep, 1
	Send, {ENTER UP}