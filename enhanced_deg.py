#def __get_expr_pcts(adata, group_key, group,  genes, expr_cutoff=0):
#    sel = adata.obs[group_key].isin(group)
#    bdata = adata[sel].copy()
#    pcts = (np.sum( bdata[:, genes].X>0, axis=0)/adata.shape[0]).T
#    return pd.DataFrame(pcts)
#__get_deg_df(bdata, deg_key='__tmp__deg__', group_key='__tmp__cluster__', group, genes)

def deg_by_cell_lists(adata,
                      index_list1, index_list2,
                      group1_name = 'group1', group2_name = 'group2', deg_key="two_group_deg",  
                      **kwargs):
    """
    compare two groups of cells using two lists of cell indices
    index_list1/2 should be two lists of str indices.
    method='wilcoxon' can be passed using kwargs.
    """
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

def deg_by_subsets(adata,
                   group_key, subset, deg_key='deg', **kwargs):
    """
    perform one-vs-others DEG analysis in a subset of cells.
    group_key: the column name in adata.obs
    subset: the cell type you want to keep
    method='wilcoxon' can be passed using kwargs.
    """
    sel   = adata.obs[group_key].isin(subset)
    bdata = adata[sel].copy()
    sc.tl.rank_genes_groups(bdata, groupby=group_key,
                            key_added='__tmp__deg__', **kwargs)
    import copy
    adata.uns[deg_key] = copy.copy(bdata.uns['__tmp__deg__'])
