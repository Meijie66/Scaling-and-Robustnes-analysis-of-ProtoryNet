#!/bin/bash
#SBATCH --job-name=L_10_30
#SBATCH --time=20:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/old_tf1/L_random_proto/CUB_10_30/L_10_30.err
#SBATCH --output=/home/limei/ProtoryNet/old_tf1/L_random_proto/CUB_10_30/L_10_30.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/old_tf1/L_random_proto/CUB_10_30
conda activate /home/limei/miniconda3/envs/old-tf
python3 CUB_10_30.py 