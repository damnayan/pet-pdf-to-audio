# pet-pdf-to-audio
The PDF to Audio Converter is a Python application designed to transform PDF documents into spoken audio files. This tool leverages the PyPDF2 library to read PDF documents and the pyttsx3 library for converting text to speech. It's especially useful for visually impaired users, auditory learners, or anyone who needs to consume written content on the go.

Key Features:

PDF Text Extraction: Efficiently reads and extracts text from any PDF file using PyPDF2.
Audio Conversion: Converts the extracted text into spoken audio, allowing users to listen to the content of PDF documents.
Customizable Audio Output: Utilizes the pyttsx3 library, which supports changing voice properties such as speech rate and volume.
File Handling: Generates an audio file from the PDF text, saving it conveniently as an MP3 file for easy playback on various devices.
Technologies Used:

Python 3.x
Libraries: PyPDF2, pyttsx3
How to Use:

Ensure Python and the required libraries (PyPDF2, pyttsx3) are installed on your system.
Place the Python script and the PDF file in the same directory.
Run the script. The PDF file will be read, and its content will be converted into an audio file named story.mp3.
