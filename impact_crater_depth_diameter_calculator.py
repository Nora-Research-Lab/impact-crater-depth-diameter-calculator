import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def compute_depth(diameter: float, crater_type: str) -> float:
    if crater_type == "Simple":
        return 0.2 * diameter
    else:  # Complex
        return 0.1 * np.sqrt(diameter)

def compute_volume(depth: float, diameter: float) -> float:
    # Paraboloid approximation: V = (pi/3) * depth * (diameter/2)^2
    return (np.pi / 3.0) * depth * (diameter / 2.0) ** 2

def classify_depth(depth: float, expected_depth: float) -> str:
    ratio = depth / expected_depth
    if ratio < 0.8:
        return "Shallow"
    elif ratio > 1.2:
        return "Deep"
    else:
        return "Normal"

def generate_plot(input_diameter: float, input_depth: float, input_type: str) -> plt.Figure:
    # Generate reference curves for Simple and Complex regimes
    diameters = np.logspace(np.log10(0.1), np.log10(200), 200)
    simple_depths = 0.2 * diameters
    complex_depths = 0.1 * np.sqrt(diameters)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.loglog(diameters, simple_depths, label="Simple (depth = 0.2 * D)")
    ax.loglog(diameters, complex_depths, label="Complex (depth = 0.1 * sqrt(D))")
    ax.scatter([input_diameter], [input_depth], color='red', s=100, zorder=5, label=f"Input ({input_type})")
    ax.set_xlabel("Diameter (km)")
    ax.set_ylabel("Depth (km)")
    ax.set_title("Depth-Diameter Scaling for Impact Craters")
    ax.legend()
    ax.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    return fig
