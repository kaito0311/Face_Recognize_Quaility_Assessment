git clone -n --depth=1 --filter=blob:none  "https://github.com/deepinsight/insightface.git"
cd "repo"
git sparse-checkout set "recognition/arcface_torch/"
git fetch origin
git checkout main
git pull  
