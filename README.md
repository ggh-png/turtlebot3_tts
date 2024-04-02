# turtlebot3_tts


## TTS Setting

---

### python pip Install

```bash
sudo apt install python3-pip 
```

### **TTS Install**

```bash
pip3 install gtts playsound
pip3 install pydub
```

### TB3  TTS  PKG Install

```bash
cd ~/ros2_ws/src
git clone https://github.com/ggh-png/turtlebot3_tts
```

### Build

```bash
cd ~/ros2_ws
colcon build --symlink-install
```


### TTS launch

```bash
ros2 run turtlebot3_tts tts_server 
```

### Call TTS Service

```bash
ros2 service call /turtlebot3/tts turtlebot3_interfaces/srv/TTS "tts_str_t: '안녕'" 
```