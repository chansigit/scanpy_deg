# scanpy_deg
enhanced DEG analysis in scanpy

# usage
```
deg_by_cell_lists(adata, 
                  index_list1=cell_indices_1, index_list2=cell_indices_2,
                  deg_key='two_group_deg',
                  method='wilcoxon'
                 )
```
<img width="582" alt="image" src="https://user-images.githubusercontent.com/18084613/200899134-8678ce46-e303-4d73-95f1-655f7ffd1556.png">



```
deg_by_subsets(adata, group_key='leiden', subset=['1','13','14'], 
               deg_key='deg_1_13_14', method='wilcoxon'
              )
```
<img width="461" alt="image" src="https://user-images.githubusercontent.com/18084613/200899279-252f70f5-3bc3-45f7-a93c-3b17fbf650e7.png">
