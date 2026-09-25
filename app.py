import gradio as gr
from impact_crater_depth_diameter_calculator import compute_depth, compute_volume, classify_depth, generate_plot

def calculate(diameter, crater_type, target_body):
    if diameter is None or diameter <= 0:
        return "Enter a positive diameter", "", "", None
    if diameter < 0.01 or diameter > 500:
        return "Diameter must be between 0.01 and 500 km", "", "", None
    if crater_type not in ("Simple", "Complex"):
        return "Select a valid crater type", "", "", None

    depth = compute_depth(diameter, crater_type)
    volume = compute_volume(depth, diameter)
    expected_depth = compute_depth(diameter, crater_type)  # same as depth
    classification = classify_depth(depth, expected_depth)
    plot = generate_plot(diameter, depth, crater_type)

    depth_str = f"{depth:.2f} km"
    volume_str = f"{volume:.2e} km³"
    classification_str = f"Classification: {classification}"

    return depth_str, volume_str, classification_str, plot

with gr.Blocks(title="Impact Crater Depth-Diameter Calculator") as demo:
    gr.Markdown("# Impact Crater Depth-Diameter Calculator")
    gr.Markdown("Enter crater diameter and type to compute depth, volume, and classification. Optionally select a target body for reference.")
    with gr.Row():
        diameter_input = gr.Number(label="Crater Diameter (km)", minimum=0.01, maximum=500, value=1.0, step=0.01)
    with gr.Row():
        type_input = gr.Dropdown(choices=["Simple", "Complex"], label="Crater Type", value="Simple")
        target_input = gr.Dropdown(choices=["Moon", "Mars", "Earth"], label="Target Body (optional)", value="Moon")
    calc_btn = gr.Button("Calculate")
    with gr.Row():
        depth_out = gr.Textbox(label="Calculated Depth", interactive=False)
        volume_out = gr.Textbox(label="Volume Estimate", interactive=False)
    with gr.Row():
        class_out = gr.Textbox(label="Classification", interactive=False)
    plot_out = gr.Plot(label="Depth-Diameter Scaling Plot")

    calc_btn.click(
        fn=calculate,
        inputs=[diameter_input, type_input, target_input],
        outputs=[depth_out, volume_out, class_out, plot_out]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
