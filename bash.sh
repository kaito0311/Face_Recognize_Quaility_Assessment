git clone -n --depth=1 --filter=blob:none  "https://github.com/deepinsight/insightface.git"
cd "repo"
git sparse-checkout set "recognition/arcface_torch/"
git fetch origin
git checkout main
git pull  



CUDA_VISIBLE_DEVICES=1 train_v2.py configs/ms1mv2_r100
CUDA_VISIBLE_DEVICES=1 python train_only_head.py configs/ms1mv2_r160
