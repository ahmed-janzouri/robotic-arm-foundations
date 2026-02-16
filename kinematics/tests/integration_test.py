import sys
import os
import math
import random
# --- SETUP PATHS ---
# 1. Get the current file's directory (kinematics/tests)
current_dir = os.path.dirname(os.path.abspath(__file__))
# 2. Go up TWO levels to reach the project root (ROBOTIC-ARM-FOUNDATIONS)
root_dir = os.path.join(current_dir, '..', '..')
# 3. Add to system path
sys.path.append(os.path.abspath(root_dir))

from kinematics.forward import RobotArm2D
from kinematics.inverse import InverseKinematics

def run_golden_test():
    # 1. Initialize Both Engines (Links = 10, 10)
    L1 = 10.0
    L2 = 10.0
    fk_engine = RobotArm2D(L1, L2)
    ik_engine = InverseKinematics(L1, L2)

    print("🤖 SYSTEM INTEGRATION TEST ONLINE")
    print("------------------------------------------------")

    # 2. Run 5 Random Test Cases
    # We restrict angles to 0-90 to avoid "Elbow Up vs Down" ambiguity for now
    for i in range(1, 6):
        print(f"\n[Test Case {i}]")
        
        # A. Generate Random Input Angles
        t1_input = random.uniform(10, 80)
        t2_input = random.uniform(10, 80)
        print(f"   Input Angles:  Theta1={t1_input:.2f}°, Theta2={t2_input:.2f}°")

        # B. Run FORWARD Kinematics
        fk_result = fk_engine.compute_forward_kinematics(t1_input, t2_input)
        hand_pos = fk_result['hand']
        print(f"   Forward Result: x={hand_pos[0]:.2f}, y={hand_pos[1]:.2f}")

        # C. Run INVERSE Kinematics
        ik_result = ik_engine.compute_angles(hand_pos[0], hand_pos[1])
        
        if ik_result is None:
            print("   ❌ FAIL: IK returned None (Unreachable?)")
            continue

        t1_output = ik_result['theta1']
        t2_output = ik_result['theta2']
        print(f"   Inverse Result: Theta1={t1_output:.2f}°, Theta2={t2_output:.2f}°")

        # D. Compare (The Moment of Truth)
        # We allow a small error margin (0.1 degrees) because of floating point math
        error_1 = abs(t1_input - t1_output)
        error_2 = abs(t2_input - t2_output)

        if error_1 < 0.1 and error_2 < 0.1:
            print("   ✅ PASS: Perfect Match")
        else:
            print(f"   ⚠️ VARIANCE DETECTED (Diff: {error_1:.4f}, {error_2:.4f})")
            print("   (Note: This might be 'Elbow Up' vs 'Elbow Down' configuration)")

if __name__ == "__main__":
    run_golden_test()