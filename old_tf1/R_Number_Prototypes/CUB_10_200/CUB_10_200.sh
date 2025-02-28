#!/bin/bash
#SBATCH --job-name=R_10_200
#SBATCH --time=2-00:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/old_tf1/R_Number_Prototypes/CUB_10_200/R_10_200.err
#SBATCH --output=/home/limei/ProtoryNet/old_tf1/R_Number_Prototypes/CUB_10_200/R_10_200.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/old_tf1/R_Number_Prototypes/CUB_10_200
conda activate /home/limei/miniconda3/envs/old-tf
python3 CUB_10_200.py