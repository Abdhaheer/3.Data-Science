class Univariate():
    def QuanQual(self,dataset):
        Qual=[]
        Quan=[]
        for columnName in dataset.columns:
            print(columnName)
            if(dataset[columnName].dtypes=="O"):
                #print ("Qual")
                Qual.append(columnName)
            else:
                #print("Quad")
                Quan.append(columnName)
        return Quan,Qual
    def FreqTable(self,dataset,columnName):
        import pandas as pd
        freqtab=pd.DataFrame(columns=["unique_values","Frequency","Relative_Freq","Cum_Freq"])
        freqtab["unique_values"]=dataset[columnName].value_counts().sort_values().index
        freqtab["Frequency"]=dataset[columnName].value_counts().sort_values().values
        freqtab["Relative_Freq"]=(freqtab["Frequency"]/len(freqtab))*100
        freqtab["Cum_Freq"]=freqtab["Relative_Freq"].cumsum()
        return freqtab
    
    def uniAnalysis(self,dataset,Quan):
        import pandas as pd
        import numpy as np
        unitable=pd.DataFrame(index=["Mean","Median","Mode","25th","50th","75th","99th","100th","IQR","1.5IQR","Lesser","Greater","Min","Max"],columns=Quan)
        for columnName in Quan:
            unitable[columnName]["Mean"]=dataset[columnName].mean()
            unitable[columnName]["Median"]=dataset[columnName].median()
            unitable[columnName]["Mode"]=dataset[columnName].mode()[0]
            unitable[columnName]["25th"]=np.percentile(dataset[columnName],25)
            unitable[columnName]["50th"]=np.percentile(dataset[columnName],50)
            unitable[columnName]["75th"]=np.percentile(dataset[columnName],75)
            unitable[columnName]["99th"]=np.percentile(dataset[columnName],99)
            unitable[columnName]["100th"]=np.percentile(dataset[columnName],100)
            unitable[columnName]["IQR"]=unitable[columnName]["75th"]-unitable[columnName]["25th"]
            unitable[columnName]["1.5IQR"]=1.5*unitable[columnName]["IQR"]
            unitable[columnName]["Lesser"]=unitable[columnName]["25th"]-unitable[columnName]["1.5IQR"]
            unitable[columnName]["Greater"]=unitable[columnName]["75th"]-unitable[columnName]["1.5IQR"]
            unitable[columnName]["Min"]=unitable[columnName].min()
            unitable[columnName]["Max"]=unitable[columnName].max()
        return unitable
