# Flow run : Init -> create pub -> callback -> spin

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Create a Node with name : simple_publisher
class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")

        # Create a Pub, send String to the topic /chatter
        self.pub_ = self.create_publisher(String, 'chatter', 10)
        self.counter_ = 0
        self.period_ = 1.0


        self.get_logger().info("Publishing at %d second " % self.period_)

        # Each 1 second call -> timerCallback
        self.timer_ = self.create_timer(self.period_, self.timerCallback)
    
    # When the timer run, return here
    def timerCallback(self):
        msg = String()
        msg.data = f" Hello world .This is a : {self.counter_} time" 
        self.pub_.publish(msg)
        self.counter_ += 1

def main():
    rclpy.init()
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown

if __name__ == '__main__':
    main()