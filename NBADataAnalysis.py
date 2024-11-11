import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data analysis and visualization class
class NBADataAnalysis:
    def __init__(self, data):
        self.data = data

    def display_data_summary(self):
        print("Data Summary:")
        print(self.data.head())

    def display_column_descriptions(self):
    # Dictionary to store column descriptions
        column_descriptions = {
            "Rk": "Rank",
            "Player": "Player's name",
            "Pos": "Position",
            "Age": "Player's age",
            "Tm": "Team",
            "G": "Games played",
            "GS": "Games started",
            "MP": "Minutes played per game",
            "FG": "Field goals per game",
            "FGA": "Field goal attempts per game",
            "FG%": "Field goal percentage",
            "3P": "3-point field goals per game",
            "3PA": "3-point field goal attempts per game",
            "3P%": "3-point field goal percentage",
            "2P": "2-point field goals per game",
            "2PA": "2-point field goal attempts per game",
            "2P%": "2-point field goal percentage",
            "eFG%": "Effective field goal percentage",
            "FT": "Free throws per game",
            "FTA": "Free throw attempts per game",
            "FT%": "Free throw percentage",
            "ORB": "Offensive rebounds per game",
            "DRB": "Defensive rebounds per game",
            "TRB": "Total rebounds per game",
            "AST": "Assists per game",
            "STL": "Steals per game",
            "BLK": "Blocks per game",
            "TOV": "Turnovers per game",
            "PF": "Personal fouls per game",
            "PTS": "Points per game"
        }
    
        # Display the column descriptions
        print("Columns' Descriptions:\n")
        for col, description in column_descriptions.items():
            print(f"{col} : {description}")


    def plot_top_players(self, stat='PTS', top_n=10, color='skyblue'):
        top_players = self.data.nlargest(top_n, stat)
        plt.figure(figsize=(10, 6))
        plt.barh(top_players['Player'], top_players[stat], color=color)
        plt.xlabel(f'{stat} per Game')
        plt.title(f'Top {top_n} Players by {stat} per Game')
        plt.gca().invert_yaxis()
        plt.show()

    def plot_distribution_by_category(self, column, xlabel, ylabel, title, color='lightgreen'):
        counts = self.data[column].value_counts()
        counts.plot(kind='bar', color=color, figsize=(8, 6))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

    def plot_average_stats_by_group(self, group_column, stats=['PTS', 'RPG', 'AST'], title='', colormap='viridis'):
        group_stats = self.data.groupby(group_column)[stats].mean()
        group_stats.plot(kind='bar', figsize=(10, 6), colormap=colormap)
        plt.title(title)
        plt.xlabel(group_column)
        plt.ylabel('Average Stats')
        plt.show()

    def plot_correlation_matrix(self):
        numeric_columns = self.data.select_dtypes(include='number')
        correlation_matrix = numeric_columns.corr()
        plt.figure(figsize=(12, 10))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Matrix of NBA Stats')
        plt.show()

    def plot_average_stats_by_age(self):
        age_stats = self.data.groupby('Age')[['PTS', 'RPG', 'AST']].mean()
        age_stats.plot(figsize=(12, 6), marker='o')
        plt.title('Average Points, Rebounds, and Assists by Age')
        plt.xlabel('Age')
        plt.ylabel('Average Stats')
        plt.legend(['Points', 'Rebounds', 'Assists'])
        plt.show()

    def plot_shooting_efficiency(self):
        self._scatter_plot('3PA', '3P%', '3-Point Shooting Efficiency', '3-Point Attempts per Game', '3-Point Percentage', 'coral')
        self._scatter_plot('FGA', 'FG%', 'Field Goal Shooting Efficiency', 'Field Goal Attempts per Game', 'Field Goal Percentage', 'teal')

    def plot_team_performance(self):
        self.plot_average_stats_by_group('Tm', ['PTS', 'AST', 'RPG'], 'Team Performance (Average Points, Assists, Rebounds)', 'coolwarm')

    def plot_team_stat_summary(self, stat='PTS', top_n=10, color='Blues_d'):
        top_team_stats = self.data.groupby('Tm')[stat].sum().sort_values(ascending=False).head(top_n)
        self._bar_plot(top_team_stats.index, top_team_stats.values, stat, 'Team', f'Top {top_n} Teams by {stat}', color)

    def plot_stat_leader_table(self, stat='PTS', num_players=10):
        # Get the top players based on the specified stat
        top_players = self.data.nlargest(num_players, stat)[['Player', stat]]
        
        # Add a ranking column from 1 to num_players
        top_players.insert(0, 'Rank', range(1, num_players + 1))
        
        # Left-align the Player names with padding
        top_players['Player'] = top_players['Player'].str.ljust(25)
        
        # Display the table without the index
        print(f"\nTop {num_players} Players by {stat} Table:")
        print(top_players.to_string(index=False))



    def display_team_points_table(self):
        # Group by team, sum the points, and reset the index to get 'Tm' as a column
        team_points = self.data.groupby('Tm')['PTS'].sum().reset_index().sort_values(by='PTS', ascending=False)
        
        # Rename the 'PTS' column to 'Total Points' for clarity
        team_points = team_points.rename(columns={'PTS': 'Total Points'})
        
        # Reset the index to start from 1 for readability
        team_points.index = range(1, len(team_points) + 1)
        
        # Display the team points table with an index
        print("\nTeam Points Table:")
        print(team_points)


    # Utility function for bar plot with annotations
    def _bar_plot(self, x_data, y_data, ylabel, xlabel, title, color):
        sns.set(style="whitegrid")
        plt.figure(figsize=(12, 6))
        bar_plot = sns.barplot(x=x_data, y=y_data, palette=color)
        plt.xlabel(xlabel, fontsize=14)
        plt.ylabel(ylabel, fontsize=14)
        plt.title(title, fontsize=16)
        bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, horizontalalignment='right')
        for p in bar_plot.patches:
            bar_plot.annotate(f'{p.get_height():.1f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                              ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                              textcoords='offset points')
        plt.show()

    # Utility function for scatter plot
    def _scatter_plot(self, x, y, title, xlabel, ylabel, color):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data[x], self.data[y], alpha=0.7, color=color)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()



