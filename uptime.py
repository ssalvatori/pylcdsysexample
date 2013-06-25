"""show uptime"""

import sys
from pylcdsysinfo import LCDSysInfo, TextLines, TextLines, BackgroundColours, TextColours
from datetime import timedelta


def getUptime():
	with open('/proc/uptime', 'r') as f:
	    uptime_seconds = float(f.readline().split()[0])
	    uptime_string = str(timedelta(seconds = uptime_seconds))
	return uptime_string

def main():
	uptime = getUptime()

	bg = BackgroundColours.BLACK
	fb = TextColours.WHITE

	
	d = LCDSysInfo()
	d.clear_lines(TextLines.ALL, bg)
	d.dim_when_idle(False)
	d.set_brightness(127)
	d.save_brightness(127, 255)
	d.set_text_background_colour(bg)

	d.display_text_on_line(3, "Uptime:", False, None, fb)
	d.display_text_on_line(4, uptime, False, None, fb)



if __name__ == "__main__":
    main()

