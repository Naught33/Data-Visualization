import pandas as pd
import json
import logging
from essentials import connection_database

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class visualize:
    def __init__(self):
        # Initialize the database connection and load the data
        try:
            logging.info("Initializing database connection and loading data.")
            new_conn = connection_database()
            self.df = new_conn.refine_data()
            logging.info("Data loaded successfully.")
        except Exception as e:
            logging.error(f"Error initializing database connection: {e}")
            self.df = pd.DataFrame()  # Empty DataFrame as a fallback

    def show_db(self) -> dict:
        """Returns the entire dataset as a JSON object."""
        try:
            return self.df.to_json()
        except Exception as e:
            logging.error(f"Error in show_db: {e}")
            return {"error": "Could not retrieve dataset"}

    def show_columns(self) -> list:
        """Returns a list of column names in the dataset."""
        try:
            return list(self.df.columns)
        except Exception as e:
            logging.error(f"Error in show_columns: {e}")
            return {"error": "Could not retrieve column names"}

    def count_bar(self, filter: str) -> dict:
        """Returns the count of values in a specified column."""
        try:
            if filter in self.df.columns:
                return self.df[filter].value_counts().head(10).to_json()
            else:
                error_msg = f"Column '{filter}' not found in dataset"
                logging.error(error_msg)
                return {"error": error_msg}
        except Exception as e:
            logging.error(f"Error in count_bar: {e}")
            return {"error": "Error processing count_bar"}

    def constrains_bar(self, filter1: str, constrain: str, filter2: str) -> dict:
        """Filters data based on a constraint and returns counts of another column."""
        try:
            if filter1 in self.df.columns and filter2 in self.df.columns:
                filtered_df = self.df[self.df[filter1] == constrain]
                return filtered_df[filter2].head(10).to_json()
            else:
                error_msg = f"One or both columns '{filter1}' or '{filter2}' not found in dataset"
                logging.error(error_msg)
                return {"error": error_msg}
        except Exception as e:
            logging.error(f"Error in constrains_bar: {e}")
            return {"error": "Error processing constrains_bar"}

    def groupby_histo(self, filter1: str, filter2: str) -> dict:
        """Groups data by two columns and returns their aggregated counts."""
        try:
            if filter1 in self.df.columns and filter2 in self.df.columns:
                grouped_df = self.df.groupby([filter1, filter2]).size().unstack()
                grouped_df['sum'] = grouped_df.sum(axis=1)
                sorted_df = grouped_df.sort_values(by='sum', ascending=False).head(10).drop(columns=['sum'])
                return sorted_df.to_json()
            else:
                error_msg = f"One or both columns '{filter1}' or '{filter2}' not found in dataset"
                logging.error(error_msg)
                return {"error": error_msg}
        except Exception as e:
            logging.error(f"Error in groupby_histo: {e}")
            return {"error": "Error processing groupby_histo"}

    def count_line(self, filter: str) -> dict:
        """Groups data by a column and returns its counts over time."""
        try:
            if filter in self.df.columns:
                return self.df.groupby([filter]).size().head(10).to_json()
            else:
                error_msg = f"Column '{filter}' not found in dataset"
                logging.error(error_msg)
                return {"error": error_msg}
        except Exception as e:
            logging.error(f"Error in count_line: {e}")
            return {"error": "Error processing count_line"}

    def get_uniq_values(self, filter: str) -> str:
        """Returns unique values from a specified column as a JSON array."""
        try:
            if filter in self.df.columns:
                unique_values = self.df[filter].unique().tolist()
                return json.dumps(unique_values)
            else:
                error_msg = f"Column '{filter}' not found in dataset"
                logging.error(error_msg)
                return json.dumps({"error": error_msg})
        except Exception as e:
            logging.error(f"Error in get_uniq_values: {e}")
            return json.dumps({"error": "Error processing get_uniq_values"})


if __name__ == "__main__":
    new_vis = visualize()
    try:
        # Example usages for testing
        print("Columns:", new_vis.show_columns())
        print("Count Bar:", new_vis.count_bar('country'))
        print("Constrained Bar:", new_vis.constrains_bar('country', 'India', 'likelihood'))
        print("Group by Histogram:", new_vis.groupby_histo('country', 'likelihood'))
        print("Count Line:", new_vis.count_line('start_year'))
        print("Unique Values:", new_vis.get_uniq_values('country'))
    except Exception as main_exception:
        logging.error(f"Error during main execution: {main_exception}")
