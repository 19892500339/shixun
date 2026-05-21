import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import os
import random

# ===================== 配置 =====================
device = torch.device("cpu")
CLASS_NAMES = ["cat", "dog"]
TEST_DIR = r"E:\_009\dataset\test"

# 加载模型
class BetterCNN(nn.Module):
    def __init__(self):
        super(BetterCNN, self).__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(64, 128, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.fc_layers = nn.Sequential(
            nn.Linear(128 * 8 * 8, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 2)
        )
    def forward(self, x):
        x = self.conv_layers(x)
        x = torch.flatten(x, 1)
        x = self.fc_layers(x)
        return x

model = BetterCNN().to(device)
model.load_state_dict(torch.load("best_model.pth", map_location=device))
model.eval()

# 预处理
transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5,0.5,0.5], std=[0.5,0.5,0.5])
])

# 预测函数
def predict(img_path):
    img = Image.open(img_path).convert("RGB")
    img = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        pred = model(img).argmax(1).item()
    return CLASS_NAMES[pred]

# 加载所有测试图片（带真实标签）
def load_test_images():
    images = []
    for label, cls in enumerate(CLASS_NAMES):
        cls_dir = os.path.join(TEST_DIR, cls)
        for f in os.listdir(cls_dir):
            if f.endswith(('jpg','png','jpeg')):
                images.append( (os.path.join(cls_dir, f), cls) )
    return images

# 10轮批量测试
if __name__ == "__main__":
    all_imgs = load_test_images()
    success = 0
    
    print("===== 开始10轮测试 =====")
    for i in range(10):
        samples = random.sample(all_imgs, 10)
        correct = 0
        for path, true_cls in samples:
            pred_cls = predict(path)
            if pred_cls == true_cls:
                correct +=1
        acc = correct * 10
        print(f"第{i+1}轮 准确率: {acc}%")
        if acc >=70:
            success +=1

    print(f"\n===== 最终结果 =====")
    print(f"10轮中满足≥70%准确率的轮数: {success}")
    print(f"是否达标: {'✅ 是' if success>=7 else '❌ 否'}")