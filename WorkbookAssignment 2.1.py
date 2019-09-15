{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "names = ['Bob','Jessica','Mary','John','Mel']\n",
    "grades = [76,95,77,78,99]\n",
    "\n",
    "GradeList = zip(names,grades)\n",
    "df = pd.DataFrame(data = GradeList,\n",
    " columns=['Names', 'Grades'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import sqlite3 as lite\n",
    "db_filename = r'datasets/mydb.db'\n",
    "con = lite.connect(db_filename)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "ename": "ProgrammingError",
     "evalue": "Cannot operate on a closed database.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mProgrammingError\u001b[0m                          Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-22-727eddcaef7d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mto_sql\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'mytable'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcon\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mschema\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mif_exists\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'replace'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mindex\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mindex_label\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mchunksize\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdtype\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mcon\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\core\\generic.py\u001b[0m in \u001b[0;36mto_sql\u001b[1;34m(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)\u001b[0m\n\u001b[0;32m   2529\u001b[0m         sql.to_sql(self, name, con, schema=schema, if_exists=if_exists,\n\u001b[0;32m   2530\u001b[0m                    \u001b[0mindex\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mindex_label\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mindex_label\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mchunksize\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mchunksize\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2531\u001b[1;33m                    dtype=dtype, method=method)\n\u001b[0m\u001b[0;32m   2532\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2533\u001b[0m     def to_pickle(self, path, compression='infer',\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\io\\sql.py\u001b[0m in \u001b[0;36mto_sql\u001b[1;34m(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)\u001b[0m\n\u001b[0;32m    458\u001b[0m     pandas_sql.to_sql(frame, name, if_exists=if_exists, index=index,\n\u001b[0;32m    459\u001b[0m                       \u001b[0mindex_label\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mindex_label\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mschema\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mschema\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 460\u001b[1;33m                       chunksize=chunksize, dtype=dtype, method=method)\n\u001b[0m\u001b[0;32m    461\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    462\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\io\\sql.py\u001b[0m in \u001b[0;36mto_sql\u001b[1;34m(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method)\u001b[0m\n\u001b[0;32m   1544\u001b[0m                             \u001b[0mif_exists\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mif_exists\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mindex_label\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mindex_label\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1545\u001b[0m                             dtype=dtype)\n\u001b[1;32m-> 1546\u001b[1;33m         \u001b[0mtable\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcreate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1547\u001b[0m         \u001b[0mtable\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minsert\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mchunksize\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1548\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\io\\sql.py\u001b[0m in \u001b[0;36mcreate\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    570\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    571\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mcreate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 572\u001b[1;33m         \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexists\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    573\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mif_exists\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'fail'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    574\u001b[0m                 raise ValueError(\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\io\\sql.py\u001b[0m in \u001b[0;36mexists\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    558\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    559\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mexists\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 560\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpd_sql\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhas_table\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mschema\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    561\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    562\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0msql_schema\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\io\\sql.py\u001b[0m in \u001b[0;36mhas_table\u001b[1;34m(self, name, schema)\u001b[0m\n\u001b[0;32m   1556\u001b[0m                  \"WHERE type='table' AND name={wld};\").format(wld=wld)\n\u001b[0;32m   1557\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1558\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mquery\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m[\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfetchall\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1559\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1560\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mget_table\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtable_name\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mschema\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\io\\sql.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m   1424\u001b[0m             \u001b[0mcur\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcon\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1425\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1426\u001b[1;33m             \u001b[0mcur\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcon\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcursor\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1427\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1428\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mkwargs\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mProgrammingError\u001b[0m: Cannot operate on a closed database."
     ]
    }
   ],
   "source": [
    "df.to_sql('mytable', con,schema=None, if_exists='replace', index=True,index_label=None,chunksize=None, dtype=None)\n",
    "\n",
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
