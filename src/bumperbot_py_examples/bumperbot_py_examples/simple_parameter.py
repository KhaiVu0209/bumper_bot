import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter

class SimpleParameter(Node):
    def __init__(self):
        super().__init__("simple_parameter")

        self.declare_parameter("int_param", 10)
        self.declare_parameter("string_param", "Khai_Vu_handsome")

        self.add_on_set_parameters_callback(self.paramChangeCallback) #Moi khi parameter bi thay doi thi ham nay se call den ham ben trong 

    def paramChangeCallback(self, params):
        result = SetParametersResult()

        for param in params:
            if param.name == "int_param" and param.type == Parameter.Type.INTEGER:
                self.get_logger().info(f"Param int changed . New valu e is {param.vale}")
                result.successful = True
            
            if param.name =="string_param" and param.type == Parameter.Type.STRING:
                self.get_logger().info(f"Param string changed . New value is {param.value}")   
                result.successful = True

def main():
    rclpy.init()
    simple_parameter = SimpleParameter()
    rclpy.spin(simple_parameter)
    simple_parameter.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
