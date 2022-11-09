# scanpy_deg
enhanced DEG analysis in scanpy

# usage
## perform group1-vs-group2 analysis
```
deg_by_cell_lists(adata, 
                  index_list1=cell_indices_1, index_list2=cell_indices_2,
                  deg_key='two_group_deg',
                  method='wilcoxon'
                 )
```

## check results
<img width="582" alt="image" src="https://user-images.githubusercontent.com/18084613/200899134-8678ce46-e303-4d73-95f1-655f7ffd1556.png">


## perform one-vs-others in a subset of groups
```
deg_by_subsets(adata, group_key='leiden', subset=['1','13','14'], 
               deg_key='deg_1_13_14', method='wilcoxon'
              )
```

## check results
<img width="537" alt="image" src="https://user-images.githubusercontent.com/18084613/200899415-09e493be-862f-4502-a9a5-ae865bcb6a63.png">

