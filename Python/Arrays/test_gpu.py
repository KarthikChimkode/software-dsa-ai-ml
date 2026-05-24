import torch

def test_gpu():
    # Check if CUDA is available
    print(f"CUDA available: {torch.cuda.is_available()}")
    
    if torch.cuda.is_available():
        # Get the current device
        device = torch.cuda.current_device()
        print(f"Current CUDA device: {device}")
        
        # Get the name of the device
        print(f"Device name: {torch.cuda.get_device_name(device)}")
        
        # Create a test tensor on GPU
        x = torch.rand(5, 3).cuda()
        print("\nTest tensor on GPU:")
        print(x)
        
        # Test GPU computation
        y = torch.rand(5, 3).cuda()
        z = x + y
        print("\nGPU computation result:")
        print(z)
    else:
        print("CUDA is not available. Please check your PyTorch installation.")

if __name__ == "__main__":
    test_gpu() 