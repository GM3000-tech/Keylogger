# Enhanced Python Keylogger with Timestamped Logs

This version of the keylogger improves on the barebones script by creating a **new log file for each run**, labeled with a timestamp.

## What’s New?

- Each time the script runs, it creates a log file named like:  
  `keylog_YYYY-MM-DD_HH-MM-SS.txt`  
  For example: `keylog_2025-08-04_21-00-00.txt`
- This helps keep logs organized and separated by session.

## How to Run

1. Ensure Python 3.x is installed  
2. Install dependencies: `pip install pynput`  
3. Run the script: `python keylogger.py`  
4. Stop logging by pressing the **ESC** key  
5. Check your directory for a newly created log file with a timestamped name

## Legal & Ethical Notice

Use responsibly and only on devices you own or have explicit permission to monitor.

## Future Directions

- Adding encryption to log files  
- Improving stealth capabilities  
- Packaging as an executable for easier use  
- Extending input capture to mouse and clipboard events

---

*Created by Gaurang Mishra*  
gmishra3000b@gmail.com
