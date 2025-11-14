def clean_header_save(path:str,sheet=0):
    """This function is designed to clean headers of an excel file

    Parameters
    ----------------------
    path: str

    path to your excel file
    
    sheet: int

    Return
    ---------------------

    
    """



    import pandas as pd
    aa = pd.read_excel(
        path, sheet_name=sheet
        )
    aa.columns = [x.lower() for x in aa]
    aa.columns = [x.strip() for x in aa ]
    aa.columns = [x.replace(" ","_") for x in aa ]
    aa.to_excel(r"C:\Users\HP\Desktop\clean_header.xlsx",index=False)
    print("Your excel file has been modified and saved in your desktop")



def clean_header_return(path:str,sheet=0):
    """This function is designed to clean headers of an excel file

    Parameters
    ----------------------
    path: str

    path to your excel file
    
    sheet: int

    Return
    ---------------------

    
    """



    import pandas as pd
    aa = pd.read_excel(
        path, sheet_name=sheet
        )
    aa.columns = [x.lower() for x in aa]
    aa.columns = [x.strip() for x in aa ]
    aa.columns = [x.replace(" ","_") for x in aa ]
    return aa 
    


