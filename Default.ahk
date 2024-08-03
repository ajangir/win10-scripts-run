#v::Run,cmd /c ""C:\Program Files (x86)\CopyQ\copyq.exe" toggle",,Hide
#c::Run,cmd /c ""C:\Program Files (x86)\CopyQ\copyq.exe" menu",,Hide
#n::WinMinimize, A
,
; Define a hotkey for Alt+D to download subtitles in smplayer semi-automatic way
!d::
    ; Press Alt+F
    SendInput, !f
    sleep, 2000 ; Sleep for 2 seconds

    SendInput, !{Tab}

    ; Click on specific pixel (adjust x, y coordinates as needed)

    Click
    sleep, 2000  ; Optional: small sleep before pressing Enter

    ; Press Enter key
    SendInput, {Enter}

	sleep, 1000
	SendInput, !{Tab}
	sleep, 500
	click , 1500,990
	Sleep, 2000  ; Sleep for 2 seconds
	SendInput, {PgDn}
return


;mouse switch to another screen, second monitor
#Space::
CoordMode, Mouse, Screen ; This is needed to assure that you get your mouse coordinates related to the screen, not to the window
MouseGetPos, MouseX, MouseY
if( MouseX > 1920) ; 1920x1080 of both monitors
{
MouseMove, 960, 540
}
else
{
MouseMove, A_ScreenWidth+960, 540
}
return

;Linux-like select and paste script
~lButton::
MouseGetPos, mousedrag_x, mousedrag_y
keywait lbutton, T0.3 
If (ErrorLevel)
{
	keywait lbutton
	mousegetpos, mousedrag_x2, mousedrag_y2
	if (abs(mousedrag_x2 - mousedrag_x) > mousedrag_threshold
	or abs(mousedrag_y2 - mousedrag_y) > mousedrag_threshold)
	{
		backup_clip := clipBoard
		sendinput ^c
		sleep, 100
		current_clip := clipBoard
		sleep, 50
		;Run,cmd /c ""C:\Program Files (x86)\CopyQ\copyq.exe" remove 0",,Hide
		clipBoard := backup_clip
	}
}
return
~lButton Up::return
!c::
SendInput, %current_clip%
return