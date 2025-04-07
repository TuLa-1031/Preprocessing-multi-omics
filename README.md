# Preprocessing dữ liệu multi-omics để lựa chọn ra features các quan trọng
# Dựa trên paper [Robust feature learning using contractive autoencoders for multi-omics clustering in cancer subtyping](https://www.sciencedirect.com/science/article/pii/S1046202324002500)
dataset: DNA methylation 450K và RNAseq FPKM [Xena](https://xenabrowser.net/datapages/?cohort=GDC%20TCGA%20Lung%20Adenocarcinoma%20(LUAD)&removeHub=https%3A%2F%2Fxena.treehouse.gi.ucsc.edu%3A443)

## Thực hiện:
  - Dữ liệu DNA methylation được bỏ đi các feature bị thiếu hơn 20% giá trị, sau đó fill các ô bị thiếu giá trị bằng phương pháp tính mean của các sample khác.
  - Tính điểm trên các feature dựa trên công thức:



    ![Công thức expression difference](https://github.com/TuLa-1031/Preprocessing-multi-omics/blob/main/expression%20difference.png)


    
  - Từ điểm số chọn các feature có điểm số cao nhất của từng loại omic (DNA methyaltion 1000 feature, RNAseq 2000 feature).
