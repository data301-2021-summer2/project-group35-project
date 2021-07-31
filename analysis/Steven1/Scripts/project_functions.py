{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "598cdf38-a357-4e7e-88aa-7cc7baf68be8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import numpy as np\n",
    "import os\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas_profiling\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9e5ee6d6-7239-4cd5-8875-c85d04d908f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Method Chaining by Year\n",
    "\n",
    "def load_and_process_df_Method_Chain_by_Year(path_to_csv_file):\n",
    "\n",
    "    df_Method_Chain_by_Year1 = (\n",
    "        pd.read_csv(\"/Users/stevenzonneveld/Desktop/data301/project-group35-project/data/raw/MileStone1.csv\")\n",
    "        .drop(columns = ['Unnamed: 0', 'price', 'title_status', 'color', 'state', 'mileage'], axis = 0)\n",
    "        .sort_values(by = ['brand'])\n",
    "        #.drop( df_cleaned [ df_cleaned ['brand'] == 'peterbilt'].index, inplace=True)  #could not figure out how to use .drop in method chaining.\n",
    "        .rename(columns = {\"brand\": \"Manufacturer\", \"year\": \"Model Year\"})   \n",
    "    )\n",
    "    df_Method_Chain_by_Year2 = df_Method_Chain_by_Year1.drop( df_Method_Chain_by_Year [ df_Method_Chain_by_Year ['Manufacturer'] == 'peterbilt'].index, inplace=True)\n",
    "   \n",
    "    return df_Method_Chain_by_Year2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4567b59b-f1b2-46af-9e98-8767b599ce69",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Method Chaining by Mileage\n",
    "\n",
    "def load_and_process_df_Method_Chain_by_Mileage(path_to_csv_file):\n",
    "\n",
    "    df_Method_Chain_by_Mileage1 = (\n",
    "        pd.read_csv(\"/Users/stevenzonneveld/Desktop/data301/project-group35-project/data/raw/MileStone1.csv\")\n",
    "        .drop(columns = ['Unnamed: 0', 'price', 'title_status', 'color', 'state', 'year'], axis = 0)\n",
    "        .sort_values(by = ['brand'])\n",
    "        #.drop( df_cleaned [ df_cleaned ['brand'] == 'peterbilt'].index, inplace=True) #could not figure out how to use .drop in method chaining.\n",
    "        #.drop( df_cleaned [ df_cleaned ['mileage'] == 0.0 ].index, inplace=True)      #could not figure out how to use .drop in method chaining.    \n",
    "        .rename(columns = {\"brand\": \"Manufacturer\", \"mileage\": \"Mileage\"})\n",
    "    )\n",
    "    df_Method_Chain_by_Mileage2 = df_Method_Chain_by_Mileage1.drop( df_Method_Chain_by_Mileage [ df_Method_Chain_by_Mileage ['Manufacturer'] == 'peterbilt'].index, inplace=True)\n",
    "    df_Method_Chain_by_Mileage3 = df_Method_Chain_by_Mileage2.drop( df_Method_Chain_by_Mileage [ df_Method_Chain_by_Mileage ['Mileage'] == 0.0 ].index, inplace=True)\n",
    "    \n",
    "    return df_Method_Chain_by_Mileage3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b28f5cd6-431c-403f-987f-26c68490640c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
