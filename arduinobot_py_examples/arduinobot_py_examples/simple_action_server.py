import rclpy
import time
from rclpy.node import Node
from rclpy.action import ActionServer
from arduinobot_msgs.action import Fibonacci

class SimpleActionServer(Node):
    def __init__(self):
        super().__init__('simple_action_server')
        self.action_server = ActionServer(self, Fibonacci, "fibonacci", self.goalCallback)
        self.get_logger().info("Action server started")
        
    def goalCallback(self, goal_handle):
        self.get_logger().info("Goal received with order %d" %goal_handle.request.order)
        feedback_msg = Fibonacci.Feedback()
        feedback_msg.partial_sequence = [0, 1]
        
        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequence.append(feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])
            self.get_logger().info("Feedback: {0}".format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)
            
        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = feedback_msg.partial_sequence
        return result
  
def main():
    rclpy.init()
    simple_action_server = SimpleActionServer()
    rclpy.spin(simple_action_server)
    simple_action_server.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()