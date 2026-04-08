import torch
from torchvision import transforms
from PIL import Image
from model import CNN

# Load model
model = CNN()
model.load_state_dict(torch.load("model.pth", map_location="cpu"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])

classes = [
    'AnnualCrop','Forest','HerbaceousVegetation','Highway',
    'Industrial','Pasture','PermanentCrop','Residential',
    'River','SeaLake'
]

def predict(image):
    image = transform(image).unsqueeze(0)
    
    with torch.no_grad():
        output = model(image)
        _, pred = torch.max(output, 1)
    
    return classes[pred.item()]