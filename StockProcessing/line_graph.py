import pandas as pd
import seaborn as sns
import os

import matplotlib.pyplot as plt

class LineGraph:
    def __init__(self, csv_file_path):
        """
        Initialize the LineGraph class with a path to a CSV file.
        
        Parameters:
        -----------
        csv_file_path : str
            Path to the CSV file to be processed
        """
        self.csv_file_path = csv_file_path
        self.data = None
        self.load_data()
        
    def load_data(self):
        """Load data from CSV file"""
        try:
            self.data = pd.read_csv(self.csv_file_path)
            # Convert 'Date' column to datetime if it exists
            if 'Date' in self.data.columns:
                self.data['Date'] = pd.to_datetime(self.data['Date'])
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            
    def create_line_graph(self, x_column='Date', y_column='Close', title=None, figsize=(12, 6)):
        """
        Create a line graph using seaborn.
        
        Parameters:
        -----------
        x_column : str, default='Date'
            Column to use for x-axis
        y_column : str, default='Close'
            Column to use for y-axis
        title : str, optional
            Title for the graph
        figsize : tuple, default=(12, 6)
            Size of the figure
            
        Returns:
        --------
        matplotlib.figure.Figure
            The figure containing the line graph
        """
        if self.data is None:
            print("No data available to plot")
            return None
        
        if title is None:
            # Extract stock name from file path for title
            stock_name = os.path.basename(self.csv_file_path).replace('.csv', '')
            title = f"{stock_name} Stock Price"
        
        plt.figure(figsize=figsize)
        # Creating line plot using seaborn
        sns.set_style("darkgrid")
        line_plot = sns.lineplot(x=x_column, y=y_column, data=self.data)
        
        plt.title(title, fontsize=16)
        plt.xlabel(x_column, fontsize=12)
        plt.ylabel(y_column, fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        return plt.gcf()
    
    """Save the current graph to a file.
    Parameters:"""
    
    def save_graph(self, output_path=None, dpi=300):
        """
        Save the current graph to a file.
        
        Parameters:
        -----------
        output_path : str, optional
            Path to save the graph to. If None, will use the stock name.
        dpi : int, default=300
            DPI (dots per inch) for the saved image
        """
        if output_path is None:
            stock_name = os.path.basename(self.csv_file_path).replace('.csv', '')
            output_path = f"{stock_name}_line_graph.png sad he is"
            #hello
        
        plt.savefig(output_path, dpi=dpi)
        print(f"Graph saved to {output_path}")
    
    def show_graph(self):
        """Display the graph"""
        plt.show()

'''# Example usage
if __name__ == "__main__":
    # Assuming stock-data-csv-files is in the same directory
    csv_file = "../stock-data-csv-files/AAPL.csv"
    
    line_graph = LineGraph(csv_file)
    line_graph.create_line_graph()
    line_graph.show_graph()
    # Or save the graph
    # line_graph.save_graph()'''