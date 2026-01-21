\# 24-Hour Alarm Clock (Python)



A Python-based 24-hour alarm clock that triggers an alarm at a user-specified \*\*date and time\*\* using the system clock.



The alarm:

\- Rings at the correct scheduled time

\- Stops automatically after 5 seconds \*\*OR\*\*

\- Stops immediately when the user presses any key

\- Exits the program cleanly (no background execution)



---



\## Features

\- 24-hour time format (HH:MM:SS)

\- Date + time based alarm

\- CPU-efficient (checks time once per second)

\- Universal alarm sound (no external audio file required)

\- Clean program termination



---



\## How It Works

1\. User enters a date and time

2\. Program continuously checks system time

3\. When the alarm time is reached:

&nbsp;  - Alarm sound starts

&nbsp;  - Alarm stops after 5 seconds \*\*or\*\* on key press

&nbsp;  - Program exits safely



---



\## Libraries Used

\- `datetime` – date and time handling

\- `time` – delays and time tracking

\- `threading` – concurrent alarm control

\- `sys` – terminal interaction

\- `winsound` (Windows only, optional) – system beep



---



\## How to Run

```bash

python main.py



