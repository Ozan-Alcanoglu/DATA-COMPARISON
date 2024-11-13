import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from setupUi import Ui_MainWindow

readerF=pd.read_csv("2022_2023_Football_Player_Stats.csv",sep=";",encoding="Latin-1")
readerB=pd.read_csv("all_seasons.csv")

class MainWindow_Function(Ui_MainWindow):

    def Football_Statistics(self):

        fig=Figure()

        canvas=FigureCanvas(fig)
        layout=self.layout_F
        layout.addWidget(canvas)
        canvas.draw()
         
    def Goals_vs_Assists_Ratio(self):

        assist=readerF[(readerF['Pos'] == 'MFFW') | (readerF['Pos'] == 'MF') | (readerF['Pos'] == 'MFDF')]["Assists"].sum()
        total_pass=readerF[(readerF['Pos'] == 'MFFW') | (readerF['Pos'] == 'MF') | (readerF['Pos'] == 'MFDF')]["PasAss"].sum()  

        goal_ratio=readerF[(readerF['Pos'] == 'FWMF') | (readerF['Pos'] == 'FW') | (readerF['Pos'] == 'FWDF')]["G/Sh"].mean()

        assist_ratio=(assist/total_pass) if total_pass > 0 else 0

        fig = Figure()
        ax = fig.add_subplot(111)

        labels = ['Midfielders Assist Ratio', 'Forwards Goal Ratio']
        values = [assist_ratio, goal_ratio]

        bar=ax.bar(labels, values, color=['yellow','red'], width=0.4)
        ax.set_ylabel('Ratios')
        ax.set_title('Assist and Goal Ratios')
        ax.set_ylim(0, 0.2)

        for ratio in bar:
            yval = ratio.get_height()
            ax.text(ratio.get_x() + ratio.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

        
        canvas = FigureCanvas(fig)
        layout = self.layout_F
        layout.addWidget(canvas) 
        canvas.draw() 

    def Forwards_vs_Defenders_Aerial(self):

        defender=readerF[(readerF['Pos']== 'DF') | (readerF['Pos']== 'DFFW') |(readerF['Pos']== 'DFMF')]['AerWon%'].mean()
        forward=readerF[(readerF['Pos'] == 'FWMF') | (readerF['Pos'] == 'FW') | (readerF['Pos'] == 'FWDF')]['AerWon%'].mean()

        fig = Figure()
        ax = fig.add_subplot(111)

        labels = ['Forward Aerials Won', 'Defender Aerials Won']
        values = [forward,defender]

        ax.pie(values, labels=labels, colors=['red', 'lightgreen'], shadow=True,autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  

        ax.set_title('Aerials Won Ratios')
        
        canvas = FigureCanvas(fig)
        layout = self.layout_F
        layout.addWidget(canvas) 
        canvas.draw() 

    def Best_Forwards(self):

        readerF['Goals'] = pd.to_numeric(readerF['Goals'], errors='coerce')
        readerF['Assists'] = pd.to_numeric(readerF['Assists'], errors='coerce')

        best_forwards_name = readerF[(readerF['Pos'] == 'FWMF') | (readerF['Pos'] == 'FW') | (readerF['Pos'] == 'FWDF')]
        best_forwards_total = best_forwards_name.assign(Total=best_forwards_name['Goals'] + best_forwards_name['Assists'])
        best_forwards_list = best_forwards_total.sort_values(by='Total', ascending=False).head(3)

        fig=Figure()
        ax=fig.add_subplot(1,1,1)

        best_players = best_forwards_list['Player'].tolist()
        labels=best_players  
        values = best_forwards_list['Total'].tolist()  

        bar=ax.bar(labels, values, color=['red','red','red'], width=0.4)
        ax.set_ylabel('G+A')
        ax.set_title('Best Forwards By Goals')
        ax.set_ylim(0, 70)

        for g_a in bar:
            yval = g_a.get_height()
            ax.text(g_a.get_x() + g_a.get_width()/2, yval, f'Total: {round(yval, 2)}', ha='center', va='bottom')



        canvas=FigureCanvas(fig)
        layout=self.layout_F
        layout.addWidget(canvas)
        canvas.draw()

    def Forwards_vs_Defenders_Attack_and_Defend(self):

        forwards_driblings=readerF[(readerF['Pos'] == 'FWMF') | (readerF['Pos'] == 'FW') | (readerF['Pos'] == 'FWDF')]['ToSuc%'].mean()
        defenders_tackles=readerF[(readerF['Pos']== 'DF') | (readerF['Pos']== 'DFFW') |(readerF['Pos']== 'DFMF')]['TklDri%'].mean()

        fig=Figure()
        ax=fig.add_subplot(1,1,1)

        labels=[("Forwards dribling"),("Defenders tackles")]
        values=[forwards_driblings,defenders_tackles]

        ax.pie(values,labels=labels,colors=("red","lightgreen"),shadow=True,autopct='%1.1f%%', startangle=90)
        ax.axis("equal")
        ax.set_title("Attack vs Defend")

        canvas=FigureCanvas(fig)
        layout=self.layout_F
        layout.addWidget(canvas)
        canvas.draw()

    def Most_Played_Minutes(self):

        most_min=readerF.sort_values(by='Min', ascending=False).head(5)[['Player', 'Min']]
        labels=most_min['Player'].tolist()
        values=most_min['Min'].tolist()

        fig=Figure()
        ax=fig.add_subplot(111)

        bar=ax.bar(labels, values, color=("blue", "blue", "blue"), width=0.4)
        ax.set_ylabel("Minute")
        ax.set_ylim(0,3000)
        ax.set_title("Top 5 Players by Minutes Played")
        ax.set_xticklabels(labels, fontsize=7)

        for g_a in bar:
            yval = g_a.get_height()
            ax.text(g_a.get_x() + g_a.get_width() / 2, yval, str(yval), ha='center', va='bottom')
            

        canvas=FigureCanvas(fig)
        layout=self.layout_F
        layout.addWidget(canvas)
        canvas.draw()

    def Best_Passing_Goalkeeper(self):

        best_passer = readerF[readerF['Pos'] == 'GK'][['Player', 'PasTotCmp%']]


        keepers = best_passer.sort_values(by='PasTotCmp%', ascending=False).head(3)
        keepers_names = keepers['Player'].tolist()
        keepers_values = keepers['PasTotCmp%'].tolist()

        fig=Figure()
        ax=fig.add_subplot(111)
        labels=keepers_names
        values=keepers_values

        bar=ax.bar(labels,values, color=("blue","blue","blue"), width=0.4)
        ax.set_ylabel("Saves%")
        ax.set_title("Best Keepers")
        ax.set_ylim(0,100)

        for percentage in bar:
            yval = percentage.get_height()
            ax.text(percentage.get_x() +percentage.get_width()/2, yval,f'{yval:.1f}%', ha='center', va='bottom')

        canvas=FigureCanvas(fig)
        layout=self.layout_F
        layout.addWidget(canvas)
        canvas.draw()

    def Midfielders_Pass_Choices(self):

        long_passes=readerF[(readerF['Pos'] == 'MFFW') | (readerF['Pos'] == 'MF') | (readerF['Pos'] == 'MFDF')]['PasLonAtt'].sum()
        short_passes=readerF[(readerF['Pos'] == 'MFFW') | (readerF['Pos'] == 'MF') | (readerF['Pos'] == 'MFDF')]['PasMedAtt'].sum()

        long_percentage=int((long_passes/(long_passes+short_passes))*100)
        short_percentage=int((short_passes/(long_passes+short_passes))*100)

        labels=['short passes','long passes']
        values=[short_percentage,long_percentage]

        fig=Figure()
        ax=fig.add_subplot(111)

        ax.pie(values,labels=labels,colors=['purple','yellow'],shadow=True,autopct='%1.1f%%', startangle=90)
        ax.axis("equal")
        ax.set_title("Pass Choices By Midfielders")

        canvas=FigureCanvas(fig)
        layout=self.layout_F
        layout.addWidget(canvas)
        canvas.draw()

    def Best_Defenders(self):
        
        best_defenders=readerF[(readerF['Pos'] == 'DFFW') | (readerF['Pos'] == 'DF') | (readerF['Pos'] == 'DFMF')]
        best_defenders_tklwonp=best_defenders.assign(TklWonp=best_defenders['TklWon'].astype(float)/best_defenders['Tkl'].astype(float))
        best_defenders_sorted = best_defenders_tklwonp[(best_defenders_tklwonp['TklWonp']!=0.0) & (best_defenders_tklwonp['TklWonp']!=1.0)]
        best_defenders_who=best_defenders_sorted.sort_values(by='TklWonp', ascending=False).head(3)
        
        
        fig=Figure()
        ax=fig.add_subplot(1,1,1)

        labels=best_defenders_who['Player'].to_list()
        values=best_defenders_who['TklWonp'].to_list()

        bar=ax.bar(labels, values, color=['red','red','red'], width=0.4)
        ax.set_ylabel('Tackles%')
        ax.set_title('Best Defenders By Tackles')
        ax.set_ylim(0,1)

        for tkl in bar:
            yval = tkl.get_height()
            ax.text(tkl.get_x() + tkl.get_width()/2, yval, f'Tackles: {round(yval, 2)}', ha='center', va='bottom')



        canvas=FigureCanvas(fig)
        layout=self.layout_F
        layout.addWidget(canvas)
        canvas.draw()

    def Basketball_Statistics(self):

        fig=Figure()

        canvas=FigureCanvas(fig)
        layout=self.layout_B
        layout.addWidget(canvas)
        canvas.draw()
        
    def Best_Basketball_Player_by_Points(self):

        basketballer=readerB.sort_values(by='pts',ascending=False)

        labels=basketballer['player_name'].head(3).tolist()
        values=basketballer['pts'].head(3).tolist()

        fig = Figure()
        ax = fig.add_subplot(111)

        seen_labels = {}
        unique_labels = []
        for label in labels:
            if label in seen_labels:
                
                seen_labels[label] += 1
                unique_labels.append(label)
            else:
                seen_labels[label] = 1
                unique_labels.append(label)
        
        
        bar = ax.bar(range(len(unique_labels)), values, color='purple', width=0.4)
        ax.set_title("Best Basketballer")
        ax.set_ylabel("Points")
        ax.set_ylim(0,100)
        ax.set_xticks(range(len(unique_labels)))
        ax.set_xticklabels(unique_labels)

        for pts in bar:
            yval = pts.get_height()
            ax.text(pts.get_x() + pts.get_width()/2, yval, f'Pts: {round(yval, 2)}', ha='center', va='bottom')


        canvas=FigureCanvas(fig)
        layout=self.layout_B
        layout.addWidget(canvas)
        canvas.draw()

    def Best_Basketball_Players_by_Rating(self):

        sort_rated=readerB.sort_values(by="net_rating",ascending=False)
        labels=sort_rated['player_name'].head(3)
        values=sort_rated['net_rating'].head(3)

        fig=Figure()
        ax=fig.add_subplot(111)
        bar=ax.bar(labels,values,color=("red","red","red"),width=0.4)
        ax.set_title("Best Basketballer By Rating")
        ax.set_ylabel("Ratings")
        ax.set_ylim(0,350)

        canvas=FigureCanvas(fig)
        layout=self.layout_B
        layout.addWidget(canvas)
        canvas.draw()

    def Best_Players_of_the_Last_5_Years(self):

        best_player=readerB.sort_values(by='net_rating',ascending=False)
        best_player_2022=best_player[(best_player['season']=='2022-23')]['player_name'].head(1).values[0]
        best_rating_2022=best_player[(best_player['season']=='2022-23')]['net_rating'].head(1).values[0]
        best_player_2021=best_player[(best_player['season']=='2021-22')]['player_name'].head(1).values[0]
        best_rating_2021=best_player[(best_player['season']=='2021-22')]['net_rating'].head(1).values[0]
        best_player_2020=best_player[(best_player['season']=='2020-21')]['player_name'].head(1).values[0]
        best_rating_2020=best_player[(best_player['season']=='2020-21')]['net_rating'].head(1).values[0]
        best_player_2019=best_player[(best_player['season']=='2019-20')]['player_name'].head(1).values[0]
        best_rating_2019=best_player[(best_player['season']=='2019-20')]['net_rating'].head(1).values[0]
        best_player_2018=best_player[(best_player['season']=='2018-19')]['player_name'].head(1).values[0]
        best_rating_2018=best_player[(best_player['season']=='2018-19')]['net_rating'].head(1).values[0]

        labels=[best_player_2018,best_player_2019,best_player_2020,best_player_2021,best_player_2022]
        values=[best_rating_2018,best_rating_2019,best_rating_2020,best_rating_2021,best_rating_2022]

        fig=Figure()
        ax=fig.add_subplot(111)

        ax.plot(labels,values, marker='o', linestyle='-', color='blue', label='Rating')
        ax.set_title("Best Players By Years")
        ax.set_ylabel("Ratings")
        plt.xticks(rotation=45)

        
        plt.legend()
        plt.tight_layout()
        
        for i, txt in enumerate(values):
            ax.annotate(f'{txt:.2f}', (labels[i], values[i]), textcoords="offset points", xytext=(0,10), ha='center')


        canvas=FigureCanvas(fig)
        layout=self.layout_B
        layout.addWidget(canvas)
        canvas.draw()

    def Best_Assisters_of_the_Last_5_Years(self):

        best_assister=readerB.sort_values(by='ast',ascending=False)
        best_player_2022=best_assister[(best_assister['season']=='2022-23')]['player_name'].head(1).values[0]
        best_assist_2022=best_assister[(best_assister['season']=='2022-23')]['ast'].head(1).values[0]
        best_player_2021=best_assister[(best_assister['season']=='2021-22')]['player_name'].head(1).values[0]
        best_assist_2021=best_assister[(best_assister['season']=='2021-22')]['ast'].head(1).values[0]
        best_player_2020=best_assister[(best_assister['season']=='2020-21')]['player_name'].head(1).values[0]
        best_assist_2020=best_assister[(best_assister['season']=='2020-21')]['ast'].head(1).values[0]
        best_player_2019=best_assister[(best_assister['season']=='2019-20')]['player_name'].head(1).values[0]
        best_assist_2019=best_assister[(best_assister['season']=='2019-20')]['ast'].head(1).values[0]
        best_player_2018=best_assister[(best_assister['season']=='2018-19')]['player_name'].head(1).values[0]
        best_assist_2018=best_assister[(best_assister['season']=='2018-19')]['ast'].head(1).values[0]

        

        labels = ["(2018-19)","(2019-20)","(2020-21)","(2021-22)","(2022-23)"]
        players=[best_player_2018,best_player_2019,best_player_2020,best_player_2021,best_player_2022]
        values=[best_assist_2018,best_assist_2019,best_assist_2020,best_assist_2021,best_assist_2022]

        fig=Figure()
        ax=fig.add_subplot(111)


        ax.plot(labels,values, marker='o', linestyle='-', color='red')
        ax.set_title("Best Assisters By Years")
        ax.set_ylabel("Assists")
        plt.xticks(rotation=45)

        for i, txt in enumerate(values):
            ax.annotate(f'{players[i]} {txt:.2f}', (labels[i], values[i]), textcoords="offset points", xytext=(0,10), ha='center',fontsize=8)


        
        plt.legend()
        plt.tight_layout()

        canvas=FigureCanvas(fig)
        layout=self.layout_B
        layout.addWidget(canvas)
        canvas.draw()

    def Average_Assists_of_the_Last_5_Years(self):

        assists_2018=readerB[(readerB['season']=='2018-19')]['ast'].mean()
        assists_2019=readerB[(readerB['season']=='2019-20')]['ast'].mean()
        assists_2020=readerB[(readerB['season']=='2020-21')]['ast'].mean()
        assists_2021=readerB[(readerB['season']=='2021-22')]['ast'].mean()
        assists_2022=readerB[(readerB['season']=='2022-23')]['ast'].mean()

        labels = ["(2018-19)","(2019-20)","(2020-21)","(2021-22)","(2022-23)"]
        values=[assists_2018,assists_2019,assists_2020,assists_2021,assists_2022]

        fig=Figure()
        ax=fig.add_subplot(111)

        plot=ax.plot(labels,values,marker='o', linestyle='-', color='red')
        ax.set_title("Average Assists Of The Last 5 Years")
        ax.set_ylabel("Average Assists")

        for i, txt in enumerate(values):
            ax.annotate(f'{txt:.2f}', (labels[i], values[i]), textcoords="offset points", xytext=(0,15), ha='center')

        canvas=FigureCanvas(fig)
        layout=self.layout_B
        layout.addWidget(canvas)
        canvas.draw()

    def Average_Points_of_the_Last_5_Years(self):

        pts_2018=readerB[(readerB['season']=='2018-19')]['pts'].mean()
        pts_2019=readerB[(readerB['season']=='2019-20')]['pts'].mean()
        pts_2020=readerB[(readerB['season']=='2020-21')]['pts'].mean()
        pts_2021=readerB[(readerB['season']=='2021-22')]['pts'].mean()
        pts_2022=readerB[(readerB['season']=='2022-23')]['pts'].mean()

        labels = ["(2018-19)","(2019-20)","(2020-21)","(2021-22)","(2022-23)"]
        values=[pts_2018,pts_2019,pts_2020,pts_2021,pts_2022]

        fig=Figure()
        ax=fig.add_subplot(111)

        plot=ax.plot(labels,values,marker='o', linestyle='-', color='red')
        ax.set_title("Average Pts Of The Last 5 Years")
        ax.set_ylabel("Average Points")

        for i, txt in enumerate(values):
            ax.annotate(f'{txt:.2f}', (labels[i], values[i]), textcoords="offset points", xytext=(0,15), ha='center')

        canvas=FigureCanvas(fig)
        layout=self.layout_B
        layout.addWidget(canvas)
        canvas.draw()

    def Top_3_Tallest_Players(self):

        players=readerB.sort_values(by='player_height',ascending=False)
        players_name=players['player_name'].head().tolist()
        players_height=players['player_height'].head().tolist()

        labels=players_name
        values=players_height

        fig=Figure()
        ax=fig.add_subplot(111)

        bar=ax.bar(labels,values,color=["cyan","cyan","cyan"],width=0.4)
        ax.set_title("Most Tallest Players")
        ax.set_ylabel("Heights(cm)")
        ax.set_ylim(0,250)

        for height in bar:
            yval = height.get_height()
            ax.text(height.get_x() + height.get_width()/2, yval, f'Height: {round(yval, 2)}', ha='center', va='bottom')

        canvas=FigureCanvas(fig)
        layout=self.layout_B
        layout.addWidget(canvas)
        canvas.draw()

    def Tallest_Players_of_the_Last_5_Years(self):

        tallest_player=readerB.sort_values(by='player_height',ascending=False)
        tallest_player_2022=tallest_player[(tallest_player['season']=='2022-23')]['player_name'].head(1).values[0]
        player_height_2022=tallest_player[(tallest_player['season']=='2022-23')]['player_height'].head(1).values[0]
        tallest_player_2021=tallest_player[(tallest_player['season']=='2021-22')]['player_name'].head(1).values[0]
        player_height_2021=tallest_player[(tallest_player['season']=='2021-22')]['player_height'].head(1).values[0]
        tallest_player_2020=tallest_player[(tallest_player['season']=='2020-21')]['player_name'].head(1).values[0]
        player_height_2020=tallest_player[(tallest_player['season']=='2020-21')]['player_height'].head(1).values[0]
        tallest_player_2019=tallest_player[(tallest_player['season']=='2019-20')]['player_name'].head(1).values[0]
        player_height_2019=tallest_player[(tallest_player['season']=='2019-20')]['player_height'].head(1).values[0]
        tallest_player_2018=tallest_player[(tallest_player['season']=='2018-19')]['player_name'].head(1).values[0]
        player_height_2018=tallest_player[(tallest_player['season']=='2018-19')]['player_height'].head(1).values[0]

        labels = ["(2018-19)","(2019-20)","(2020-21)","(2021-22)","(2022-23)"]
        players=[tallest_player_2018,tallest_player_2019,tallest_player_2020,tallest_player_2021,tallest_player_2022]
        values=[player_height_2018,player_height_2019,player_height_2020,player_height_2021,player_height_2022]

        fig=Figure()
        ax=fig.add_subplot(111)

        ax.plot(labels,values,marker="o",linestyle="-",color="red")
        ax.set_title("Tallest Players of the Last 5 Years")
        ax.set_ylabel("Height(cm)")

        for i, txt in enumerate(values):
            ax.annotate(f'{players[i]} {txt:.2f}', (labels[i], values[i]), textcoords="offset points", xytext=(0,15), ha='center',fontsize=8)

        canvas=FigureCanvas(fig)
        layout=self.layout_B
        layout.addWidget(canvas)
        canvas.draw()

    def Footballer_vs_Basketballer_2022(self):

        fig=Figure()

        canvas=FigureCanvas(fig)
        layout=self.layout_FvB
        layout.addWidget(canvas)
        canvas.draw()

    def Football_vs_Basketball_by_Shoot(self):

        football=readerF['G/Sh'].mean()
        basketball=readerB[(readerB['season']=='2022-23')]['ts_pct'].mean()


        labels=["Football","Basketball"]
        values=[football,basketball]

        fig=Figure()
        ax=fig.add_subplot(111)

        bar=ax.bar(labels,values,color=("red","purple"),width=0.4)
        ax.set_title("Football vs Basketball by Shoot")
        ax.set_ylabel("Shoot Ratio(Shoot/Total Shoot)")
        ax.set_ylim(0,1)

        for ratio in bar:
            yval=ratio.get_height()
            ax.text(ratio.get_x()+ratio.get_width()/2, yval, f'Ratio: {round(yval, 2)}', ha='center', va='bottom')

        canvas=FigureCanvas(fig)
        layout=self.layout_FvB
        layout.addWidget(canvas)
        canvas.draw()

    def Football_vs_Basketball_by_Assist(self):

        assist=readerF[(readerF['Pos'] != 'GK')]["Assists"].sum()
        total_pass=readerF[(readerF['Pos'] != 'GK') ]["PasAss"].sum()          

        football=(assist/total_pass) if total_pass > 0 else 0

        basketball=readerB[(readerB['season']=='2022-23')]['ast_pct'].mean()


        labels=["Football","Basketball"]
        values=[football,basketball]

        fig=Figure()
        ax=fig.add_subplot(111)

        bar=ax.bar(labels,values,color=("red","purple"),width=0.4)
        ax.set_title("Football vs Basketball by Assist")
        ax.set_ylabel("Assist Ratio(Assist/Total Pass)")
        ax.set_ylim(0,0.2)

        for ratio in bar:
            yval=ratio.get_height()
            ax.text(ratio.get_x()+ratio.get_width()/2, yval, f'Ratio: {round(yval, 2)}', ha='center', va='bottom')

        canvas=FigureCanvas(fig)
        layout=self.layout_FvB
        layout.addWidget(canvas)
        canvas.draw()

    def Football_vs_Basketball_by_Minute(self):

        football=readerF["Min"].mean()

        basketball=(readerB[(readerB['season']=='2022-23')]['gp'].mean())*40


        labels=["Football","Basketball"]
        values=[football,basketball]

        fig=Figure()
        ax=fig.add_subplot(111)

        bar=ax.bar(labels,values,color=("red","purple"),width=0.4)
        ax.set_title("Football vs Basketball by Minute")
        ax.set_ylabel("Minutes Per Player")
        ax.set_ylim(0,2000)

        for ratio in bar:
            yval=ratio.get_height()
            ax.text(ratio.get_x()+ratio.get_width()/2, yval, f'Minute: {round(yval, 2)}', ha='center', va='bottom')

        canvas=FigureCanvas(fig)
        layout=self.layout_FvB
        layout.addWidget(canvas)
        canvas.draw()

    def Football_vs_Basketball_by_Age(self):

        football=readerF["Age"].mean()

        basketball=(readerB[(readerB['season']=='2022-23')]['age'].mean())


        labels=["Football","Basketball"]
        values=[football,basketball]

        fig=Figure()
        ax=fig.add_subplot(111)

        bar=ax.bar(labels,values,color=("red","purple"),width=0.4)
        ax.set_title("Football vs Basketball by Age")
        ax.set_ylabel("Average Age")
        ax.set_ylim(0,40)

        for ratio in bar:
            yval=ratio.get_height()
            ax.text(ratio.get_x()+ratio.get_width()/2, yval, f'Age: {round(yval, 2)}', ha='center', va='bottom')

        canvas=FigureCanvas(fig)
        layout=self.layout_FvB
        layout.addWidget(canvas)
        canvas.draw()
