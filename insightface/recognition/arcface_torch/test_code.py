import torch 

from backbones import get_model

backbone = get_model(
        "r160", dropout=0.0, fp16=True, num_features=512).cuda()



# torch.save(

#     backbone.state_dict(),
#         "wieght.pth", 
# )
# print("[INFO] Loadding pretrained backbone")
# original_weight = torch.load("/data/disk2/tanminh/Evaluate_FIQA_EVR/pretrained/r160_imintv4_statedict.pth")
# backbone_dict = dict() 
# for key in original_weight.keys():
#     backbone_dict["module." + str(key)] = original_weight[key]
# backbone.load_state_dict(backbone_dict)

backbone_dict = torch.load("wieght.pth")
for key in backbone_dict.keys():
    print(key)

original_dict = torch.load("/data/disk2/tanminh/Evaluate_FIQA_EVR/pretrained/r160_imintv4_statedict.pth")

for key in backbone_dict.keys():
    if key not in original_dict.keys():
        print("[INFO] key not contain: ", key) 
    else: 
        