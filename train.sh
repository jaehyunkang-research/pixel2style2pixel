torchrun --nproc_per_node=3 scripts/train.py \
--dataset_type=ffhq_encode \
--exp_dir=experiments/amp \
--workers=4 \
--batch_size=3 \
--test_batch_size=3 \
--test_workers=4 \
--val_interval=5000 \
--save_interval=10000 \
--encoder_type=GradualStyleEncoder \
--start_from_latent_avg \
--lpips_lambda=0.8 \
--l2_lambda=1 \
--id_lambda=0.1 \
--cams_lambda=1 \
--dataset_path=/workspace/ffhq_512_mirrored \
--distributed=True 