{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "names = ['Bob','Jessica','Mary','John','Mel']\n",
    "grades = [76,95,77,78,99]\n",
    "GradeList = zip(names,grades)\n",
    "df = pd.DataFrame(data = GradeList,\n",
    "columns=['Names', 'Grades'])\n",
    "\n",
    "\n",
    "import os\n",
    "import sqlite3 as lite\n",
    "db_filename = r'mydb.db'\n",
    "con = lite.connect(db_filename)\n",
    "df.to_sql('mytable1',\n",
    "con,\n",
    "schema=None,\n",
    "if_exists='replace',\n",
    "index=True,\n",
    "index_label=None,\n",
    "chunksize=None,\n",
    "dtype=None)\n",
    "con.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
