import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter

class simpleParameter(Node):
    def __init__(self):
        super().__init__('simpleParameter')
        self.declare_parameter("simple_int_param", 28)
        self.declare_parameter("simple_str_param", "Peter")

        self.add_on_set_parameters_callback(self.paramChangesCallback)

    def paramChangesCallback(self, params):
        result = SetParametersResult()

        for param in params:
            if param.name == "simple_int_param" and param.type_ == Parameter.Type.INTEGER:
                self.get_logger().info("Param simple_int_param changed! New value is %d" %param.value)
                result.successful = True
            if param.name == "simple_string_param" and param.type_ == Parameter.Type.STRING:
                self.get_logger().info("Param simple_string_param changed! New value is %s" %param.value)
                result.successful = True
        return result

def main():
    rclpy.init()
    simple_Parameter = simple_Parameter()
    rclpy.spin(simple_Parameter)
    simple_Parameter.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()