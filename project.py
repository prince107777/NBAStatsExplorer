import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import NBADataAnalysis as nba
import NBADataloder as nbd


def main():
    # Usage
    file_path = 'NBA_Player_Stats_2023_2024_Playoffs.csv'
    loader = nbd.NBADataLoader(file_path)
    nba_df = loader.load_data()
    loader.check_nulls_and_dtypes()

    # Fill missing values and add RPG column
    percentage_columns = ['FG%', '3P%', '2P%', 'FT%', 'eFG%']
    nba_df = loader.fill_missing_values(percentage_columns)
    nba_df = loader.add_rpg_column()

    # Create analysis and visualization instance
    nba_analysis = nba.NBADataAnalysis(nba_df)
    
    while True:
        print("\nChoose an option:")
        print("1. Display Column Descriptions")
        print("2. Display Data Summary")
        print("3. Plot Top Players by Stat")
        print("4. Plot Distribution by Category (e.g., Position)")
        print("5. Plot Average Stats by Team")
        print("6. Plot Correlation Matrix of Stats")
        print("7. Plot Average Stats by Age")
        print("8. Plot Shooting Efficiency")
        print("9. Plot Team Performance")
        print("10. Plot Team Stat Summary")
        print("11. Display Top Players Table")
        print("12. Display Team Points Table")
        print("0. Exit")

        choice = input("Enter your choice (0-12): ")

        if choice == "0":
            print("Exiting the program. Have a nice day!")
            break
        elif choice == "1":
            nba_analysis.display_column_descriptions()
        elif choice == "2":
            nba_analysis.display_data_summary()
        elif choice == "3":
            stat = input("Enter the stat to display (e.g., 'PTS' for points): ")
            top_n = int(input("Enter the number of top players to display: "))
            nba_analysis.plot_top_players(stat=stat, top_n=top_n)
        elif choice == "4":
            column = 'Pos'
            xlabel = column
            ylabel = "Frequency"
            title = f"Distribution of {column} Category"
            nba_analysis.plot_distribution_by_category(column=column, xlabel=xlabel, ylabel=ylabel, title=title)
        elif choice == "5":
            group_column = 'Tm'
            stats = ['PTS', 'AST', 'RPG']
            title = "Average Points, Assists, Rebounds by Team"
            nba_analysis.plot_average_stats_by_group(group_column=group_column, stats=stats, title=title)
        elif choice == "6":
            nba_analysis.plot_correlation_matrix()
        elif choice == "7":
            nba_analysis.plot_average_stats_by_age()
        elif choice == "8":
            nba_analysis.plot_shooting_efficiency()
        elif choice == "9":
            nba_analysis.plot_team_performance()
        elif choice == "10":
            stat = input("Enter the stat for team summary (e.g., 'PTS' for points): ")
            top_n = int(input("Enter the number of top teams to display: "))
            nba_analysis.plot_team_stat_summary(stat=stat, top_n=top_n)
        elif choice == "11":
            stat = input("Enter the stat to display top players by (e.g., 'PTS' for points): ")
            num_players = int(input("Enter the number of top players to display: "))
            nba_analysis.plot_stat_leader_table(stat=stat, num_players=num_players)
        elif choice == "12":
            nba_analysis.display_team_points_table()
        else:
            print("Invalid choice. Please enter a number between 0 and 12.")

if __name__ == "__main__":
    main()
