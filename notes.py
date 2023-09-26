#Installation
pip install seaborn as s

#import
import seaborn 

#plot
s..set_style('darkgrid')

#Apart from darkgrid, there are other styles that you can use like:-
darkgrid
whitegrid
dark
white
ticks 

#Plotting in Seaborn
s.scatterplot(x=df[' '], y=df[' '])
s.scatterplot(x=' ', y=' ', data=df)
s.scatterplot(x=' ', y=' ', hue=' ', data=df, alpha=)

#countplot
s.countplot(x=' ', data=df)

#displot
s.displot(x=df[' '], kde=False)

#kdeplot
s.kdeplot(x=df[' '])

#regplot
s.regplot(x=df[' '], y=df[' '], scatter_kws={'color','pink'}, line_kws={'color'.'red'})

#Implot
s.Implot(x=' ', y=' ',hue=' ',data=df)

#pairplot
s.pairplot(df[[' '],' ',' ']]

#joinplot
s.joinplot(x=' ',y=' ',data=df)

#boxplot
s.boxplot(x=' ',data=df)

#swarmplot
s.swarmplot(x=' ',y=' ',data=df,alpha=)

#heatmap
s.heatmap(df.corr(),annot=True,cmap='inferno')

#stripplot
s.stripplot(x=' ',y=' ',data=df,palette=colors)

  

