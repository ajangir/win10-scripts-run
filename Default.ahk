#Requires AutoHotkey >=2.0
#Warn

#n::WinMinimize "A"

; Define a hotkey for Alt+D to downAltTabload subtitles in smplayer semi-automatic way
!d::{
    ; Press Alt+f
    Send "!f"
    sleep 1000 ; Sleep for 2 seconds

    if WinExist("Subtitles")
		WinActivate

    ; Click on specific pixel (adjust x, y coordinates as needed)

    sleep 2000  ; Optional: small sleep before pressing Enter
    Click
    ; Press Enter key
    Send "{Enter}"

	sleep 1000
	if WinExist("SMPlayer")
		WinActivate
	
	click 1500,950
	Sleep 2000  ; Sleep for 2 seconds
	Send "{PgDn}"
return
}


;mouse switch to another screen, second monitor
#Space::{
CoordMode "Mouse", "Screen" ; This is needed to assure that you get your mouse coordinates related to the screen, not to the window
MouseGetPos &MouseX, &MouseY
if( MouseX > 1920) ; 1920x1080 of both monitors
{
MouseMove 960, 540
}
else
{
MouseMove A_ScreenWidth+960, 540
}
return
}
