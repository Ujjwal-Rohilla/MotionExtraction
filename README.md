# Motion Extraction
A python program that only shows the moving objects in your webcam. Originally inspired by [Posy](https://www.youtube.com/watch?v=NSS6yAMZF78)'s youtube video on this. 
![Motion Extraction of my... phone](https://github.com/user-attachments/assets/1d930c19-d08f-4531-ae40-0d3ca456bf71)

<sub> Motion Extraction of my phone while I was shaking it <sub/>

## What it do?
As the title suggests, it uses your webcam to basically 'extract motion' to show moving things. Posy beautifully explains it in his [video](https://www.youtube.com/watch?v=NSS6yAMZF78). Should check it out!

<sub> _Thought of making it in python while taking a shower lol._ <sub/>

## Installation
> [!NOTE]
> This assumes you already have Python 3

In your terminal/command prompt, type/paste the below line-by-line
```
git clone https://github.com/Ujjwal-Rohilla/MotionExtraction
cd MotionExtraction
pip install opencv-python
pip install numpy
cd '.\Motion Extraction'
python3 MotionExtraction.py
```

## Usage
> [!TIP]
> Keybinds to change settings of the program

| Key | What it does                                   | Notes
|-----|------------------------------------------------|------------------------------------------------------------------------------------------
|  Q  | Quit the Program                               | -
|  M  | Enable/Disable Motion Extracting               | -
|  R  | Change the Resolution in the format `[W]x[H]`  | Example: 640x480 or 1920x1080
|  F  | Change the FPS                                 | Your webcam _might_ change it by itself depending on the lighting, and the resolution set.

## Limitations
> [!WARNING]
> - Your WebCam might just not support a specific resolution, or a FPS. In that case the resolution might change but the FPS will probably stay the same
> - FPS might decrease if lighting is too low (to compensate for exposure/brightness) or if the FPS is not compatible with a resolution (like `1920x1080` and `120` FPS). All this depends on your WebCam

### To Do
- [X] Upload this Repo
- [ ] Add keybind `C` to change the camera source
  - [ ] \(Maybe) Allow user to see which number corresponds to which camera
- [ ] Add keybind `I` to save the current frame as an Image
- [ ] Pyinstaller's .exe doesn't work.. figure out how to fix that
