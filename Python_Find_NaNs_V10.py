def find_nan(df):
    ''' This function takes a dataframe and computes the number of NaNs in it.
        You will need the following libraries : pandas, numpy and HTML.
        To import HTML run this : from IPython.display import display, HTML
    '''
    
    cols_with_nan = [] # Liste pour stocker les col comportant partiellement des NaN.
    cols_no_nan = [] # Liste pour stocker les col ne comportant aucun NaN.
    cols_full_nan = [] # Liste pour stocker les col comportortant uniquement des NaN (rare mais possible).
    nb_nan_by_col = [] # Liste pour stocker les NaN par col :
    perc_nan_by_col = [] # Liste pour stocker les % de NaN par col.


    for col in df.columns.values: # Boucler sur les col pour calculer le nbr des NaN.
        if df[col].isnull().any(): # On teste l'existence de NaN pour la col en cours.
            nb_total_lines = len(df.index) # On stocke le nbr de lignes de notre df.
            nb_nan = df[col].isnull().sum() # On stocke le nbr de NaN par col.
            if nb_nan != nb_total_lines : # On traite le cas où la col contient partiellement des NaN.
                cols_with_nan.append(col) # On récupère le nom de la col contenant des NaN.
                nb_nan_by_col.append(nb_nan) # On inscrit le nbr de NaN pour la col en cours.

            else : # On traite le cas où la col n'a que des NaN.
                cols_full_nan.append(col) # On inscrit le nbr de NaN dans la colonne en question.
                perc_nan_by_col.append(100) # On inscrit 100% pour la col en cours.

        else : # On traite le cas où la colonne ne comporte pas de NaN.
            cols_no_nan.append(col) # On inscrit le nbr de NaN dans la col en question.
            perc_nan_by_col.append(0) # On inscrit 0% dans la col en question. 

    # On sort de la boucle FOR.

    if (cols_with_nan + cols_full_nan): # On bool teste l'existence de col partielle ou complète NaN.
        nb_nan_total = df.isnull().sum() # On stocke la le nbr total de NaN contenus dans notre df.
        perc_nan_by_col = (round(nb_nan_total / df.shape[0] * 100, 2)) ## On affiche le % de NaN pour les col avec des NaN.

    resultat = pd.concat([nb_nan_total, perc_nan_by_col], axis = 1, keys=['Nb NaN', '% NaN']) # On affiche le résultat final.
    display(HTML(resultat.to_html()))
    
    legende = {1 : "Nb NaN : nombre de NaN par colonne en valeur absolue.",
               2 : "% NaN : pourcentage de NaN par colonne."
              }
    print(legende[1], legende[2], sep = "\n")
    
# END OF FUNCTION 