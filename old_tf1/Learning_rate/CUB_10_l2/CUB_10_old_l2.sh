#!/bin/bash
#SBATCH --job-name=10_l2
#SBATCH --time=20:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/old_tf/Learning_rate/CUB_10_l2/10_l2_s1.err
#SBATCH --output=/home/limei/ProtoryNet/old_tf/Learning_rate/CUB_10_l2/10_l2_s1.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/old_tf/Learning_rate/CUB_10_l2
conda activate /home/limei/miniconda3/envs/old-tf
python3 CUB_10_l2.py