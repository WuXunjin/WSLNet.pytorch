CUDA_VISIBLE_DEVICES=1,7 python3 -m demo_coco /home/lucliu/dataset/mscoco \
--image-size 448 \
--batch-size 50 \
--lrp 0.1 \
--lr 0.01 \
--epochs 12 \
--k 0.2 \
--maps 4 \
--alpha 0.7 \
# --resume ./expes/models/coco_add_no_grp_conv/448/50_d_8/checkpoint.pth.tar