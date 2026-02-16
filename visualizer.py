import matplotlib.pyplot as plt

def plot_robot(l1, l2, theta1, theta2, target=None):
    """
    Visualizes the robot arm configuration.
    """
    # We need to re-calculate positions properly for plotting
    # Convert to radians for plotting math
    import math
    t1_rad = math.radians(theta1)
    t2_rad = math.radians(theta2)

    # Calculate Elbow (Simple Trig)
    elbow_x = l1 * math.cos(t1_rad)
    elbow_y = l1 * math.sin(t1_rad)

    # Calculate Hand (Add second vector)
    # Note: Theta2 is relative to the first link
    hand_x = elbow_x + l2 * math.cos(t1_rad + t2_rad)
    hand_y = elbow_y + l2 * math.sin(t1_rad + t2_rad)

    # Plot Setup
    plt.figure(figsize=(6, 6))
    
    # Draw Links
    x_coords = [0, elbow_x, hand_x]
    y_coords = [0, elbow_y, hand_y]
    
    # Plot Arm (Blue line, Circles at joints)
    plt.plot(x_coords, y_coords, '-o', linewidth=5, markersize=10, color='#2c3e50', label='Robot Arm')
    
    # Plot Target (Red X) if provided
    if target:
        plt.plot(target[0], target[1], 'rx', markersize=15, markeredgewidth=3, label='Target')

    # Styling
    plt.xlim(-(l1+l2)-5, (l1+l2)+5)
    plt.ylim(-(l1+l2)-5, (l1+l2)+5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.title(f"Inverse Kinematics Solver\nTarget: {target} | Angles: {theta1:.1f}°, {theta2:.1f}°")
    plt.legend()
    
    # Save for LinkedIn
    plt.savefig("robot_showcase.png")
    print("📸 Snapshot saved as 'robot_showcase.png'")
    plt.show()