#Requires AutoHotkey >=2.0
#Warn

#n::WinMinimize "A"
^q::send "!{f4}"

!v::SendEvent '{Text}' A_Clipboard
#v::Run 'cmd /c ""C:\Program Files (x86)\CopyQ\copyq.exe" toggle"',"", "Hide"
#c::Run 'cmd /c ""C:\Program Files (x86)\CopyQ\copyq.exe" menu"',"", "Hide"

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

	sleep 2000
	if WinExist("SMPlayer")
		WinActivate
	
	click 1500,950
	Send "."
	MouseMove 800,500
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

; Hotkey definition kill tasks - process tree in task manager
!k::
{
    ; Check if Task Manager is the active window
    if WinActive("ahk_exe Taskmgr.exe")
    {
      Delay := 2000
      ; Get the currently focused control
      FocusedClassNN := ControlGetClassNN(ControlGetFocus("A"))
      ;MsgBox 'Control with focus ClassNN: ' FocusedClassNN
      
      ; Handling SysListView321 (Process List) kill process tree
      if (FocusedClassNN = "SysListView321")
      {
          ; Right-click, wait, press 't', wait, press Enter
          Sleep Delay
          Send "{RButton}"
          Sleep Delay
          Send "t"
          Sleep Delay
          Send "{Enter}"
      }
      
      ; Handling DirectUIHWND1 (Performance/App tabs)
      else if (FocusedClassNN = "DirectUIHWND1")
      {
          ; Right-click, short delay, press 'e'
          Send "{RButton}"
          Sleep Delay
          Send "e"
      }
    }
    return    
}

/*
global isKeyboardDisabled := 0


^!e::
{
    global isKeyboardDisabled := 1
    ShowTooltip("Keyboard Disabled (Press Esc to enable)")
}

; Hotkey to manually enable the keyboard using Ctrl+Alt+E
$Esc::
{
    global isKeyboardDisabled := 0
    ShowTooltip("Keyboard Enabled")
send "{Esc}"
}

; Function to show and auto-hide tooltips
ShowTooltip(message, duration := 3000)
{
    ToolTip(message)
    SetTimer () => ToolTip(), -duration
}

; Block inputs when keyboard is disabled
#HotIf (isKeyboardDisabled = 1)
{
*a::return
*b::return
*c::return
*d::return
*e::return
*f::return
*g::return
*h::return
*i::return
*j::return
*k::return
*l::return
*m::return
*n::return
*o::return
*p::return
*q::return
*r::return
*s::return
*t::return
*u::return
*v::return
*w::return
*x::return
*y::return
*z::return
*0::return
*1::return
*2::return
*3::return
*4::return
*5::return
*6::return
*7::return
*8::return
*9::return
*F1::return
*F2::return
*F3::return
*F4::return
*F5::return
*F6::return
*F7::return
*F8::return
*F9::return
*F10::return
*F11::return
*F12::return
*Space::return
*Tab::return
*Enter::return
*Backspace::return
*Delete::return
*Insert::return
*Home::return
*End::return
*PgUp::return
*PgDn::return
*Up::return
*Down::return
*Left::return
*Right::return
*NumpadAdd::return
*NumpadSub::return
*NumpadMult::return
*NumpadDiv::return
*NumpadDot::return
*Numpad0::return
*Numpad1::return
*Numpad2::return
*Numpad3::return
*Numpad4::return
*Numpad5::return
*Numpad6::return
*Numpad7::return
*Numpad8::return
*Numpad9::return
*`::return  ; Accent/tilde key
*\::return  ; Backslash
*[::return  ; Left bracket
*]::return  ; Right bracket
*;::return  ; Semicolon
*'::return  ; Apostrophe
*,::return  ; Comma
*.::return  ; Period
*-::return  ; Minus
*=::return  ; Equals
\*/::return  ; Slash
}
#HotIf

*/