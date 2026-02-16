import sys
from kinematics.inverse import InverseKinematics
from visualizer import plot_robot

def main():
    print("🤖 ROBOTIC ARM CONTROL SYSTEM V1.0")
    print("-----------------------------------")
    
    # 1. Setup Robot
    L1 = 10.0
    L2 = 10.0
    ik_solver = InverseKinematics(L1, L2)

    # 2. User Input
    try:
        x_input = float(input("Enter Target X: "))
        y_input = float(input("Enter Target Y: "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers.")
        sys.exit(1)

    print(f"\n⚙️  Computing Inverse Kinematics for ({x_input}, {y_input})...")

    # 3. Solve IK
    solution = ik_solver.compute_angles(x_input, y_input)

    if solution:
        t1 = solution['theta1']
        t2 = solution['theta2']
        print(f"✅ Solution Found: Theta1={t1:.2f}°, Theta2={t2:.2f}°")
        
        # 4. Visualize
        print("📊 Generating Visualization...")
        plot_robot(L1, L2, t1, t2, target=(x_input, y_input))
    else:
        print("❌ Target Unreachable! The point is outside the workspace.")

if __name__ == "__main__":
    main()