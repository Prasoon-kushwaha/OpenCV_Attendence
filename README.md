# OpenCV Attendance System

## Overview
The OpenCV Attendance System is a desktop application that utilizes OpenCV and face recognition technology to manage student attendance. This system provides an efficient and modern approach to attendance taking, eliminating the need for manual processes and ensuring higher accuracy.

## Features
- **Face Recognition:** Uses OpenCV for detecting and recognizing faces.
- **Automatic Attendance Marking:** Automatically marks attendance when a student's face is recognized.
- **User-Friendly Interface:** Simple and intuitive GUI for ease of use.
- **Student Data Management:** Add and manage student details, including capturing their photos for recognition.
- **Attendance Records:** View and export attendance records for analysis.

## Prerequisites
- Python 3.x
- OpenCV library
- face_recognition library
- Tkinter library (usually included with Python installations)
- CSV module (included with Python standard library)

## Flow Diagram
<img src="/UI_Main/2.png" alt="Flow Diagram" width="400">

## User Interface
### Main UI
<img src="/UI_Main/1.png" alt="Main UI" width="600">

### Additional UI Screens
<img src="/UI_Main/3.png" alt="Screen 1" width="400"> <img src="/UI_Main/4.png" alt="Screen 2" width="400">

### With Camera Input
<img src="/UI_Main/5.png" alt="Camera Input" width="600">

### UI with Student Details
<img src="/UI_Main/5a.png" alt="Student Details" width="600">

### MySQL Database
<img src="/UI_Main/6.png" alt="Database" width="600">

### Email Alerts
<img src="/UI_Main/7.png" alt="Email Alerts" width="600">

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Prasoon-kushwaha/OpenCV_Attendence.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd OpenCV_Attendence
    ```
3. **Install the required libraries:**
    ```bash
    pip install opencv-python face_recognition
    ```
4. **Run the application:**
    ```bash
    python main.py
    ```

## Usage
1. **Launching the Application:**
   - Run `main.py` to start the application.
   - The main window will appear with options to manage attendance and student data.

2. **Managing Students:**
   - Add new students by entering their details and capturing their photos.
   - Update existing student records by selecting a student and modifying their details.

3. **Marking Attendance:**
   - The system will automatically detect and recognize faces, marking attendance for recognized students.
   - Ensure the camera is properly set up and positioned.

4. **Viewing Attendance Records:**
   - View attendance records by selecting a date range.
   - Export attendance data to a CSV file for further analysis.

## Project Structure
```
OpenCV_Attendence/
│
├── main.py # Entry point for the application
├── face_recognition.py # Module for face recognition
├── gui.py # Module for creating the GUI
├── student_management.py # Module for managing student data
├── attendance.py # Module for handling attendance
├── data/
│ ├── students.csv # CSV file storing student data
│ └── attendance.csv # CSV file storing attendance records
├── images/ # Directory storing student photos
└── README.md # Project README file
```

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments
- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)