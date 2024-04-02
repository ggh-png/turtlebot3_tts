#!/usr/bin/env python3

from gtts import gTTS
from playsound import playsound

import rclpy
from rclpy.node import Node
from turtlebot3_interfaces.srv import TTS
import tempfile

class SpeakTTS(Node):
    def __init__(self):
        super().__init__("turtlebot3_tts")

        self.srv = self.create_service(TTS, '/turtlebot3/tts', self.callback_service)
        self.get_logger().info("TTS Service is ready.")

    def callback_service(self, request, response):
        self.get_logger().info(f"Received request for TTS: '{request.tts_str_t}'")

        # TTS 처리
        try:
            tts = gTTS(text=request.tts_str_t, lang='ko')
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
                temp_file_name = temp_file.name
                tts.save(temp_file_name)
            
            playsound(temp_file_name)

            response.success = True
            self.get_logger().info("TTS processing completed successfully.")
        except Exception as e:
            response.success = False
            self.get_logger().error(f"Error in TTS processing: {str(e)}")

        return response


def main(args=None):
    rclpy.init(args=args)

    tts_node = SpeakTTS()

    rclpy.spin(tts_node)

    tts_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()