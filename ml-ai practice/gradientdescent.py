import numpy as np 

# Data: y = 2x+3

x = np.array([0, 1, 2, 3, 4])
y = np.array([3,5,7,9,11])

# Initialize parameters 

w = 0.0 # weight
b = 0.0 # bias 
lr = 0.1 # learning rate

# Training loop 

for epoch in range(20):

    # 1. prediction
    y_pred = w * x + b 

    # 2. loss (Mean Squared Error)
    loss = np.mean((y- y_pred)**2)

    # 3. Gradients(how w and b should change
    dw = -2 * np.mean(x*(y - y_pred))
    db = -2 * np.mean(y - y_pred)

    # 4. update parameters
    w = w - lr * dw 
    b = b - lr * db 

    print(f"Epoch {epoch}: w={w:.2f}, b={b:.2f}, loss={loss:.4f}")

print("\nFinal model: ")
print(f"y = {w:.2f}x + {b:.2f}")


