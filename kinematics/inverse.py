import math

class InverseKinematics:
    """
    Geometric Inverse Kinematics Solver for a 2-Link Planar Arm.
    """
    def __init__(self, link_1: float, link_2: float):
        self.l1 = link_1
        self.l2 = link_2

    def compute_angles(self, target_x: float, target_y: float) -> dict:
        """
        Calculates joint angles (theta1, theta2) to reach (x, y).
        Returns None if unreachable.
        """
        # 1. Physics Check (Reachability)
        R = math.sqrt(target_x**2 + target_y**2)
        if R > (self.l1 + self.l2):
            return None # Target is out of reach

        try:
            # 2. Law of Cosines (Elbow Angle)
            # cos(gamma) = (a^2 + b^2 - c^2) / 2ab
            cos_gamma = (self.l1**2 + self.l2**2 - R**2) / (2 * self.l1 * self.l2)
            
            # Clamp value to handle floating point noise (e.g., 1.000000002)
            cos_gamma = max(-1.0, min(1.0, cos_gamma))
            
            gamma = math.acos(cos_gamma)
            theta2_rad = math.pi - gamma  # Elbow bending relative to straight arm

            # 3. Trigonometry (Shoulder Angle)
            # theta1 = atan2(y, x) - internal_angle_alpha
            phi = math.atan2(target_y, target_x)
            
            cos_alpha = (self.l1**2 + R**2 - self.l2**2) / (2 * self.l1 * R)
            cos_alpha = max(-1.0, min(1.0, cos_alpha))
            
            alpha = math.acos(cos_alpha)
            theta1_rad = phi - alpha

            return {
                "theta1": math.degrees(theta1_rad),
                "theta2": math.degrees(theta2_rad)
            }

        except ValueError:
            return None # Math domain error