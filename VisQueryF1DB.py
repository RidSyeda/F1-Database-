def displaybar (value1, value2,color):
    import pandas as pd 
    import numpy as np 
    import matplotlib.pyplot as plt
    plt.bar (value1, value2,color=color,width=0.8)
    plt.xticks (range(len(value2)), value1, fontsize=8, rotation=30, ha="center")
    plt. show()
    
def displaypie(list1, list2):
    import matplotlib.pyplot as plt
    plt.pie(list1, labels=list2)
    plt.show()
    
def displayscatter(col1, col2, color):
    import pandas as pd
    import matplotlib.pyplot as plt
    plt.scatter(x=col1, y=col2, color=color)
    plt.xticks(rotation=30,fontsize=8) 
    plt.show()
    
def displayshistogram(col1, bins,color, edgecolor):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    plt.hist(col1, bins, color=color, edgecolor= edgecolor)
    plt.show()
    
def displaycharts(data1, data2, color):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    plt.bar(np.arange(len(data1)), data2, width=0.8,color=color)
    plt.xticks (range(len(data2)), data1, fontsize=8, rotation=30, ha="center") 
    plt.show()
        
def displayline(les1, les2, color):   
    import matplotlib.pyplot as plt 
    import numpy as np 
    plt.plot(les1, les2, color=color, linestyle=':') 
    plt.show() 
    