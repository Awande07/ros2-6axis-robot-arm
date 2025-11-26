#!/usr/bin/env python3
# This shebang line tells the system this is a Python 3 script.

# Import the ROS 2 client library for Python
import rclpy
# Import the Node class from rclpy
from rclpy.node import Node
# Import the String message type from the std_msgs package
from std_msgs.msg import String

# Create a class that inherits from the Node class
class MyFirstNode(Node):

    def __init__(self):
        # Initialize the parent (Node) class with the node name: 'my_first_node'
        super().__init__('my_first_node')
        
        # Create a Publisher.
        # This node will publish messages of type String on the topic 'my_topic'.
        # The '10' is the queue size, which limits the number of outgoing messages if subscribers are slow.
        self.publisher_ = self.create_publisher(String, 'greetings', 10)
        
        # Create a timer. This will call the 'timer_callback' function every 0.5 seconds.
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # Initialize a counter to track how many messages we've sent
        self.i = 0

    def timer_callback(self):
        # This function is called every time the timer period elapses.
        
        # Create a new String message object
        msg = String()
        # Set the message data to a string
        msg.data = 'My awesome node is talking! Count: %d' % self.i
        
        # Publish the message to the topic
        self.publisher_.publish(msg)
        
        # Log a message to the console, for debugging and monitoring
        self.get_logger().info('Publishing: "%s"' % msg.data)
        
        # Increment the counter
        self.i += 1

# The main function: the entry point of this Python script
def main(args=None):
    # Initialize the ROS 2 communication library
    rclpy.init(args=args)
    
    # Create an instance of our node class
    my_first_node = MyFirstNode()
    
    # 'spin' keeps the node running and processes callbacks (like timer_callback)
    try:
        rclpy.spin(my_first_node)
    except KeyboardInterrupt:
        # This block runs if you press Ctrl+C to stop the node
        pass
    finally:
        # Clean up and shut down gracefully
        my_first_node.destroy_node()
        rclpy.shutdown()

# This standard Python check ensures main() only runs if this file is executed directly,
# not if it's imported as a module by another file.
if __name__ == '__main__':
    main()