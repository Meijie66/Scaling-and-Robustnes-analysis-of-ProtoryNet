#!/bin/bash
#SBATCH --job-name=2_old_2
#SBATCH --time=10:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/old_tf2/Number_classes/CUB_2_old/2_s2.err
#SBATCH --output=/home/limei/ProtoryNet/old_tf2/Number_classes/CUB_2_old/2_s2.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/old_tf2/Number_classes/CUB_2_old
conda activate /home/limei/miniconda3/envs/old-tf
python3 CUB_2_old.py 