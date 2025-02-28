#!/bin/bash
#SBATCH --job-name=10_l4_2
#SBATCH --time=20:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/old_tf2/Learning_rate/CUB_10_l4/10_l4_s2.err
#SBATCH --output=/home/limei/ProtoryNet/old_tf2/Learning_rate/CUB_10_l4/10_l4_s2.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/old_tf2/Learning_rate/CUB_10_l4
conda activate /home/limei/miniconda3/envs/old-tf
python3 CUB_10_l4.py 