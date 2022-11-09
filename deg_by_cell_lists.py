def deg_by_cell_lists(adata,
                      index_list1, index_list2,
                      group1_name = 'group1', group2_name = 'group2', deg_key="two_group_deg", 
                      method='wilcoxon',
                      **kwargs):
    if isinstance(index_list1, list):
        lst = index_list1+index_list2
    if isinstance(index_list1, pd.core.indexes.base.Index):
        lst = index_list1.tolist()+index_list2.tolist()
    bdata = adata[np.unique( lst  )].copy()  
    bdata.obs['__tmp__cluster__'] = "others"
    bdata.obs.loc[index_list1, '__tmp__cluster__'] = group1_name
    bdata.obs.loc[index_list2, '__tmp__cluster__'] = group2_name
    bdata.obs['__tmp__cluster__'] = bdata.obs['__tmp__cluster__'].astype("category")
    sc.tl.rank_genes_groups(bdata, groupby='__tmp__cluster__',
                            key_added='__tmp__deg__', **kwargs)
    import copy
    adata.uns[deg_key] = copy.copy(bdata.uns['__tmp__deg__'])
    
