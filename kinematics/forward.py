import math
import sys
import os

# Ensure we can find matrix_lib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import matrix_lib as core

class RobotArm2D:
    """
    A 2-Link Planar Robot Arm Kinematics Engine.
    """
    def __init__(self, link_1: float, link_2: float):
        self.l1 = link_1
        self.l2 = link_2

    def _get_transformation_matrix(self, theta_deg: float, length: float) -> list:
        """Generates a 3x3 Homogeneous Transformation Matrix."""
        theta_rad = math.radians(theta_deg)
        c = math.cos(theta_rad)
        s = math.sin(theta_rad)
        
        return [
            [c, -s, length * c],
            [s,  c, length * s],
            [0,  0, 1]
        ]

    def compute_forward_kinematics(self, theta1: float, theta2: float) -> dict:
        """
        Calculates the (x, y) position of the Elbow and Hand.
        Returns: {'elbow': (x, y), 'hand': (x, y)}
        """
        # 1. Base -> Elbow (Frame 0 to 1)
        T_01 = self._get_transformation_matrix(theta1, self.l1)
        
        # 2. Elbow -> Hand (Frame 1 to 2)
        T_12 = self._get_transformation_matrix(theta2, self.l2)
        
        # 3. Base -> Hand (Global Transformation)
        T_global = core.matrix_multiplication(T_01, T_12)
        
        return {
            "elbow": (T_01[0][2], T_01[1][2]),
            "hand":  (T_global[0][2], T_global[1][2])
        }