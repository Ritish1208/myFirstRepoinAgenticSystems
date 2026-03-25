import pandas as pd
import plotly.express as px

# Step 1: Create dataset
epochs = list(range(1, 11))
loss_values = [0.9, 0.75, 0.6, 0.5, 0.45, 0.42, 0.4, 0.39, 0.38, 0.38]

# Step 2: Create DataFrame
df = pd.DataFrame({
    "Epoch": epochs,
    "Loss": loss_values
})

# Step 3: Create interactive line chart
fig = px.line(df, x="Epoch", y="Loss", title="Training Loss Over Epochs")

# Step 4: Add labels
fig.update_layout(
    xaxis_title="Epoch",
    yaxis_title="Loss"
)

# Step 5: Add annotation (where loss stabilizes)
fig.add_annotation(
    x=9,
    y=0.38,
    text="Loss Stabilizes Here",
    showarrow=True,
    arrowhead=2
)

# Step 6: Show chart
fig.show()